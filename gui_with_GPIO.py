import pygame.gfxdraw,math,time
import RPi.GPIO as GPIO

#GPIO Setup
LED_pin_red = 37
LED_pin_green = 35
LED_pin_yellow = 33
LED_red_output = 0
LED_green_output =0
LED_yellow_output = 0
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_pin_red,GPIO.OUT)
GPIO.setup(LED_pin_green,GPIO.OUT)
GPIO.setup(LED_pin_yellow,GPIO.OUT)

Q=113
blue_color = (18, 186, 231)
class Screen(object):
    def __init__(self):
        sundry = pygame.init()
        self.sstimeout = time.time()
        self.ssactive = False
        self.width = pygame.display.Info().current_w
        self.height = pygame.display.Info().current_h
        self.screen = pygame.display.set_mode((self.width,self.height),pygame.FULLSCREEN)
        self.screen.fill(blue_color)
        pygame.display.update()
        self.page = ''
    def sstimeoutcheck(self):
        if time.time() - self.sstimeout > 150:
            self.ssactive = True
    def clearss(self):
        self.ssactive = False
        self.sstimeout = time.time()
    def setpage(self,page):
        self.page = page
    def refresh(self):
        if self.ssactive:
            self.screen.fill((0,0,0,))
        else:
            self.screen.fill(blue_color)
            font = pygame.font.Font(None, 45)
            font = pygame.font.SysFont("Vera", 45)
            text = font.render(self.page.title, True,(212, 55, 34))
            w = text.get_width()
            h = text.get_height()
            self.screen.blit(text, (self.width/2 - w/2,5))
            # pygame.draw.lines(self.screen,(0,0,0),False,[(int(self.width/2),0),(int(self.width/2),self.height)])
            # pygame.draw.lines(self.screen,(0,0,0),False,[(0,int(self.height/2)),(self.width,int(self.height/2))])
            for button in self.page.buttons:
                button.render(self.screen,self.width,self.height)
        pygame.display.update()

    def detect_selection(self,coords):
        self.sstimeout = time.time()
        self.ssactive = False

        for button in self.page.buttons:
            x,y = button.detect_selection(coords,self.width,self.height)

            if x >0:
                # return self.page.title, button.detect_selection(coords,self.width,self.height)
                return self.page.title,(x,y)
        return "",(0,"")

class Page(object):
    def __init__(self,title):
        self.title = title
        self.buttons = []
    def add_input(self,button):
        self.buttons.append(button)

class Button(object):
    def __init__(self,x,y,text,value):
        self.x = x
        self.y = y
        self.text = text
        self.value = value

class Square(Button):
    def __init__(self,x,y,d,text,value):
        self.type = 'square'
        self.d = d
        Button.__init__(self,x,y,text,value)

    def render(self,screen):
        ul = (self.x,self.y)
        lr = (self.x+self.d,self.y+self.d)
        ll = (self.x, self.y + self.d)
        ur = (self.y + self.d,self.x)
        corners = (ul,ur,lr,ll)
        pygame.gfxdraw.filled_polygon(screen,corners,(129,138,148))
    def detect_selection(self,coords,w,h):
        a = coords[0]
        b = coords[1]

        if (a >=self.x and a<=(self.x + self.d) and b>=self.y and b<(self.y + self.d)):
            return self.value,self.text
        else:
            return 0,""

class Rect(Button):
    def __init__(self,x,y,l,w,text,value):
        self.type = 'rect'
        self.l = l
        self.w = w
        Button.__init__(self,x,y,text,value)

    def render(self,screen):
        ul = (self.x,self.y)
        lr = (self.x+self.l,self.y+self.w)
        ll = (self.x, self.y + self.w)
        ur = (self.x + self.l,self.y)
        corners = (ul,ur,lr,ll)
        pygame.gfxdraw.filled_polygon(screen,corners,(129,138,148))
    def detect_selection(self,coords,w,h):
        a = coords[0]
        b = coords[1]
        if (a >=self.x and a<=(self.x + self.l) and b>=self.y and b<(self.y + self.w)):
            return self.value, self.text
        else:
            return 0,""
class Circle(Button):
    def __init__(self,x,y,r,text,value):
        self.type = 'circle'
        self.r = r
        Button.__init__(self,x,y,text,value)
    def render(self,screen):
        # pygame.gfxdraw.filled_circle(screen,self.x,self.y,self.r,(129, 138, 148))
        pygame.draw.circle(screen,(129, 138, 148),(self.x*w,self.y*h),self.r,1)
    def detect_selection(self,coords,w,h):
        a = coords[0]
        b = coords[1]
        if (math.sqrt((self.x*w-a)**2 + (self.y*h-b)**2)<self.r*w):
            return self.value, self.text
        else:
            return 0, ""

class Icons(object):
    def __init__(self):
        self.grb = pygame.image.load('green_round_button.png').convert_alpha()
        self.yrb = pygame.image.load('yellow_round_button.png').convert_alpha()
        self.rrb = pygame.image.load('red_round_button.png').convert_alpha()

class RedRoundButton(Circle):
    def __init__(self,x,y,r,text,value):
        super(RedRoundButton,self).__init__(x,y,r,text,value)
        self.icons = Icons()
        self.image = self.icons.rrb
        self.type = 'rrb'
    def render(self,screen,w,h):
        self.image  = pygame.transform.smoothscale(self.image,(int(self.r*2*w),int(self.r*2*w)))
        screen.blit(self.image,(int((self.x-self.r)*w),int((self.y*h-self.r*w))))

class YellowRoundButton(Circle):
    def __init__(self,x,y,r,text,value):
        super(YellowRoundButton,self).__init__(x,y,r,text,value)
        self.icons = Icons()
        self.image = self.icons.yrb
        self.type = 'grb'
    def render(self,screen,w,h):
        self.image  = pygame.transform.smoothscale(self.image,(int(self.r*2*w),int(self.r*2*w)))
        screen.blit(self.image,(int((self.x-self.r)*w),int((self.y*h-self.r*w))))

class GreenRoundButton(Circle):
    def __init__(self,x,y,r,text,value):
        super(GreenRoundButton,self).__init__(x,y,r,text,value)
        self.icons = Icons()
        self.image = self.icons.grb
        # self.grb = pygame.image.load('green_round_button.png').convert_alpha()
        self.type = 'grb'
    def render(self,screen,w,h):
        # self.image = pygame.image.load('green_round_button.png').convert_alpha()
        self.image  = pygame.transform.smoothscale(self.image,(int(self.r*2*w),int(self.r*2*w)))
        screen.blit(self.image,(int((self.x-self.r)*w),int((self.y*h-self.r*w))))
        #pygame.draw.lines(screen,(0,0,0),False,[(self.x-200,self.y),(self.x+200,self.y)])
        # pygame.draw.lines(screen,(0,0,0),False,[(self.x,self.y-200),(self.x,self.y+200)])
        # Circle.render(self,screen)

# define pages
pygame.init()
screen1 = Screen()
home_page = Page("Main")
second_page = Page("Settings")
button1 = GreenRoundButton(.2,.2,.05,"Green",7)
button2 = YellowRoundButton(.2,.5,.05,"Yellow",8)
button3 = RedRoundButton(.2,.8,.05,"Red",9)
home_page.add_input(button1)
home_page.add_input(button2)
home_page.add_input(button3)

# define the screen

screen1.setpage(home_page)
screen1.refresh()

loop = True
while loop:
    value =0
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == Q:
                loop = False
            if event.key == 49: #pressed 1 key
                print "switching to home page"
                screen1.setpage(home_page)
                screen1.refresh()
            if event.key == 50: #pressed 2 key
                print "switching to second page"
                screen1.setpage(second_page)
                screen1.refresh()
        if event.type == pygame.MOUSEBUTTONUP:
            if screen1.ssactive == True:
                screen1.clearss()
            else:
                source_page, stuff = screen1.detect_selection(pygame.mouse.get_pos())
                value = stuff[0]
                text = stuff[1]

    if value > 0:
        if source_page == "Main":
            if value == 7:
                LED_green_output ^=1
                GPIO.output(LED_pin_green,LED_green_output)
            if value == 8:
                LED_yellow_output ^=1
                GPIO.output(LED_pin_yellow,LED_yellow_output)
            if value == 9:
                LED_red_output ^=1
                GPIO.output(LED_pin_red,LED_red_output)
                # screen1.setpage(second_page)
        if source_page == "Settings":
            screen1.setpage(home_page)

    screen1.sstimeoutcheck()
    screen1.refresh()

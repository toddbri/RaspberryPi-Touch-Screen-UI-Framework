import pygame.gfxdraw,math,time
Q=113
blue_color = (97, 159, 182)
class Screen(object):
    def __init__(self):
        blue_color = (18, 186, 231)
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
            text = font.render(self.page.title, True, (0,255, 0))
            w = text.get_width()
            h = text.get_height()
            self.screen.blit(text, (self.width/2 - w/2,5))
            for button in self.page.buttons:
                button.render(self.screen)
        pygame.display.update()

    def detect_selection(self,coords):
        self.sstimeout = time.time()
        self.ssactive = False

        for button in self.page.buttons:
            x = button.detect_selection(coords)[0]
            if x >0:
                return self.page.title, button.detect_selection(coords)
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
    def detect_selection(self,coords):
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
    def detect_selection(self,coords):
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
        pygame.draw.circle(screen,(129, 138, 148),(self.x,self.y),self.r,1)
    def detect_selection(self,coords):
        a = coords[0]
        b = coords[1]
        if (math.sqrt((self.x-a)**2 + (self.y-b)**2)<self.r):
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
    def render(self,screen):
        self.image  = pygame.transform.smoothscale(self.image,(self.r*2,self.r*2))
        screen.blit(self.image,(self.x-self.r,self.y-self.r))

class YellowRoundButton(Circle):
    def __init__(self,x,y,r,text,value):
        super(YellowRoundButton,self).__init__(x,y,r,text,value)
        self.icons = Icons()
        self.image = self.icons.yrb
        self.type = 'grb'
    def render(self,screen):
        self.image  = pygame.transform.smoothscale(self.image,(self.r*2,self.r*2))
        screen.blit(self.image,(self.x-self.r,self.y-self.r))

class GreenRoundButton(Circle):
    def __init__(self,x,y,r,text,value):
        super(GreenRoundButton,self).__init__(x,y,r,text,value)
        self.icons = Icons()
        self.grb = pygame.image.load('green_round_button.png').convert_alpha()
        self.type = 'grb'
    def render(self,screen):
        self.image = pygame.image.load('green_round_button.png').convert_alpha()
        self.image = self.icons.grb
        self.image  = pygame.transform.smoothscale(self.image,(self.r*2,self.r*2))
        screen.blit(self.image,(self.x-self.r,self.y-self.r))
        # pygame.draw.lines(screen,(0,0,0),False,[(self.x-200,self.y),(self.x+200,self.y)])
        # pygame.draw.lines(screen,(0,0,0),False,[(self.x,self.y-200),(self.x,self.y+200)])
        # Circle.render(self,screen)

# define pages
pygame.init()
screen1 = Screen()
home_page = Page("Main")
second_page = Page("Settings")
button1 = Square(200,200,50,"Select Zone",1)
home_page.add_input(button1)
button2 = Circle(450,200,30,"Back",3)
button3 = Circle(200,300,25,"Turn on",1)
button4 = Rect(100,100,50,30,"Run for 5 minutes",2)
button5 = GreenRoundButton(600,600,75,"Red",9)
button6 = YellowRoundButton(300,300,60,"Yellow",9)
button7 = RedRoundButton(300,500,60,"Yellow",9)
home_page.add_input(button6)
home_page.add_input(button5)
home_page.add_input(button7)
second_page.add_input(button4)
home_page.add_input(button2)
second_page.add_input(button3)


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
            screen1.setpage(second_page)
        if source_page == "Settings":
            screen1.setpage(home_page)

    screen1.sstimeoutcheck()
    screen1.refresh()

import pygame.gfxdraw,math,time
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

class Slider(object):
    def __init__(self,x,y,h,w,text,value):
        pass

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

    def render(self,screen,w,h):
        self.ul = (int(self.x*w - self.d*w/2),int(self.y*h - self.d*w/2))
        self.lr = (int(self.x*w + self.d*w/2),int(self.y*h + self.d*w/2))
        self.ll = (int(self.x*w - self.d*w/2),int(self.y*h + self.d*w/2))
        self.ur = (int(self.x*w + self.d*w/2),int(self.y*h - self.d*w/2))
        corners = (self.ul,self.ur,self.lr,self.ll)
        pygame.gfxdraw.filled_polygon(screen,corners,(129,138,148))
    def detect_selection(self,coords,w,h):
        a = coords[0]
        b = coords[1]
        if (a >=int(self.x*w - self.d*w/2) and a<=int(self.x*w + self.d*w/2) and b>=int(self.y*h - self.d*w/2) and b<=int(self.y*h + self.d*w/2)):
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
    def render(self,screen,w,h):
        # pygame.gfxdraw.filled_circle(screen,self.x,self.y,self.r,(129, 138, 148))
        pygame.draw.circle(screen,(129, 138, 148),(int(self.x*w),int(self.y*h)),int(self.r*w),1)
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
        self.home = pygame.image.load('orange_house.png').convert_alpha()
        self.gear = pygame.image.load('blue_gear.png').convert_alpha()

class RedRoundButton(Circle):
    def __init__(self,x,y,r,text,value):
        super(RedRoundButton,self).__init__(x,y,r,text,value)
        self.icons = Icons()
        self.image = self.icons.rrb
        self.type = 'rrb'
    def render(self,screen,w,h):
        self.image  = pygame.transform.smoothscale(self.image,(int(self.r*2*w),int(self.r*2*w)))
        screen.blit(self.image,(int((self.x-self.r)*w),int((self.y*h-self.r*w))))
        # Circle.render(self,screen,w,h)

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
        # self.icons = Icons()
        # self.image = self.icons.grb
        self.image = Icons().grb
        # self.grb = pygame.image.load('green_round_button.png').convert_alpha()
        self.type = 'grb'
    def render(self,screen,w,h):
        # self.image = pygame.image.load('green_round_button.png').convert_alpha()
        self.image  = pygame.transform.smoothscale(self.image,(int(self.r*2*w),int(self.r*2*w)))
        screen.blit(self.image,(int((self.x-self.r)*w),int((self.y*h-self.r*w))))
        #pygame.draw.lines(screen,(0,0,0),False,[(self.x-200,self.y),(self.x+200,self.y)])
        # pygame.draw.lines(screen,(0,0,0),False,[(self.x,self.y-200),(self.x,self.y+200)])
        # Circle.render(self,screen)
class BlueGear(Circle):
    def __init__(self,x,y,r,text,value):
        self.image = Icons().gear
        Circle.__init__(self,x,y,r,text,value)
    def render(self,screen,w,h):
        self.image = pygame.transform.smoothscale(self.image,(int(self.r*2*w),int(self.r*2*w)))
        screen.blit(self.image,(int(self.x*w-self.r*w),int(self.y*h-self.r*w)))
        # Circle.render(self,screen,w,h) #turn on to enable debugging on location detection.
class HomeButton(Square):
    def __init__(self,x,y,d,text,value):
        self.nativex = 298.0 #Enter as float
        self.nativey = 282.0 #Enter as float
        self.image = Icons().home
        Square.__init__(self,x,y,d,text,value)

    def render(self,screen,w,h):
        self.image = pygame.transform.smoothscale(self.image,(int(self.d*w),int(self.d*w*(self.nativey/self.nativex))))
        screen.blit(self.image,(int(self.x*w-self.d*w/2),int(self.y*h-self.d*w/2)))
        # Square.render(self,screen,w,h) #Enable for location debuggin

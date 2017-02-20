import pygame.gfxdraw,math,time
from TouchScreenFramework import *
onRPi = False
try:
    import RPi.GPIO as GPIO
    onRPi = True
except ImportError:
    pass
print onRPi

#GPIO Setup
LED_pin_red = 37
LED_pin_green = 35
LED_pin_yellow = 33
LED_red_output = 0
LED_green_output =0
LED_yellow_output = 0
if onRPi:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED_pin_red,GPIO.OUT)
    GPIO.setup(LED_pin_green,GPIO.OUT)
    GPIO.setup(LED_pin_yellow,GPIO.OUT)

Q=113

# define pages
pygame.init()
screen1 = Screen()
home_page = Page("Main")
second_page = Page("Settings")
button1 = GreenRoundButton(.2,.3,.05,"Green",7)
button2 = YellowRoundButton(.2,.5,.05,"Yellow",8)
button3 = RedRoundButton(.2,.7,.05,"Red",9)
button4 = BlueGear(.9,.1,.015,"Settings",5)
button5 = HomeButton(.9,.1,.03,"Home",5)
home_page.add_input(button1)
home_page.add_input(button2)
home_page.add_input(button3)
home_page.add_input(button4)
second_page.add_input(button5)
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
                if onRPi:
                    LED_green_output ^=1
                    GPIO.output(LED_pin_green,LED_green_output)
            if value == 8:
                if onRPi:
                    LED_yellow_output ^=1
                    GPIO.output(LED_pin_yellow,LED_yellow_output)
            if value == 9:
                if onRPi:
                    LED_red_output ^=1
                    GPIO.output(LED_pin_red,LED_red_output)
            if value == 5:
                screen1.setpage(second_page)
        if source_page == "Settings":
            if value == 5:
                screen1.setpage(home_page)

    screen1.sstimeoutcheck()
    screen1.refresh()

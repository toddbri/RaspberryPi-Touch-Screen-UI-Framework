##Synopsis

This is a Touch UI framework for the Raspberry Pi 3. It has only been tested with the [Raspberry Pi touch display](https://www.raspberrypi.org/products/raspberry-pi-touch-display/) and the Raspbian Jessie distribution.
The drivers for the RPi touch display are included in the Jessie distribution. This framework is build on the [pygame module](http://www.pygame.org/lofi.html).

##Overview

The Framework is contained in the module TouchScreenFramework.py. The framework handles rendering and touch detection. The organization of the framework is as follows: the top of the hierarchy is the Screen object. There is one screen object. The screen can contain multiple page objects. Page objects can contain multiple input objects. The input object can be arbitrarily placed on a page and given an arbitrary size.

##Usage

###   1. Importing the module.

The module is imported into user code as follows:

```        from TouchScreenFramework import *```

###   2. Screen object.

In the user's code the screen object must be created before any other objects.

```screen_name = Screen()```

###   3. Page objects.

Page objects are created after the screen object is created. Multiple page objects can be created. Each page is named by passing a string to the Page object.

```page_name = Page("Home")```

###   4. Input Objects.

Input objects can be created and added to pages. The currently supported input objects are:

* Green Round Button
* Yellow Round Button
* Red Round Button
* Blue Gear Icon
* Orange Home Icon
* Slider control

When each object is created is it given a location, size, label, and return value. The x, y location is specified as a percentage of the screen width and height with values from 0 to 1.0 (ie: a value of 0.5, 0.5 would place the object in the center of the screen). The size of the objects are also specified in percentage of screen width with values from 0 to 1.0.

#### Input object formats:

#####Green Round Button:

```button_name = GreenRoundButton(x, y, diameter, "label", return_value)```

Ex: button1 = GreenRoundButton(.2,.3,.05,"Trigger",18)

This example would place a button of diameter 5% of the screen width centered at the location 20% of the screen width over and 30% of the screen height down. When pressed the framework will return the name of the page, the button label, and return value.

The format is the same for the YellowRoundButton and RedRoundButton.


#####Blue Gear Button:

```button_name = BlueGear(x, y, diameter, "label", return_value)```

#####Orange Home Button:

```button_name = HomeButton(x, y, dimension, "label", return_value)```

#####Slider control:

```slider_name = Slider(x, y, h, w, "label",return_value)```

The x, h, w values are expressed as percentage of screen width. The y value is expressed as a percentage of screen height.

###Adding input objects to the page

```page_name.add_input(button_name)```

###5. Changing pages.

The displayed page is changed by calling the setpage() method on the Screen object and passing the name of the page object.

```screen.setpage(page_name)```

###6. Refreshing the page.

The page can be refreshed by calling the refresh() method on the Screen object.

```screen_name.refresh()```

###7. Detecting user input.

The user's code detects user input by calling the getevent() method on the Screen object.

```source_page, return_values = screen_name.getevent()```

source_page will contain the label value of the page the input object was on. The return_values variable is a tuple containing first the label of the input object detected and the specified return value set during creation of the input object.

If no touch event is detected the source_page will be set to "" and the return_values to (0,""). If a physical keyboard is available the source_page value will be "keyboard" and the return_values will be (event.key,"") where event.key is the value of the key pressed.

Provide code examples and explanations of how to get the project.

##Planned Updates

Describe and show how to run the tests with code examples.

##License

A short snippet describing the license (MIT, Apache, etc.)

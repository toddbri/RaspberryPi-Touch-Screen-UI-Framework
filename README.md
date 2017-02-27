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

In the user code the first screen object must be created before any other objects.

```screen = Screen()```

###   3. Page objects.

Page objects are created after the screen object is created. Multiple page objects can be created. Each page is named by passing a string to the Page object.

```page1 = Page("Home")```

###   4. Input Objects.

Input objects can be created and added to any page. The currently supported input objects are:

* Green Round Button
* Yellow Round Button
* Red Round Button
* Blue Gear Icon
* Orange Home Icon
* Slider control

When each object is created is it given a location, size, label, and return value. The x, y location is specified as a percentage of the screen width and height with values from 0 to 1.0 (ie: a value of 0.5, 0.5 would place the object in the center of the screen). The size of the objects are also specified in percentage of screen width with values from 0 to 1.0.

#### Input object formats:

Green Round Button:

```button_name = GreenRoundButton(x, y, diameter, "Label", return_value)```

Ex: button1 = GreenRoundButton(.2,.3,.05,"Label1",18)

This would place a button of diameter 5% of the screen width centered at the location 20% of the screen width over and 30% of the screen height down. When pressed the framework would will return the name of the page, the button label, and return value.

The format is the same for the YellowRoundButton and RedRoundButton.


Blue Gear Button:

```button_name = BlueGear(x, y, diameter, "label", return_value)```


##Installation

Provide code examples and explanations of how to get the project.

##Tests

Describe and show how to run the tests with code examples.

##License

A short snippet describing the license (MIT, Apache, etc.)

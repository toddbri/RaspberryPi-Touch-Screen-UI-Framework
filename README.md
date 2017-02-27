##Synopsis

This is a Touch UI framework for the Raspberry Pi 3. It has only been tested with the [Raspberry Pi touch display](https://www.raspberrypi.org/products/raspberry-pi-touch-display/) and the Raspbian Jessie distribution.
The drivers for the RPi touch display are included in the Jessie distribution. This framework is build on the [pygame module](http://www.pygame.org/lofi.html).

##Overview

The Framework is contained in the module TouchScreenFramework.py. The framework handles rendering and touch detection. The organization of the framework is as follows: the top of the hierarchy is the Screen object. There is one screen object. The screen can contain multiple page objects. Page objects can contain multiple input objects. The input object can be arbitrarily placed on a page and given an arbitrary size.

##Usage

  #Importing the module:

    The module is imported into user code as follows:

```from TouchScreenFramework import *```

##Installation

Provide code examples and explanations of how to get the project.

##Tests

Describe and show how to run the tests with code examples.

##License

A short snippet describing the license (MIT, Apache, etc.)

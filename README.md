Our atempt at creating an operating system like program for micropython devices.

Display library is: https://github.com/devbis/st7789py_mpy
And text function is from: https://github.com/adafruit/micropython-adafruit-rgb-display/blob/master/rgb_text.py

If you want it to run at boot put 'import microOS' into your boot.py file.

TODO:

fix menu bug so that first app menu option stays shown.

Fix bug where the time is slightly off (up to around a minute)

add more options to the main menu.

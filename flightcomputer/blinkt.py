#!/usr/bin/python
from blinkt import set_pixel, show
from time import sleep

# Blink the 2,4,6 lights bright white
# These are the lights not used by GPS, temperature or camera status

while True:
    set_pixel(2,255,255,255)
    set_pixel(4,255,255,255)
    set_pixel(6,255,255,255)
    show()
    sleep(2)
    set_pixel(2,0,0,0)
    set_pixel(4,0,0,0)
    set_pixel(6,0,0,0)
    show()
    sleep(0.5)

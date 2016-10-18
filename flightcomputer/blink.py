#!/usr/bin/python
from blinkt import set_pixel, show
from time import sleep

def st(lednumber, colour):
    if colour == 'green':
        set_pixel(lednumber,0,0,64)
    if colour == 'red':
        set_pixel(lednumber,0,64,0)
    if colour == 'blue':
        set_pixel(lednumber,64,0,0)
    if colour == "white":
        set_pixel(lednumber,64,64,64)
    if colour == "off":
        set_pixel(lednumber,0,0,0)
        

set_pixel(0,0,0,0)
set_pixel(1,0,0,0)
set_pixel(2,0,0,0)
set_pixel(3,0,0,0)
set_pixel(4,0,0,0)
set_pixel(5,0,0,0)
set_pixel(6,0,0,0)
set_pixel(7,0,0,0)
show()
sleep(1)
while True:
    try:
        f = open('/tmp/gpsstatus', 'r')
        st(2, f.readline().strip())
        f.close()
        show()
    except Exception as inst:
        print "No GPS Status"
        print inst
        set_pixel(2,0,0,0)
        show()
    try:
        f = open('/tmp/temperaturestatus', 'r')
        st(4, f.readline().strip())
        f.close()
        show()
    except Exception as inst:
        print "No temperature Status"
        print inst
        set_pixel(4,0,0,0)
        show()
    try:
        f = open('/tmp/camerastatus', 'r')
        st(6, f.readline().strip())
        f.close()
        show()
    except Exception as inst:
        print "No camera Status"
        print inst
        set_pixel(6,0,0,0)
        show()
    sleep(1)

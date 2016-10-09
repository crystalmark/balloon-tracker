#!/usr/bin/python
import time
import picamera
from blinkt import set_pixel, show

def status(colour):
    try:
        f = open("camerastatus", "w+")
        f.write(colour)
        f.close()
    except:
        print "Unable to write camera status"

try:
    with picamera.PiCamera() as camera:
	    camera.resolution = (640, 480)
	    camera.framerate=90
	    status("green")
	    # set_pixel(1,0,0,255)
	    # show()
	    camera.start_recording('/home/pi/Video/%d.h264' % time.time())
	    camera.wait_recording(60)
	    for i in range(2, 2000):
	        camera.split_recording('/home/pi/Video/%d.h264' % time.time())
	        camera.wait_recording(60)
	    camera.stop_recording()
except:
	    status("red")
	    # set_pixel(1,255,0,0)
	    # show()
	    # sleep(120)
	    raise


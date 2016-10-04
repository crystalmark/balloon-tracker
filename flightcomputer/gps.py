#!/usr/bin/python
import gps
import time

from blinkt import set_pixel, show
from time import sleep

import logging 
from logging.handlers import TimedRotatingFileHandler

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

logger = logging.getLogger("GPS Log")
logger.setLevel(logging.INFO)
sensor = TimedRotatingFileHandler('gps' , when='M', interval=10)
logger.addHandler(sensor)

while True:
    try:
    	report = session.next()
	    set_pixel(3,0,0,255)
	    show()
	    logger.info(report)
	time.sleep(5)
    except:
		session = None
		print "GPSD has terminated"
		set_pixel(3,255,0,0)
		show()
		sleep(120)


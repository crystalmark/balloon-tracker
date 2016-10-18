#!/usr/bin/python
import time
import logging 
from logging.handlers import TimedRotatingFileHandler

def status(colour):
    try:
        f = open("/tmp/temperaturestatus", "w+")
        f.write(colour)
        f.close()
    except Exception as e:
        print e
        print "Unable to write temperature status"

def read(id):
    status("green")
    tfile = open("/sys/bus/w1/devices/%s/w1_slave" % id) 
    text = tfile.read() 
    tfile.close() 
    secondline = text.split("\n")[1] 
    temperaturedata = secondline.split(" ")[9] 
    temperature = float(temperaturedata[2:]) 
    temperature = temperature / 1000 
    return "%s,%s,%s" % (id, time.time(), temperature)

logger = logging.getLogger("Temperature Log")
logger.setLevel(logging.INFO)

sensor = TimedRotatingFileHandler('/home/pi/temperature' , when='M', interval=10)
logger.addHandler(sensor)

while True:
    logger.info(read('28-800000281770'))
    logger.info(read('28-80000028041a'))
    time.sleep(0.5)
    status("off")
    time.sleep(10)

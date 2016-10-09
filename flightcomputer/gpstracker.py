#!/usr/bin/python

import os 
from gps import *
from time import *
import time 
import threading 
import jsonpickle
from time import sleep
import logging
from logging.handlers import TimedRotatingFileHandler


def status(colour):
    try:
        f = open("gpsstatus", "w+")
        f.write(colour)
        f.close()
    except:
        print "Unable to write GPS status"


class GpsPoller(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.session = gps(mode=WATCH_ENABLE)
        self.current_value = None 
        self.running = True 

    def get_current_value(self):
        return self.current_value

    def run(self):
        try:
            while self.running:
                self.current_value = self.session.next() 
        except StopIteration:
            pass

if __name__ == '__main__':
    gpsp = GpsPoller()
    try: 
        status("red")
	logger = logging.getLogger("GPS Log")
        logger.setLevel(logging.INFO)
        sensor = TimedRotatingFileHandler('/home/pi/gps' , when='M', interval=10)
        logger.addHandler(sensor)

        gpsp.start() 
        while True:
            # print("GPS Log...")
            report = gpsp.get_current_value()
            # print report
            try: 
                if report.keys()[0].startswith('ep'):
                    status("green")
                    logger.info("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (time.time(), report['time'], report['lat'], report['lon'], report['alt'], report['climb'], report['epx'], report['epy'], report['epv'], report['track']))
                time.sleep(.5)
                status("blue")
                time.sleep(4)
            except(AttributeError, KeyError):
                pass 
            time.sleep(0.5)

    except(KeyboardInterrupt, SystemExit):
        print "\nKilling Thread.."
        gpsp.running = False 
        gpsp.join()
        status("red")

    print "Done.\nExiting." 

#!/bin/bash
# Run this as part of the boot sequence.  On my pi zero, the gpsd 
# would not work so I stopped it and started my own instance with
# USB0 
# @reboot for the root crontab works well to start this script
sleep 20
while true; do
    if ! pidof python | grep gps.py >/dev/null; then
        sudo service gpsd stop
	sleep 10
        sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock
	sleep 10
	su -c ~pi/gps.py pi
   fi
   sleep 10
done &



#!/bin/bash
# Run this as part of the boot sequence.  On my pi zero, the gpsd 
# would not work so I stopped it and started my own instance with
# USB0 
# @reboot for the root crontab works well to start this scriptsu
su -c "touch /tmp/gpsstatus" pi
su -c "touch /tmp/temperaturestatus" pi
su -c "touch /tmp/camerastatus" pi
while true; do
    sleep 20
    if ! pidof python | grep gps.py >/dev/null; then
	echo "stopping gpsd service"
        sudo service gpsd stop
	sleep 10
	echo "starting our own gpsd"
        # sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock &
	sudo gpsd /dev/ttyACM0 -n -F /var/run/gpsd.sock &
	sleep 10
	echo "trying cgps"
	# cgps >> /dev/null &
	cgps -s
	sleep 30
	killall cgps
	echo "starting the logger..."
	su -c ~pi/gpstracker.py pi
   fi
done &



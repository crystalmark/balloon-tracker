#!/bin/bash
counter=0
while [ 1 ]
do
  gpspipe -r -n 1000 -o /home/pi/gps.nmea
  gzip /home/pi/gps.nmea
  mv /home/pi/gps.nmea.gz /home/pi/gps.nmea.$counter.gz
  let counter=counter+1
done

#!/bin/bash

if [ -z "$1" ]; then
	echo "Useage tracker.sh [FEED_ID]"
	exit -1
fi
FEED_ID=$1

LATEST=/tmp/latest.xml
COORDS=/tmp/coordinates.csv
KML=/tmp/balloon.kml

wget -q https://api.findmespot.com/spot-main-web/consumer/rest-api/2.0/public/feed/$FEED_ID/latest.xml -O $LATEST
lat=$(grep -oPm1 "(?<=<latitude>)[^<]+" $LATEST)
long=$(grep -oPm1 "(?<=<longitude>)[^<]+" $LATEST)
cat head.kml > $KML
cat placemark.kml >> $KML
cat coordinates.kml >> $KML
sed -i "s/{latitude}/$lat/g" $KML
sed -i "s/{longitude}/$long/g" $KML
coord="$lat,$long,0"
touch $COORDS
if grep -q $coord $COORDS; then
	echo "$coord already logged.  No status update received."
else
	echo $coord >> $COORDS
fi
cat $COORDS >> $KML
cat tail.kml >> $KML

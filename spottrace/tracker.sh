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
cat head.kml > $COORDS
cat placemark.kml >> $COORDS
cat coordinates.kml >> $COORDS
sed -i "s/{latitude}/$lat/g" $COORDS
sed -i "s/{longitude}/$long/g" $COORDS
coord="$lat,$long,0"
touch $COORDS
if grep -q $coord $COORDS; then
	echo "$coord already logged.  No status update received."
else
	echo $coord >> $COORDS
fi
cat $COORDS >> $KML
cat tail.kml >> $KML

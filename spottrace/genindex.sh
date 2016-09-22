#!/bin/bash
if [ -z "$1" ]; then
	echo "Useage tracker.sh [FEED_ID] [WEBROOT]"
	exit -1
fi
FEED_ID=$1
WEBROOT=$2

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd $DIR

./tracker.sh $FEED_ID

if [ $? -eq 0 ]; then
	cp /tmp/balloon.kml $WEBROOT/
	sed "s/{rev}/`date +%s`/" index.html.template > $WEBROOT/index.html
fi

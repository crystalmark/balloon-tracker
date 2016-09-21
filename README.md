# Balloon Tracker

Scripts and templates to make a balloon and chase-car tracking web page.

One can be tracked using the Spot Trace API, the other using a Raspberry Pi with GPS receiver and internet connection.

## Hardware

### SPOT Trace
SPOT Trace GPS tracker with satellite phone communications.  This is about the best hardware for tracking a high alititude balloon since it can send location details back to us on the ground, even when out of range of ground based mobile networks.  There is an alititude limit of around 7000m so a flight computer is required if you would like to record the balloon position any higher.

### Flight computer
Simply used for recording the location but without trasmission to the ground.  This design can be enhanced to use low power short wave radio to communicate home but that's beyond this project... so far.

### Chase Car computer 
A raspberry pi with GPS receiver, running a bash script via cron which connects to the web server via ssh to transmit it's location.

## Software

The web page is nothing fancy, simple an HTML page that displays a Google Map which in turn loads KML files.

## Set-up
### SPOT Tracker
Get the FEED_ID from the findmespot.eu website by creating a new share feed:
https://login.findmespot.com/spot-main-web/myaccount/share/list.html
The FEED_ID is the glId parameter that appears in the feed details URL.

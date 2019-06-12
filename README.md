# Connection-Alerter
Script that pings Google DNS server and plays a sound on a re-established connection.

Essentially can be build into a IoT device that plays a beep or sound when the connection is down. For example:

1:00pm - Internet Goes Doesn
1:00pm - IoT Device Beeps alerting people there is an issue with the internet. Makes troubleshooting easier as we only need to focus on the internet or any devices that preceed the IoT device. 
1:10pm - Internet is reconnected. Device stops beeping or plays a file: "Internet Connected"

This device could also alert of high packet loss. 

It should be able to run on any IoT device but if it were to be used in the above example I would recommend a direct connection to the router via ethernet cable. 

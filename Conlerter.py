#print("Sub Routine Application") Monitors the network connection and plays a sound if the connection goes down

#    Conlerter version 1, Copyright (C) 2015 Stephen Jack Henry
#    Conlerter comes with ABSOLUTELY NO WARRANTY.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; type `show c' for details.

import os
import subprocess
import winsound
import time

def NetFail():
    winsound.Beep(2000 , 180), winsound.Beep(1400 , 180)

def NetSucc():
    winsound.Beep(1400 , 250), winsound.Beep(2000 , 250), winsound.Beep(3600 , 280)

ips=[]
n = 1
x = '8.8.8.8'
ips.append(x)
for ping in range(0,n):
    ipd=ips[ping]
res = subprocess.call(['ping', '-n', '1', ipd]) # I need to code this so it does a continuous ping and when it goes out for more then 20 seconds it plays a soun0d

# http://www.python-course.eu/python3_loops.php
# https://www.google.co.uk/search?q=if+statement+when+loop+has+executed+a+number+of+times&oq=if+statement+when+loop+has+executed+a+number+of+times&aqs=chrome..69i57.31087j0j4&sourceid=chrome&es_sm=122&ie=UTF-8#q=if+statement+while+loop+has+executed+a+number+of+times+python

#res = subprocess.call(['ping', '-n', '4', ipd])
#if ipd in str(res):
#    print ("ping to", ipd, "OK") # I need to code it so if it's 10 seconds of stable pings again it will play a connection sound
#elif "failure" in str(res):
#    print ("ping to", ipd, "recieved no responce", NetFail())
#else:
#    print ("ping to", ipd, "failed!", NetFail())



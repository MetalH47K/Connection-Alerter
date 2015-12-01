# ("Sub Routine Application") Monitors the network connection and plays a sound if the connection goes down

#### WORK IN PROGRESS ####

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
NetSuccess = 10
NetFailure = 10
PinSuc = 0
PinFail = 0
x = '8.8.8.8'
ips.append(x)
for ping in range(0,n):
    ipd=ips[ping]

def PingFailure():
    while PinFail < NetSuccess:
        res = subprocess.call(['ping', '-n', '10', ipd])
    if ipd in str(res):
        PingSuccess()
    else:
        print ("ping to", ipd, "failed!"), NetFail()

def PingSuccess():
    while PinFail < NetFailure: # This needs to be cleaned up so it doesn't interfere with the other function
        res = subprocess.call(['ping', '-n', '10', ipd])
    if ipd in str(res):
        PingFail()
    else:
        print ("ping to", ipd, "successful!"), NetSucc()

# I've defined the main looping fuctions. 

print('Starting Monitor'); PingSuccess()

# So it runs the main loop until the connection fails: It plays a sound and runs the second loop until the connection is
# restablished, plays a sound and it switches back to the other loop. I only want it to play the sound when switching 
# to the other loop



    #except "failure" in str(res):
    #    print('Conection Stable', NetSucc())
    #    PinSuc += 1

#if ipd in str(res):
#    print ("ping to", ipd, "OK") # I need to code it so if it's 10 seconds of stable pings again it will play a connection sound
#elif "failure" in str(res):
#    print ("ping to", ipd, "recieved no responce", NetFail())
#else:
#    print ("ping to", ipd, "failed!", NetFail())
#except "failure" in str(res):



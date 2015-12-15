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

class Sound():
    def NetFail():
        winsound.Beep(2000 , 180), winsound.Beep(1400 , 180)
    def NetSucc():
        winsound.Beep(1400 , 250), winsound.Beep(2000 , 250), winsound.Beep(3600 , 280)


ips = [] # I think this code is used to create a variable of an IP address?
x = '8.8.8.8'
ips.append(x)
for ping in range(0,1):
    ipd = ips[ping]


class IP(object):
    UNABLE = "failed"   # word indicating unreachable host #CHANGE MADE FROM UNABLE TO CODE
    MAX = 15            # number of success/failure to record new state
    def __init__(self, ip, failfunc, succfunc, initial = True):
        self.ip = ip
        self.failfunc = failfunc  # to warn of a disconnection
        self.succfunc = succfunc  # to warn of a connection
        self.connected = initial  # start by default in connected state
        self.curr = 0             # number of successive alternate states
    def test(self):
        p = subprocess.Popen([ 'ping', '-n', '1', self],
                     stdout = subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if self.UNABLE in out: # CHANGE MADE FROM UNABLE TO CODE
            if self.connected:
                self.curr += 1
            else:
                self.curr = 0   # reset count
        else:
            if not self.connected:
                self.curr += 1
            else:
                self.curr = 0   # reset count
        if self.curr >= self.MAX:     # state has changed
            self.connected = not self.connected
            self.curr = 0
            if self.connected:        # warn for new state
                self.succfunc(self)
            else:
                self.failfunc(self)


# MAIN PROGRAM

IP.test(ipd)


# NOTES

# I have a basic understanding of CLASS and I am still trying to wrap my head around __int__ and self declarations. In the context
# of this application I am unable to figure out why the code is throwing an error about a STR not being an attibute. 
# I have made a small CLASS at the top to practice turning the two sound functions I had into a CLASS. It doesn't seem I need to 
# but it's about learning it more so than practibility at the moment. 


# TEST & OLD CODE BELOW

# Sound.NetFail()
# Sound.NetSucc()

#def PingFailure():
#    while PinFail < NetSuccess:
#        res = subprocess.call(['ping', '-n', '10', ipd])
#    if ipd in str(res):
#        PingSuccess()
#    else:
#        print ("ping to", ipd, "failed!"), NetFail()

#def PingSuccess():
#    while PinFail < NetFailure: # This needs to be cleaned up so it doesn't interfere with the other function
#        res = subprocess.call(['ping', '-n', '10', ipd])
#    if ipd in str(res):
#        PingFail()
#    else:
#        print ("ping to", ipd, "successful!"), NetSucc()

## I've defined the main looping fuctions. 

#print('Starting Monitor'); PingSuccess()

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



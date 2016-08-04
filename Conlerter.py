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

class ConSound():
    def NetFail():
        winsound.Beep(2000 , 180), winsound.Beep(1400 , 180)
    def NetSucc():
        winsound.Beep(1400 , 250), winsound.Beep(2000 , 250), winsound.Beep(3600 , 280)

IPAddress = "8.8.8.8"

class IP(object):
    StateChangeRate = 15
    def __init__(self, ip, failfunc, succfunc, initial = True):
        self.ip = ip
        self.failfunc = ConSound.NetFail()
        self.succfunc = ConSound.NetSucc()
        self.connected = initial
        self.curr = 0
    def PingTest(self):
        FailedPing = "Request timed out"
        p = subprocess.Popen(['ping', '-n', '1', self],
            stdout = subprocess.PIPE, stderr=subprocess.PIPE)
        out,err = p.communicate()
        if FailedPing.encode('utf-8') in out:
            if self.connected:
                self.curr += 1
                print(curr)  ### TESTING
            else:
                self.curr = 0
        else:
            if not self.connected: ### Errors out Here
                self.curr += 1
            else:
                self.curr = 0
        if self.curr >= self.StateChangeRate:
            self.connected = not self.connected
            self.curr = 0
            if self.connected:
                self.succfunc(self)
            else:
                self.failfunc(self)




		

### Need to create two states... On and Off (True and False)
### Then do a ping test and if its up for 15 pings or down for 15 pings change the state from the other
### And then play a sound. 
		
		
		
# MAIN PROGRAM

IP.PingTest(IPAddress)

UnableToFindHost = "Ping request could not find host"
UnreachablePing = "Destination Host Unreachable"
PingR = PingReply
PingF = FailedPing
PingH = UnableToFindHost
PingU = UnreachablePing
SCN = StateChangeNumber            # number of success/failure pings to record new state
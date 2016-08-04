# ("Sub Routine Application") Monitors the network connection and plays a sound if the connection goes down

#### WORK IN PROGRESS ####

#    Conlerter version 1, Copyright (C) 2015 Stephen Jack Henry
#    Conlerter comes with ABSOLUTELY NO WARRANTY.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; type `show c' for details.

# NOTES

# I have a basic understanding of CLASS and I am still trying to wrap my head around __int__ and self declarations. In the context
# of this application I am unable to figure out why the code is throwing an error about a STR not being an attibute. 
# I have made a small CLASS at the top to practice turning the two sound functions I had into a CLASS. It doesn't seem I need to 
# but it's about learning it more so than practibility at the moment. 

import os
import subprocess
import winsound
import time

class ConSound():
    def NetFail():
        winsound.Beep(2000 , 180), winsound.Beep(1400 , 180)
    def NetSucc():
        winsound.Beep(1400 , 250), winsound.Beep(2000 , 250), winsound.Beep(3600 , 280)


#IPS = [] #Create List
#x = '8.8.8.8' #Add IP Address
#ips.append(x) #Add x to list
#for ping in range(0,1): 
#    ipd = ips[ping]

IPAddress = "8.8.8.8"

class IP(object):
	#Below are the varibles
	StateChangeNumber = 15            # number of success/failure pings to record new state
	PingReply = "Reply from"
	FailedPing = "Request timed out"   # word indicating unreachable host 
	UnableToFindHost = "Ping request could not find host"
	UnreachablePing = "Destination Host Unreachable"
	###
	#Below is the code efficient abreviations of the above. 
	###
    PingR = PingReply
	PingF = FailedPing
	PingH = UnableToFindHost
	PingU = UnreachablePing
	SCN = StateChangeNumber            # number of success/failure pings to record new state
    def __init__(self, ip, failfunc, succfunc, initial = True):
        self.ip = ip
        self.failfunc = failfunc  # to warn of a disconnection
        self.succfunc = succfunc  # to warn of a connection
        self.connected = initial  # start by default in connected state
        self.curr = 0             # number of successive alternate states
    def PingTest(self):
        p = subprocess.Popen(['ping', '-n', '1', self],
                     stdout = subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if PingF in stdout: #Command in question This needs to be reviewed. 
            if self.connected:
                self.curr += 1
            else:
                self.curr = 0   # reset count
        else:
            if not self.connected:
                self.curr += 1
            else:
                self.curr = 0   # reset count
        if self.curr >= self.SCN:     # state has changed
            self.connected = not self.connected
            self.curr = 0
            if self.connected:        # warn for new state
                self.succfunc(self)
            else:
                self.failfunc(self)
	def EmailState(): #TEST CLASS FUNCTION
		print("Email Addres not found in database")
		

### Need to create two states... On and Off (True and False)
### Then do a ping test and if its up for 15 pings or down for 15 pings change the state from the other
### And then play a sound. 
		
		
		
# MAIN PROGRAM

IP.PingTest(IPAddress)

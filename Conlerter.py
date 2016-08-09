# ("Sub Routine Application") Monitors the network connection and plays a sound if the connection goes down

#### WORK IN PROGRESS ####

#    Conlerter version 1, Copyright (C) 2015 Stephen Jack Henry
#    Conlerter comes with ABSOLUTELY NO WARRANTY.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; type `show c' for details.


import subprocess
import winsound

class ConSound():
    def NetFail():
        winsound.Beep(2000 , 180), winsound.Beep(1400 , 180)
    def NetSucc():
        winsound.Beep(1400 , 250), winsound.Beep(2000 , 250), winsound.Beep(3600 , 280)

IPAddress = "8.8.8.8"

class IP(object):
    def __init__(self, ip, failfunc, succfunc, initial = True):
        self.ip = ip
        self.failfunc = ConSound.NetFail()
        self.succfunc = ConSound.NetSucc()
        self.connected = initial
        switch = 0
    def PingTest(self):
        FailPing = 0
        StateChangeRate = 5
        FailedPing = "Request timed out"
        ElseTestPing = 0 #####
        SuccessfulPing = 0
        loop = 0
        Switch = 0
        while loop < 1:
            p = subprocess.Popen(['ping', '-n', '1', self], #CMD eqiv: C:\>ping -n 1 IPAddress 
                stdout = subprocess.PIPE, stderr=subprocess.PIPE)
            out,err = p.communicate()
            if FailedPing.encode('utf-8') in out:
                if FailPing >= StateChangeRate:
                    ConSound.NetFail()
                    FailPing += 1
                    Switch = 1
                    print('STATE CHANGE')
                else:
                    ElseTestPing += 1     
                    print('Ping Null Land', ElseTestPing) #Seems to be redirecting here even on a successful ping which means there is an error with the IF statment
            else:
                print('Ping Successful REDIRECTED FROM FIRST IF STATEMENT')
            if Switch == 1:
                if SuccessfulPing >= StateChangeRate:
                    ConSound.NetSucc()
                    SuccessfulPing += 1
                    Switch = 0
                    print('STATE CHANGE')
                else:
                    ElseTestPing += 1     
                    print('Ping Null Land', ElseTestPing) 
            else:
                print('Pinging Again:')
                print(' ')


IP.PingTest(IPAddress)

		

### Need to create two states... On and Off (True and False)
### Then do a ping test and if its up for 15 pings or down for 15 pings change the state from the other
### And then play a sound. 
		
		
		
# MAIN PROGRAM

#Junk

#UnableToFindHost = "Ping request could not find host"
#UnreachablePing = "Destination Host Unreachable"
#PingR = PingReply
#PingF = FailedPing
#PingH = UnableToFindHost
#PingU = UnreachablePing
#SCN = StateChangeNumber            # number of success/failure pings to record new state
print("Hello World")

import os
import subprocess
import winsound
import time

winsound.Beep(2000 , 180), winsound.Beep(1400 , 180)

ips=[]
n = 1
x = '8.8.8.8'
ips.append(x)
for ping in range(0,n):
    ipd=ips[ping]
res = subprocess.call(['ping', '-n', '1', ipd]) # I need to code this so it does a continuous ping and when it goes out for more then 20 seconds it plays a sound
if ipd in str(res):
    print ("ping to", ipd, "OK") # I need to code it so if it's 10 seconds of stable pings again it will play a connection sound
elif "failure" in str(res):
    print ("ping to", ipd, "recieved no responce")
else:
    print ("ping to", ipd, "failed!")

winsound.Beep(1400 , 250), winsound.Beep(2000 , 250), winsound.Beep(3600 , 280)
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



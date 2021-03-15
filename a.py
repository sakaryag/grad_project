#!/usr/bin/python

import time
import threading

# Define a function for the thread
def print_time(i  ):
   count = 0
   print (i,time.ctime(time.time()) )

# Create two threads as follows
try:

    for i in range(3):
        robot = threading.Thread(target=print_time,args=(i,))
        robot.start()


except:
   print ("Error: unable to start thread")

#!/usr/bin/env python2
import serial
from time import sleep
import os

i = 0
rcv = ""

ser = serial.Serial(
              
   port="/dev/ttyAMA0",
   baudrate = 115200,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1)

while True:
	#rcv = ser.read()
	#print rcv
	ser.write('\nCounter: %d' %(i))
	i = i+1
	# ser.write(b'hehe')
	#ser.flush()
	sleep(1)
# except KeyboardInterrupt:
	# ser.close()
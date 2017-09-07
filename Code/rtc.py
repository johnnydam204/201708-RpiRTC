import RPi.GPIO as GPIO
import time
import datetime
import serial
import os

SCLK = 17
SLCH = 18
SDI	 = 27
LED  = 22

ledCode = [0xc0,0xf9,0xa4,0xb0,0x99,0x92,0x82,0xf8,0x80,0x90]
counter = 0

# Khai bao bien thoi gian
Hour = 0
Minute = 0
Second  = 0
Day = 0
Weekday = 0
Month = 0
Year = 0


GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(SCLK, GPIO.OUT)
GPIO.setup(SLCH, GPIO.OUT)
GPIO.setup(SDI, GPIO.OUT)
GPIO.setup(LED, GPIO.OUT)

GPIO.output(SCLK,GPIO.LOW)
GPIO.output(SLCH,GPIO.LOW)
GPIO.output(SDI,GPIO.LOW)

def shiftingOut(sdata = 0):
	i = 0
	buffer = 0
	temp = 0
	for i in range(0,8):
		buffer = sdata
		sdata = sdata << 1
		temp = buffer & 0x80				
		if(temp == 0):
			GPIO.output(SDI,GPIO.LOW)
		else:
			GPIO.output(SDI,GPIO.HIGH)

		GPIO.output(SCLK,GPIO.HIGH)
		time.sleep(0.001)
		GPIO.output(SCLK,GPIO.LOW)
		
	return
		
def shiftingLatch():
	GPIO.output(SLCH,GPIO.HIGH)
	time.sleep(0.001)
	GPIO.output(SLCH,GPIO.LOW)
	return
	
def displayTime():
	# shiftingOut(ledCode[((Year%1000)%100)%10])
	# shiftingOut(ledCode[((Year%1000)%100)/10])
	# shiftingOut(ledCode[(Year%1000)/100])
	# shiftingOut(ledCode[Year/1000])
	
	# shiftingOut(ledCode[Month%10])
	# shiftingOut(ledCode[Month/10])

	# shiftingOut(ledCode[Day%10])
	# shiftingOut(ledCode[Day/10])	
	
	shiftingOut(ledCode[Second%10])
	shiftingOut(ledCode[Second/10])
	
	shiftingOut(ledCode[Minute%10])
	shiftingOut(ledCode[Minute/10])
	
	# shiftingOut(ledCode[Hour%10])
	# shiftingOut(ledCode[Hour/10])
	
	shiftingLatch()
	return
	
# ser = serial.Serial(
              
   # port="/dev/ttyAMA0",
   # baudrate = 115200,
   # parity=serial.PARITY_NONE,
   # stopbits=serial.STOPBITS_ONE,
   # bytesize=serial.EIGHTBITS,
   # timeout=3.0)
# time.sleep(2)

while True:
	# Doc thoi gian
	MyDateTime = datetime.datetime.now()

	#Tach thoi gian
	Hour = MyDateTime.hour
	Minute = MyDateTime.minute
	Second = MyDateTime.second
	Day = MyDateTime.day   			#Day of month
	Weekday = MyDateTime.weekday()	#Day of week
	Month = MyDateTime.month
	Year = MyDateTime.year
	
	# Hien thi thoi gian
	displayTime()
	# myPort.write("\r\nTime:" + Hour)    
	time.sleep(0.1)
	
	#ser.write("\n\rWrite counter: %d" %(counter))
	#ser.write("\n\rXin chao")
	#counter += 1
	#time.sleep(1)
	
	# ser.write("\r\nSay something:")
    # rcv = ser.read()
    # ser.write("\r\nYou sent:" + repr(rcv))
	

	
	


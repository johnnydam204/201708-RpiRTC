try:
	import RPi.GPIO as GPIO
	import time
	import datetime
	import serial
	import os

	SLCH = 27
	SCLK = 17
	SDI	 = 18
	LED  = 22

	playSong = "omxplayer -o local /home/pi/Desktop/RealtimeClock/1.mp3 &"

	#ledCode = [0xc0,0xf9,0xa4,0xb0,0x99,0x92,0x82,0xf8,0x80,0x90]
	ledBigCode = [0xF3,0xC0,0xB5,0xE5,0xC6,0x67,0x77,0xC1,0xF7,0xE7,0x00,0x9F,0xCF,0x6F,0x1F,0xCE,0xFA,0x3F,0x3B,0x1E,0x04]
	#              0  , 1  , 2  , 3  , 4  , 5  , 6  , 7  , 8  , 9  ,    , P  , A  , S  , F  , H  , U  , E  , C  , T  ,  -

	ledSmallCode = [0x0C,0x3F,0x4A,0x1A,0x39,0x98,0x88,0x3E,0x08,0x18]
	#                0  , 1  , 2  , 3  , 4  , 5  , 6  , 7  , 8  , 9

	# Khai bao bien thoi gian
	Hour = 0
	Minute = 0
	Second  = 0
	Day = 0
	Weekday = 0
	Month = 9
	Year = 2017

	# =============== Xu ly doc file cai dat thoi gian ===============
	file = open("/home/pi/Public/ThietLapThoiGianChayNhac.txt","r")

	fileData = file.read()
	#print fileData

	# Chuyen ky tu xuong dong "\n" thanh ":" truoc khi tach
	fileData = fileData.replace("\n",":")
	#print fileData

	# Tach gia tri luu tru thoi gian
	strTime = fileData.split(':')
	#print strTime
	#print len(strTime)

	# Chuyen doi tu lmang ky tu sang mang so nguyen
	arrTime = [int(strNumber) for strNumber in strTime]              
	#print arrTime 

	# Tach mang cai dat gio, phut, giay
	hrsSet = [0]*20  #Mang chua gio,  gom 20 phan tu, gia tri khoi tao la 0
	minSet = [0]*20  #Mang chua phut, gom 20 phan tu, gia tri khoi tao la 0
	secSet = [0]*20  #Mang chua giay, gom 20 phan tu, gia tri khoi tao la 0

	for i in range(0,20):               
		hrsSet[i] = arrTime[i*3 +0]
		minSet[i] = arrTime[i*3 +1]
		secSet[i] = arrTime[i*3 +2]
	#print hrsSet
	#print minSet
	#print secSet

	# ======================= Thiet lap GPIO ==========================
	#GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(SCLK, GPIO.OUT)
	GPIO.setup(SLCH, GPIO.OUT)
	GPIO.setup(SDI, GPIO.OUT)
	GPIO.setup(LED, GPIO.OUT)

	GPIO.output(SCLK,GPIO.LOW)
	GPIO.output(SLCH,GPIO.LOW)
	GPIO.output(SDI,GPIO.LOW)

	# =================== Xay dung ham con dieu khien LED ==============
	def shiftingOut(sdata = 0):
		i = 0
		buffer = 0
		temp = 0
		for i in range(0,8):
			buffer = sdata
			sdata = sdata << 1
			temp = buffer & 0x80				
			if(temp):
				GPIO.output(SDI,GPIO.HIGH)
			else:
				GPIO.output(SDI,GPIO.LOW)

			GPIO.output(SCLK,GPIO.HIGH)
			time.sleep(0.0001)
			GPIO.output(SCLK,GPIO.LOW)
		return
			
	def shiftingLatch():		
		GPIO.output(SLCH,GPIO.HIGH)
		time.sleep(0.0001)
		GPIO.output(SLCH,GPIO.LOW)
		return

	# Khai bao ham truyen du lieu xuong dong ho
	# def putOutLine(pos, led1, led2):
		# ledNumIndex[pos] = led2
		# ledNumIndex[pos +1] = led1
		# return
		
	def displayTime():		
		shiftingOut(ledSmallCode[(Year%100)%10])
		shiftingOut(ledSmallCode[(Year%100)/10])
		shiftingOut(ledSmallCode[(Year%1000)/100])
		shiftingOut(ledSmallCode[Year/1000])
		
		shiftingOut(ledSmallCode[Month%10])
		shiftingOut(ledSmallCode[Month/10])

		shiftingOut(ledSmallCode[Day%10])
		shiftingOut(ledSmallCode[Day/10])	
		
		# shiftingOut(ledSmallCode[Second%10])
		# shiftingOut(ledSmallCode[Second/10])
		
		shiftingOut(ledBigCode[Minute%10])
		if(Second % 2):
			shiftingOut(ledBigCode[Minute/10])
		else:
			shiftingOut(ledBigCode[Minute/10]|0x08)
		
		shiftingOut(ledBigCode[Hour%10])
		shiftingOut(ledBigCode[Hour/10])		

		shiftingLatch()
		return

	# =================== Cau hinh truyen thong Serial =================	
	# ser = serial.Serial(              
	   # port="/dev/ttyAMA0",
	   # baudrate = 115200,
	   # parity=serial.PARITY_NONE,
	   # stopbits=serial.STOPBITS_ONE,
	   # bytesize=serial.EIGHTBITS,
	   # timeout=3.0)
	# time.sleep(1)

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
		
		# Chay nhac
		for i in range(0,20): 
			if(Hour != 0):
				if (Hour == hrsSet[i] and Minute == minSet[i] and Second == secSet[i]):
					os.system(playSong)
		displayTime()
			
		#In ra ngay thang nam
		print("Date: %s/%s/%s" % (Day, Month,Year))

		# In ra Thu trong tuan
		#print("Weekday: %s" % (Weekday))
		if 		Weekday == 0: print 'Monday'
		elif	Weekday == 1: print 'Tuesday'
		elif	Weekday == 2: print 'Wednesdayday'
		elif	Weekday == 3: print 'Thursday'
		elif	Weekday == 4: print 'Friday'
		elif	Weekday == 5: print 'Saturday'
		elif	Weekday == 6: print 'Sunday'		

		# In ra thoi gian
		print("Time: %s:%s:%s" % (Hour, Minute,Second))		
		time.sleep(1)
		
except KeyboardInterrupt:
	GPIO.cleanup()


	

	
	


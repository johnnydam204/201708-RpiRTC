import time
import os

file = open ("D:\ReadTextFile\CaiDatThoiGian.txt","r")
fileData = file.read()
#print fileData

# Chuyển ký tự xuống dòng "\n" thành ":" trước khi tách
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

# Chạy nhạc
for i in range(0,20): 
    if (Hour == hrsSet[i] and Minute == minSet[i] and Second == secSet[i]):
        os.system(playSong)





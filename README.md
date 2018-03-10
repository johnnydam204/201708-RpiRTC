RpiClock - Digital Clock and Reminder
1. Burn Raspbian OS into microSD card using Etcher sofware
2. Disconnect and reconnect the microSD card
3. Creat ssh file in boot folder on Window Explorer
4. Plug the internet cable to LAN Port on Raspberry Pi
5. Scan the RPi's IP using Advanced IP Scanner 
6. Login RPi using PuTTY within the IP found in step 5 (user: pi, passwd: raspberry)
7. sudo raspi-config
	Boot Options -> B1 Desktop/CLI -> Console Autologin
	Localisation Options -> Change Timezone -> Asia -> Ho Chi Minh City
	Advanced Options 	-> A1 Expand Filesystem
						-> A4 Audio -> Force 3.5mm
	Finish -> Reboot
8. Re-login to RPi
9. 	sudo apt-get update
	sudo apt-get upgrade
	sudo install omxplayer #for mp3 player
10. Copy source code to RPi using sftp (Filezillar or WinSCP)
	/home/pi/Public
	/home/pi/RpiClock
11. Modify the CaiDatThoiGian.txt in Public folder to play music 
12. Run the Program (python script) at startup
	sudo nano /home/pi/.bashrc
	insert the code at the end of file:			
		echo DIGITAL CLOCK
		sudo python /home/pi/RpiClock/rtc.py
13. Reboot
	sudo reboot -n
14. (Optional: Install and config Samba to share folder between RPi and Window PC (copy in CaiDatThoiGian.txt))

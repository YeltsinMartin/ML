import time 

while 1:
	file = open('/sys/class/leds/beaglebone:green:usr3/brightness' , 'w')
	file.write('1')
	file.close()
	print "LED ON"
	time.sleep(0.5)
	
	file = open('/sys/class/leds/beaglebone:green:usr3/brightness', 'w')
	file.write('0')
	file.close()
	print "LED OFF"
	time.sleep(0.5)

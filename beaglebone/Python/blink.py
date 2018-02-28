import Adafruit_BBIO.GPIO as GPIO
import time
pin_list = ['P8_8','P8_10']

# setting output pin
for pin_name in pin_list:
	GPIO.setup(pin_name, GPIO.OUT)

# setting input pin

GPIO.setup("P8_13",GPIO.IN)

while 1:
	print (GPIO.input("P8_13"))
	GPIO.output("P8_8",GPIO.HIGH)
	GPIO.output("P8_10",GPIO.LOW)
	time.sleep(0.5)
	GPIO.output("P8_8",GPIO.LOW)
	GPIO.output("P8_10",GPIO.HIGH)
	time.sleep(0.5)


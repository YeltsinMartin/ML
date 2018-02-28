import Adafruit_BBIO.GPIO as GPIO
import time

# cleanup all the previous declared PINS
GPIO.cleanup()


# declare toggle function
def toggle_fun(channel):
	global toggle
	if (not toggle):
		GPIO.output(pin_list[0], GPIO.HIGH)
		GPIO.output(pin_list[1], GPIO.LOW)
		toggle = True
	elif(toggle):
		GPIO.output(pin_list[0], GPIO.LOW)
		GPIO.output(pin_list[1], GPIO.HIGH)
		toggle = False

pin_list = ['P8_8','P8_10']

# setting output pin
for pin_name in pin_list:
	GPIO.setup(pin_name, GPIO.OUT)


# setting input pin
GPIO.setup("P8_13",GPIO.IN)
toggle = False
GPIO.add_event_detect("P8_13", GPIO.RISING, callback=toggle_fun, bouncetime=50)


# never ending loop
while 1:
	pass


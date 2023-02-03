import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(18, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(16, GPIO.OUT, initial = GPIO.HIGH)
GPIO.output(16, GPIO.LOW)
time.sleep(2)
GPIO.output(16, GPIO.HIGH)




#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT) # 20-21 kimenetek
GPIO.setup(20, GPIO.OUT)

print "start"

drive=GPIO.PWM(21,50)
drive.start(7.5)
turn=GPIO.PWM(20,50)
turn.start(7.5)

turn.ChangeDutyCycle(7.5)

wait = 0.5

#test1()
print "test1() stopped" 

for speed in range(75,100):
	drive.ChangeDutyCycle(speed/10.0)
	print speed/10.0
	time.sleep(wait)
for speed in range(100,75,-1):
	drive.ChangeDutyCycle(speed/10.0)
	#turn.ChangeDutyCycle(speed/10.0 - 0.3)
	print speed/10.0
	time.sleep(wait)

drive.ChangeDutyCycle(7.5)
#turn.ChangeDutyCycle(7.5)
print "end of 1"

time.sleep(5)

for steer in range(75, 100):
	turn.ChangeDutyCycle(steer/10.0)
	print steer/10.0
	time.sleep(wait)
for steer in range(100, 75, -1):
	turn.ChangeDutyCycle(steer/10.0)
	print steer/10.0
	time.sleep(wait)

turn.ChangeDutyCycle(7.5)
print "end of 2"

time.sleep(5)

for speed in range(75,100):
	drive.ChangeDutyCycle(speed/10.0)
	print speed/10.0
	time.sleep(wait)
for speed in range(100,75,-1):
	drive.ChangeDutyCycle(speed/10.0)
	#turn.ChangeDutyCycle(speed/10.0 - 0.3)
	print speed/10.0
	time.sleep(wait)

drive.ChangeDutyCycle(7.5)
#turn.ChangeDutyCycle(7.5)
print "end of 3"

def test1():
	print "Start of test1()"

	time.sleep(5)
	drive.ChangeDutyCycle(8.5)
	turn.ChangeDutyCycle(7.5)

	#Forward(50)
	for i in range(0, 51):
		time.sleep(5)

	#Stop and turn
	drive.ChangeDutyCycle(7.5)
	turn.ChangeDutyCycle(9.0)

	for j in range(0, 31):
		time.sleep(5)
	turn.ChangeDutyCycle(7.5)

test1()
print "stop"
drive.stop()
turn.stop()
time.sleep(3)
print "cleanup"
GPIO.cleanup()
time.sleep(3)

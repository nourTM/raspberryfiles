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

def test1():
	print "Start of test1()"
	print "Go forward and sleep for 8sec"
	drive.ChangeDutyCycle(5.0)
	turn.ChangeDutyCycle(7.5)
	time.sleep(5)
	print "Stop and turn"	
	drive.ChangeDutyCycle(7.5)
	time.sleep(2)
	turn.ChangeDutyCycle(5.0)
	time.sleep(3)
	print "stop turning"
	turn.ChangeDutyCycle(7.5)

	print "end of test1()"

test1()
print "stop"
drive.stop()
turn.stop()
time.sleep(3)
print "cleanup"
GPIO.cleanup()
time.sleep(3)

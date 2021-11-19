from motor_c import Motor
from motor_speed import MotorSpeed, MotorTurn
import RPi.GPIO as GPIO
import time

def main():
	GPIO.setmode(GPIO.BCM)
	motor = Motor(GPIO)
	for times in range(1,3):
		# first move slow always!
		motor.Turn(MotorTurn.RIGHT_MAX, 2) # 190 degree
		motor.Turn(MotorTurn.RIGHT_MAX, 2) # 90 degree
		
		time.sleep(2)

	motor.StopMotor()
	GPIO.cleanup()

if __name__ == '__main__':
	main()
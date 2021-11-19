import time

class Motor:
	STAND_SPEED = 7.5
	FORWARD_SPEED_MAX = 40
	BACKWARD_SPEED_MAX = 100
	RIGHT_SPEED_MAX = 40
	LEFT_SPEED_MAX = 100
	def __init__(self, GPIO):
		GPIO.setup(21, GPIO.OUT) # 20-21 kimenetek
		GPIO.setup(20, GPIO.OUT)
		self.drive=GPIO.PWM(21,50) 
		self.drive.start(self.STAND_SPEED) 
		self.turn=GPIO.PWM(20,50)
		self.turn.start(self.STAND_SPEED)

	def Forward(self, speed, duration):
		self.drive.ChangeDutyCycle(self.STAND_SPEED)
		self.drive.ChangeDutyCycle(speed/10.0)
		time.sleep(duration)
		self.drive.ChangeDutyCycle(self.STAND_SPEED)

	def Turn(self, speed, duration):
		self.turn.ChangeDutyCycle(self.STAND_SPEED)
		self.turn.ChangeDutyCycle(speed/10.0)
		time.sleep(duration)
		self.turn.ChangeDutyCycle(self.STAND_SPEED)

	def ForwardTurnRight(self, speed, duration):
		self.turn.ChangeDutyCycle(self.STAND_SPEED)
		self.drive.ChangeDutyCycle(self.STAND_SPEED)
		self.turn.ChangeDutyCycle(self.RIGHT_SPEED_MAX/10.0)
		self.drive.ChangeDutyCycle(speed/10.0)
		time.sleep(duration)
		self.turn.ChangeDutyCycle(self.STAND_SPEED)		

	def TurnRight(self, duration):
		self.turn.ChangeDutyCycle(self.STAND_SPEED)
		self.turn.ChangeDutyCycle(self.RIGHT_SPEED_MAX/10.0)
		time.sleep(duration)
		self.turn.ChangeDutyCycle(self.STAND_SPEED)

	def ForwardTurnLeft(self, speed, duration):
		self.turn.ChangeDutyCycle(self.STAND_SPEED)
		self.drive.ChangeDutyCycle(self.STAND_SPEED)
		self.turn.ChangeDutyCycle(self.LEFT_SPEED_MAX/10.0)
		self.drive.ChangeDutyCycle(speed/10.0)
		time.sleep(duration)
		self.turn.ChangeDutyCycle(self.STAND_SPEED)

	def BackwardTurnLeft(self, speed, duration):
		self.turn.ChangeDutyCycle(self.STAND_SPEED)
		self.drive.ChangeDutyCycle(self.STAND_SPEED)
		self.turn.ChangeDutyCycle(self.LEFT_SPEED_MAX/10.0)
		self.drive.ChangeDutyCycle(speed/10.0)
		time.sleep(duration)
		self.turn.ChangeDutyCycle(self.STAND_SPEED)
		
	def TurnLeft(self, duration):
		self.turn.ChangeDutyCycle(self.STAND_SPEED)
		self.turn.ChangeDutyCycle(self.LEFT_SPEED_MAX/10.0)
		time.sleep(duration)
		self.turn.ChangeDutyCycle(self.STAND_SPEED)


	def StopMotor(self):
		self.drive.stop()
		self.turn.stop()
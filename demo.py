#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
#for the keyboard controls
import pygame
import time
import atexit
#the address on the steper HAT and making it an object
stepperHAT = Adafruit_MotorHAT(addr = 0x60)
#making the stepper an object based on address and steps/rev
stepper1 = stepperHAT.getStepper(200, 1)
stepper1.setSpeed(60)
#port 1 for steppers is m1 and m2 combined on the HAT the other two are port 2
#auto disables motors on shutdown
def turnOffMotors():
	stepperHAT.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	stepperHAT.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	stepperHAT.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	stepperHAT.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
atexit.register(turnOffMotors)
interval = 0.1
stepSpeed =100 
pygame.init()
screen = pygame.display.set_mode([400,400])
pygame.display.set_caption("Stepper controller")

def funcPygameKey(events):
	for event in events:
		if event.type == pygame.QUIT:
			print ('quit pygame')
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				print ('key w -single coil forward')
				print (stepSpeed)
				stepper1.step(stepSpeed, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)
			elif event.key == pygame.K_s:
				print ('key s -single coil backward')
				print (stepSpeed)
				stepper1.step(stepSpeed, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)
			elif event.key == pygame.K_q:
				print ('key q -Double coil forward')
				print (stepSpeed)
				stepper1.step(stepSpeed, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
			elif event.key == pygame.K_a:
				print ('key a -Double coil backward')
				print (stepSpeed)
				stepper1.step(stepSpeed, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)
			elif event.key == pygame.K_e:
				print ('key e -Interleaved coil forward')
				print (stepSpeed)
				stepper1.step(stepSpeed, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.INTERLEAVE)
			elif event.key == pygame.K_d:
				print ('key d -Interleaved coil backward')
				print (stepSpeed)
				stepper1.step(stepSpeed, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.INTERLEAVE)
			elif event.key == pygame.K_r:
				print ('key r -Microsteps forward')
				print (stepSpeed)
				stepper1.step(stepSpeed, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.MICROSTEP)
			elif event.key == pygame.K_f:
				print ('key f -Microsteps Backward')
				print (stepSpeed)
				stepper1.step(stepSpeed, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.MICROSTEP)
try:
	print ('Program running- use keyboard to test stepper')
	while True:
			funcPygameKey(pygame.event.get())

			time.sleep(interval)

except KeyboardInterrupt:

	print ('you choose to exit out of the keyboard controller')

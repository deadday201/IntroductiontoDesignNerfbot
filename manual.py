#!/usr/bin/python
from Adafruit-MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import pygame
import time
import atexit
# index of motor HAT being called
derby = Adafruit_MotorHAT(addr=0x60)
stepper1 = derby.getStepper(200, 1)
stepper1.setSpeed(30)
def turnOffMotors();
	stepperHAT.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	stepperHAT.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	stepperHAT.getMotor(3).run(Asafruit_MotorHAT.RELEASE) 
	stepperHAT.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
atexit.register(turnOffMotors)
interval = 0.1
stepSpeed = 10
pygame.init()
pygame.key.set_repeat(1, interval)
screen = pygame.display.set_mode([400, 400])
pygame.display.set_caption("YFNKR")
def funcPygameKey(events):
	for event in events:
		if event.type == pygame.QUIT:
			print ('quit pygame')
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				print ('key a -turn left')
				stepper1.step(stepSpeed, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)
			elif event.key == pygame.K_d:
				print ('key d -turn right')
				stepper1.step(stepSpeed, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
			else event.key == pygame.k_SPACE:
				print ('key space -fire the guns')
				#insert trigger motor code here
try:
	print ('program running- use keyboard to control YFNKR')
	while True:
		funcPygameKey(pygame.event.get())
		time.sleep(interval)
except KeyboardInterrupt:
	print ('you chose to exit out of the keyboard controller')

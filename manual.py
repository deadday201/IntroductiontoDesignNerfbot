#!/usr/bin/python
from Adafruit-MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import pygame
import time
import atexit
# index of motor HAT being called
derby = Adafruit_MotorHAT(addr=0x60) #(address) default 0x60
stepper1 = derby.getStepper(200, 1) #(steps per rev, port)
stepper1.setSpeed(30) #(rev per minute)
#TURN OFF
def turnOffMotors();
	derby.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	derby.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	derby.getMotor(3).run(Asafruit_MotorHAT.RELEASE) 
	derby.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
atexit.register(turnOffMotors)
#VARIABLES
#fastEngaged = True
interval = 0.1
stepSpeedFast = 10
stepSpeedSlow = 1
stepSpeed
pygame.init()
pygame.key.set_repeat(1, interval)
screen = pygame.display.set_mode([400, 400])
pygame.display.set_caption("YFNKR")
def funcPygameKey(events):
	for event in events:
		if event.type == pygame.QUIT:
			print ('quit pygame')
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				if stepSpeed == stepSpeedFast:
					stepSpeed = stepSpeedSlow
				else:
					stepSpeed = stepSpeedFast
				#if fastEngaged:
				#	fastEngaged = False
				#else:
				#	fastEngaged = True
			elif event.key == pygame.K_a:
				print('key a - turn ccw @ ' stepSpeed)
				stepper1.step(stepSpeed, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)
				#if fastEngaged:
				#	print ('key a -turn left fast')
				#	stepper1.step(stepSpeedFast, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)
				#else:
				#	print ('key a -turn left slow')
				#	stepper1.step(stepSpeedSlow, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)
			elif event.key == pygame.K_d:
				#if fastEngaged:
				#	print ('key d -turn right fast')
				#	stepper1.step(stepSpeedFast, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
				#else
				#	print ('key d -turn right slow')
				#	stepper1.step(stepSpeedSlow, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
				print ('key d - turn cw @ ' stepSpeed)
				stepper1.step(stepSpeed, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
			elif event.key == pygame.k_SPACE:
				print ('key space -fire the guns')
				#insert trigger motor code here
try:
	print ('program running- use keyboard to control YFNKR')
	while True:
		funcPygameKey(pygame.event.get())
		time.sleep(interval)
except KeyboardInterrupt:
	print ('you chose to exit out of the keyboard controller')

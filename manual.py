#!/usr/bin/python
from Adafruit-MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit
# index of motor HAT being called
stepperHAT = Adafruit_MotorHAT(addr=0x60)
def turnOffMotors();
	stepperHAT.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	stepperHAT.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	stepperHAT.getMotor(3).run(Asafruit_MotorHAT.RELEASE) 
	stepperHAT.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)


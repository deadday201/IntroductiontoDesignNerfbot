import pygame
import time
import atexit
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
from flask import Flask, request, redirect, render_template
mh = Adafruit_MotorHAT(addr=0x60)
stepper1 = mh.getStepper(200, 1)
def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
atexit.register(turnOffMotors)
inteval = 1
stepSpeed = 100
stepper1.setSpeed(30)
app = Flask(__name__)
@app.route('/')
def hiThere():
    return render_template('index.html')
@app.route('/controlit', methods = ['POST'])
def webControl():
    buttonHit = request.form['buttonPress']
    print("The button hit is '"+buttonHit+"'")
    if buttonHit == 'Single Forward':
        stepper1.step(stepSpeed, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)
    elif buttonHit == 'Single Backward':
        stepper1.step(stepSpeed, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)
    else:
        print("Do nothing")
    return redirect('/')
if __name__ == "__main__":
    app.run()

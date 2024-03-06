import RPi.GPIO as GPIO #General Purpose Input Output pins
import time

# Initiliaze GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

#Define GPIO pin connected to the servo
servo_pin = 18

# Set up the GPIO pin as output 
GPIO.setup.PWM(servo_pin, 50) # 50  Hz (20ms period)

# Start PWM with 0 duty cycle (servo at 0 degrees)
pwm.start(0)

pwm.stop()
GPIO.cleanup()

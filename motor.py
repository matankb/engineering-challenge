import RPi.GPIO as GPIO
from time import sleep

#set mode for identifying pins
GPIO.setmode(GPIO.BOARD)

#set constants for GPIO pin numbers
MOTOR_RIGHT = 11
MOTOR_LEFT = 12

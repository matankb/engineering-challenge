import RPi.GPIO as GPIO
from time import sleep

#set mode for identifying pins
GPIO.setmode(GPIO.BOARD)

#set constants for GPIO pin numbers
MOTOR_RIGHT = 16
MOTOR_LEFT = 18

while True:
  input = input('Direction:') #Will be subsituted for voice control
  if input == 'left':
    GPIO.output(MOTOR_LEFT, GPIO.HIGH)
    GPIO.output(MOTOR_RIGHT, GPIO.LOW)
  elif input == 'right':
    GPIO.output(MOTOR_RIGHT, GPIO.HIGH)
    GPIO.output(MOTOR_LEFT, GPIO.LOW)
  elif input == 'forward':
    GPIO.output(MOTOR_RIGHT, GPIO.HIGH)
    GPIO.output(MOTOR_LEFT, GPIO.HIGH)
  elif input == 'stop':
    #turns motors off
    GPIO.output(MOTOR_RIGHT, GPIO.LOW)
    GPIO.output(MOTOR_RIGHT, GPIO.LOW)
    GPIO.cleanup()
    break

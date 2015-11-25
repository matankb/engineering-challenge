import RPi.GPIO as GPIO
import speech_recognition as sr

#set mode for identifying pins
GPIO.setmode(GPIO.BOARD)

#set constants for GPIO pin numbers
MOTOR_RIGHT = 16
MOTOR_LEFT = 18

command = ''

while True:
  if command == 'left':
    print('Moving left...')
    GPIO.output(MOTOR_RIGHT, GPIO.HIGH)
    GPIO.output(MOTOR_LEFT, GPIO.LOW)
  elif command == 'right':
    print('Moving right...')
    GPIO.output(MOTOR_LEFT, GPIO.HIGH)
    GPIO.output(MOTOR_RIGHT, GPIO.LOW)
  elif command == 'forward':
    print('Moving forward...')
    GPIO.output(MOTOR_RIGHT, GPIO.HIGH)
    GPIO.output(MOTOR_LEFT, GPIO.HIGH)
  elif command == 'stop':
    print('Stopping motors..')
    #turns motors off
    GPIO.output(MOTOR_RIGHT, GPIO.LOW)
    GPIO.output(MOTOR_LEFT, GPIO.LOW)
    GPIO.cleanup()
    print('Motors stopped')
    break

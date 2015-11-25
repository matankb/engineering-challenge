import RPi.GPIO as GPIO
import speech_recognition as sr
from Queue import Queue

event_queue = Queue()

rec = sr.Recognizer()
mic = sr.Microphone()

def phrase_heard(rec, audio):
  try:
    event_queue.put(rec.recognize_google(audio))
  except sr.UnknownValueError:
    print('Error: could not recognize speech')
  except sr.RequestError as e:
    print('Error: could not complete request; {0}'.format(e))

#set mode for identifying pins
GPIO.setmode(GPIO.BOARD)

#set constants for GPIO pin numbers
MOTOR_RIGHT = 16
MOTOR_LEFT = 18

while True:
  command = event_queue.get()
  if not command == '':
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
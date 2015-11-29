import RPi.GPIO as GPIO
import speech_recognition as sr
from queue import Queue

event_queue = Queue()

rec = sr.Recognizer()
mic = sr.Microphone()

def phrase_heard(rec, audio):
  try:
    rec_google = rec.recognize_google(audio)
    commands = rec_google.split(' ')
    for command in commands:
        event_queue.put(command)
  except sr.UnknownValueError:
    print('Error: could not recognize speech')
  except sr.RequestError as e:
    print('Error: could not complete request; {0}'.format(e))

with mic as source:
  #calibrates for background noise
  rec.adjust_for_ambient_noise(source)

rec.listen_in_background(mic, phrase_heard)

#set mode for identifying pins
GPIO.setmode(GPIO.BOARD)

#set constants for GPIO pin numbers
MOTOR_RIGHT = 16
MOTOR_LEFT = 18

GPIO.setup(MOTOR_RIGHT, GPIO.OUT)
GPIO.setup(MOTOR_LEFT, GPIO.OUT)

while True:
  command = event_queue.get()

  if command == 'left':
    print('Moving left...')
    GPIO.output(MOTOR_RIGHT, GPIO.HIGH)
    GPIO.output(MOTOR_LEFT, GPIO.LOW)
  elif command == 'right':
    print('Moving right...')
    GPIO.output(MOTOR_LEFT, GPIO.HIGH)
    GPIO.output(MOTOR_RIGHT, GPIO.LOW)
  elif command == 'forward' or command == 'go':
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

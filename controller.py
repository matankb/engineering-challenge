from motor.py import Motor
import speech_recognition as sr
from queue import Queue
from time import sleep

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

motor_r = Motor(1, 2, 3) #THESE ARE PLACEHOLDERS
motor_l = Motor(4, 5, 6) #SO ARE THESE

while True:
  command = event_queue.get()

  if command == 'left':
    print('Moving left...')
    motor_r.forward()
    motor_l.back()
  elif command == 'right':
    print('Moving right...')
    motor_r.back()
    motor_l.forward()
  elif command == 'forward' or command == 'go':
    print('Moving forward...')
    motor_r.forward()
    motor_l.forward()
  elif command == 'stop':
    print('Stopping motors..')
    #turns motors off
    motor_r.stop()
    motor_l.stop()
    print('Motors stopped')

import io
import background_listener as bl
from queue import Queue
from time import sleep

event_queue = Queue()

DEBUG = True #set to true if debugging / developing

if DEBUG:
    from threading import Thread
    #this allows us to input via keyboard
    def input_cb():
        event_queue.put(input())
        input_cb()

    Thread(None, input_cb).start()

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

motor_r = io.Motor(1, 2, 3) #THESE ARE PLACEHOLDERS
motor_l = io.Motor(4, 5, 6) #SO ARE THESE

TURN_TIME = 3 #constant for amount of time (secs) cart takes to turn
COLL_REVERSE_TIME = 1

while True:
  command = event_queue.get()

  if command == 'left':
    print('Moving left...')
    motor_r.forward()
    motor_l.back()

    sleep(TURN_TIME)
    event.queue.put('stop')

  elif command == 'right':
    print('Moving right...')
    motor_r.back()
    motor_l.forward()

    sleep(TURN_TIME)
    event_queue.put('stop')

  elif command == 'forward' or command == 'go':
    print('Moving forward...')
    motor_r.forward()
    motor_l.forward()

  elif command == 'back' or command == 'reverse':
    print('Moving back...')
    motor_r.back()
    motor_l.back()

  elif command == 'stop':
    print('Stopping motors..')
    #turns motors off
    motor_r.stop()
    motor_l.stop()
    print('Motors stopped')

  elif command == '_collide_':
    print('Collided!')
    event_queue.put("back")
    sleep(COLL_REVERSE_TIME)
    event_queue.put("stop")

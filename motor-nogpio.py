import speech_recognition as sr
from queue import Queue

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

with mic as source:
  #calibrates for background noise
  rec.adjust_for_ambient_noise(source)

rec.listen_in_background(mic, phrase_heard)

while True:
  command = event_queue.get()

  if command == 'left':
    print('Moving left...')
  elif command == 'right':
    print('Moving right...')
  elif command == 'forward':
    print('Moving forward...')
  elif command == 'stop':
    print('Stopping motors..')
    print('Motors stopped')

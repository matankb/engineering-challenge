from Queue import Queue

event_queue = Queue()

class Event:
    def __init__(self, type, param):
        self.type = type
        self.param = param

def start(callback):

    while True:
      event = event_queue.get()
      callback(event.type, event.param)

def queue(type, param):
    event_queue.put(Event(type, param))

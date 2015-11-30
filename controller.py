DEBUG = True #set to true if debugging / developing

if DEBUG:
    from threading import Thread
    import dummy_io as io
else:
    import io

import background_listener as bl
from queue import Queue
from time import sleep
import event_loop


if DEBUG:
    #this allows us to input via keyboard
    def input_cb():
        event_loop.queue('user', input())
        input_cb()
    Thread(None, input_cb).start()



def sr_success(phrase):
    commands = phrase.split(' ')
    for command in commands:
        event_loop.queue('user', command)
def sr_failure(e):
    print(e)

bl.start_listening(sr_success, sr_failure)




motor_r = io.Motor(1, 2, 3) #THESE ARE PLACEHOLDERS
motor_l = io.Motor(4, 5, 6) #SO ARE THESE

TURN_TIME = 3 #constant for amount of time (secs) cart takes to turn
COLL_REVERSE_TIME = 1

def handle_event(event):
    if event.type == 'user':
        if event.param == 'left':
            print('Moving left...')
            motor_r.forward()
            motor_l.back()

            sleep(TURN_TIME)
            motor_r.stop()
            motor_l.stop()

        elif event.param == 'right':
            print('Moving right...')
            motor_r.back()
            motor_l.forward()

            sleep(TURN_TIME)
            motor_r.stop()
            motor_l.stop()

        elif event.param == 'forward' or event == 'go':
            print('Moving forward...')
            motor_r.forward()
            motor_l.forward()

        elif event.param == 'back' or event == 'reverse':
            print('Moving back...')
            motor_r.back()
            motor_l.back()

        elif event.param == 'stop':
            print('Stopping motors..')
            #turns motors off
            motor_r.stop()
            motor_l.stop()
            print('Motors stopped')

    elif event.type == 'internal':
        if event.param == 'collide':
            print('Collided!')
            motor_r.back()
            motor_l.back()
            sleep(COLL_REVERSE_TIME)
            motor_r.stop()
            motor_l.stop()

event_loop.start(handle_event)

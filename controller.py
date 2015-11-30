DEBUG = True #set to true if debugging / developing

if DEBUG:
    from threading import Thread
    from lib import dummy_io as io
else:
    from lib import io

from lib import background_listener as bl
from queue import Queue
from time import sleep
from lib import event_loop
from config import *


if DEBUG:
    #this allows us to input via keyboard
    def input_cb():
        event_loop.queue('user', input())
        input_cb()
    input_thread = Thread(None, input_cb)
    input_thread.daemon = True
    input_thread.start()



def sr_success(phrase):
    commands = phrase.split(' ')
    for command in commands:
        event_loop.queue('user', command)
def sr_failure(e):
    print(e)

bl.start_listening(sr_success, sr_failure)




motor_r = io.Motor(MOTORR_A, MOTORR_B, MOTORR_E)
motor_l = io.Motor(MOTORL_A, MOTORL_B, MOTORL_E)


def handle_event(type, param):
    if type == 'user':
        if param == 'left':
            print('Moving left...')
            motor_r.forward()
            motor_l.back()

            sleep(TURN_TIME)
            motor_r.stop()
            motor_l.stop()

        elif param == 'right':
            print('Moving right...')
            motor_r.back()
            motor_l.forward()

            sleep(TURN_TIME)
            motor_r.stop()
            motor_l.stop()

        elif param == 'forward' or param == 'go':
            print('Moving forward...')
            motor_r.forward()
            motor_l.forward()

        elif param == 'back' or param == 'reverse':
            print('Moving back...')
            motor_r.back()
            motor_l.back()

        elif param == 'stop':
            print('Stopping motors..')
            #turns motors off
            motor_r.stop()
            motor_l.stop()
            print('Motors stopped')

    elif type == 'internal':
        if param == 'collide':
            print('Collided!')
            motor_r.back()
            motor_l.back()

            sleep(COLL_REVERSE_TIME)
            motor_r.stop()
            motor_l.stop()

event_loop.start(handle_event)

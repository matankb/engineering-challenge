#import various libraries, mostly internal libraries found in lib/
import sys
from time import sleep
from queue import Queue
from lib import io
from lib import background_listener as bl
from lib import event_loop
from config import *


#handling speech recognition callbacks
def sr_success(phrase):
    #parse recognized string into individual commands
    commands = phrase.split(' ')
    #queue each command
    for command in commands:
        event_loop.queue('user', command)

def sr_failure(e):
    print(e)


#start listening in background
#returns function that will stop listening, which is stored in var
stop_listening = bl.start_listening(sr_success, sr_failure)

#collision detection and handling
def on_collide():
    event_loop.queue('internal', 'collide')

io.on_input(INPUT_COLLIDE, on_collide, io.RISING)

#define motors with io.Motor class, using constants in config.py
motor_r = io.Motor(MOTORR_A, MOTORR_B, MOTORR_E)
motor_l = io.Motor(MOTORL_A, MOTORL_B, MOTORL_E)


#handling for all events
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

            '''
                 -------------------------------------
                 MUSEUM OF PRESERVED COMMENTS PRESENTS


                     __________________________
                    |                           |
                    |                           |
                    |   ---------------------   |
                    |    #turns motors off      |
                    |   ---------------------   |
                    |                           |
                    |                           |
                    |___________________________|
                    |                           |
                    |    The Oldest Comment     |
                    |        Nov 25 2015        |
                    |___________________________|


            '''

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

        elif param == 'exit':
            print('Cleaning up...')
            motor_r.stop()
            motot_l.stop()
            io.cleanup()

            stop_listening()
            print('Exiting')
            sys.exit(0)

#start event loop
event_loop.start(handle_event)

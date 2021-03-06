import RPi.GPIO as GPIO

#set pin numbering mode
GPIO.setmode(GPIO.BOARD)

#io-related constants
RISING = GPIO.RISING
FALLING = GPIO.FALLING

#classes to represent actual GPIO pins + motors
class Pin:
    def __init__(self, num):
        self.num = num
        GPIO.setup(num, GPIO.OUT)

    def high(self):
        GPIO.output(self.num, GPIO.HIGH)

    def low(self):
        GPIO.output(self.num, GPIO.LOW)

#NOTE: Does motor belong here?
class Motor:
    def __init__(self, pin_a, pin_b, pin_e):
        self.pin_a = Pin(pin_a)
        self.pin_b = Pin(pin_b)
        self.pin_e = Pin(pin_e)

    def forward(self):
        self.pin_a.high()
        self.pin_b.low()
        self.pin_e.high()

    def back(self):
        self.pin_a.low()
        self.pin_b.high()
        self.pin_e.high()

    def stop(self):
        self.pin_e.low()

#facade for handling input on pins
def on_input(num, callback, type = RISING):
    GPIO.setup(num, GPIO.IN)

    GPIO.add_event_detect(num, type, callback)

def cleanup():
    GPIO.cleanup()

#dummy_io.py - a module for using IO without access to RPi.GPIO
RISING = GPIO.RISING
FALLING = GPIO.FALLING

class Pin:
    def __init__(self, num):
        self.num = num

    def high(self):
        self.num #useless expression, will break if not there

    def low(self):
        self.num

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

def on_input(num, callback, type = RISING):

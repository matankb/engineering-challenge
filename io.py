import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

class Pin:
    def __init__(self, num):
        self.num = num
        GPIO.setup(num, GPIO.OUT)

    def on(self):
        GPIO.output(self.num, GPIO.HIGH)

    def off(self):
        GPIO.output(self.num, GPIO.LOW)

class Motor:
    def __init__(self, pin_a, pin_b, pin_e):
        self.pin_a = Pin(pin_a)
        self.pin_b = Pin(pin_b)
        self.pin_e = Pin(pin_e)

    def forward(self):
        self.pin_a.on()
        self.pin_b.off()
        self.pin_e.on()

    def back(self):
        self.pin_a.off()
        self.pin_b.on()
        self.pin_e.on()

    def stop(self):
        self.pin_e.off()

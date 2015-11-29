import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

class Motor:
    def __init__(self, pin_a, pin_b, pin_e):
        self.pin_a = pin_a
        self.pin_b = pin_b
        self.pin_e = pin_e

        GPIO.setup(pin_a, GPIO.OUT)
        GPIO.setup(pin_b, GPIO.OUT)
        GPIO.setup(pin_e, GPIO.OUT)

    def forward(self):
        GPIO.output(self.pin_a, GPIO.HIGH)
        GPIO.output(self.pin_b, GPIO.LOW)
        GPIO.output(self.pin_e, GPIO.HIGH)

    def back(self):
        GPIO.output(self.pin_a, GPIO.LOW)
        GPIO.output(self.pin_b, GPIO.HIGH)
        GPIO.output(self.pin_e, GPIO.HIGH)

    def stop(self):
        GPIO.output(self.pin_e, GPIO.LOW)

from threading import Thread
import time
import RPi.GPIO as GPIO


class LedThread(Thread):
    red_led_pin = 7
    green_led_pin = 10

    def __init__(self, greenLED, redLED):
        super(LedThread, self).__init__()
        self._keepgoing = True
        self._speed_on = 1
        self._speed_off = 1
        self._led_color = self.green_led_pin
        self.red_led_pin = redLED
        self.green_led_pin = greenLED

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(greenLED, GPIO.OUT)
        GPIO.setup(redLED, GPIO.OUT)

    def run(self):
        while (self._keepgoing):
            GPIO.output(self._led_color, True)
            time.sleep(self._speed_on)
            print(self._led_color)
            GPIO.output(self._led_color, False)
            time.sleep(self._speed_off)

    def ready(self):
        if not self.is_alive():
            self.start()

        GPIO.output(self._led_color, False)
        self._led_color = self.green_led_pin
        self._speed_on = 1
        self._speed_off = 1

    def error(self):
        if not self.is_alive():
            self.start()

        GPIO.output(self._led_color, False)
        self._led_color = self.red_led_pin
        self._speed_on = 0.15
        self._speed_off = 0.15

    def wating(self):
        if not self.is_alive():
            self.start()

        GPIO.output(self._led_color, False)
        self._led_color = self.green_led_pin
        self._speed_on = 0.2
        self._speed_off = 0.2

    def success(self):
        if not self.is_alive():
            self.start()

        GPIO.output(self._led_color, False)
        self._led_color = self.green_led_pin
        self._speed_off = 0
        self._speed_on = 1

    def stop(self):
        self._keepgoing = False


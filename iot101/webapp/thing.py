import RPi.GPIO as GPIO

LED_PIN = 17
SWITCH_PIN = 27

class PiThing(object):
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED_PIN, GPIO.OUT) #led pini ayarlandi
        GPIO.setup(SWITCH_PIN, GPIO.IN) #Switch pini ayarlandi

    def read_switch(self):
        return GPIO.input(SWITCH_PIN)

    def set_led(self,value):
        GPIO.output(LED_PIN, value)

from subprocess import call
from signal import pause
from gpiozero import LED, Button

def print_thing():
    led = LED(18)
    button.when_pressed = led.on
    print ("button pressed")
    

button.when_pressed = print_thing
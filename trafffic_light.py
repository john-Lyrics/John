from gpiozero import TrafficLights
from time import sleep
from time import bazer 

lights = TrafficLights(2, 3, 4,11)

lights.green.on()

while True:
    sleep(10)
    lights.green.off()
    lights.amber.on()
    sleep(1)
    lights.amber.off()
    lights.red.on()
    sleep(10)
    lights.red.bazer.on()
    sleep(1)
    lights.amber.on()
    sleep(1)
    lights.green.on()
    lights.amber.off()
    lights.red.off()
    
from machine import Pin, Timer
import time

led = Pin("LED", Pin.OUT)

for i in range(0, 4):
    led.toggle()
    time.sleep(0.1)
    
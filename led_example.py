import machine
import time


led_pin = machine.Pin(5, machine.Pin.OUT)

lit = True
while True:
    led_pin.value(lit)
    time.sleep(1)
    lit = not lit
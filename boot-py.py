import machine
import time

led = machine.Pin(2,machine.Pin.OUT)


while True:
    led.value(1)
    time.sleep_ms(1000)
    led.value(0)
    time.sleep_ms(1000)


import ugit
ugit.pull_all()

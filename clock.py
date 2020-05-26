#!/usr/bin/env python3

import spidev
from time import sleep
from vfd import VFD
import datetime
import psutil

# Initiate the display
vfd = VFD(0,0)
displaySize = 20

print("<=== Clock v0.4 ===>")

vfd.setCursor(0, 0)
welcome = "<=== Clock v0.4 ===>"
vfd.text(welcome)
sleep(2)

print("<==== Starting Clock ====>")

def clock():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")

def cpu_state():
    cpu_temperature = psutil.sensors_temperatures()['cpu-thermal'][0].current
    return f'{int(psutil.cpu_freq().current)} MHz {round(cpu_temperature, 1)} °C'

try:
    vfd.home()
    while True:
        # Get data
        clock()
        cpu_state()

        # Display data
        vfd.home()
        vfd.text(clock().center(displaySize))
        vfd.setCursor(0, 1)
        vfd.text(cpu_state().center(displaySize))
        sleep(1)
finally:
    # Clear screen on exit
    vfd.clear()
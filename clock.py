#!/usr/bin/env python3

import spidev
from time import sleep
from vfd import VFD
import datetime
import psutil

# Initiate the display
vfd = VFD(0,0)
displaySize = 20

print("<=== Clock v0.3 ===>")

vfd.setCursor(0, 0)
welcome = "<=== Clock v0.3 ===>"
vfd.text(welcome)
sleep(2)

print("<==== Starting Clock ====>")

try:
    vfd.home()
    while True:
        # Constants to update every loop
        now = datetime.datetime.now()
        clock = (now.strftime("%H:%M:%S"))
        cpu_temperature = psutil.sensors_temperatures()['cpu-thermal'][0].current
        cpu_state = str(int(psutil.cpu_freq().current)) + " MHz" + " " + str(round(cpu_temperature, 1)) + "°C"

        # Display data
        vfd.text(clock.center(displaySize))
        vfd.setCursor(0, 1)
        vfd.text(cpu_state.center(displaySize))
        sleep(0.1)
        vfd.home()
finally:
    # Clear screen on exit
    vfd.clear()
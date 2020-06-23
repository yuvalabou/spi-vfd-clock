#!/usr/bin/env python3

import spidev
from time import sleep
from vfd import VFD, COLS
import datetime
import psutil

vfd = VFD(0, 0)
welcome = "Starting Clock"

def clock():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")

def cpu_state():
    cpu_temp = psutil.sensors_temperatures()['cpu-thermal'][0].current
    return f'{int(psutil.cpu_freq().current)} MHz {cpu_temp:.1f} C'

def main():
    
    print(welcome)
    vfd.home()
    vfd.text(welcome.center(COLS))
    sleep(3)

    try:
        while True:
            vfd.home()
            vfd.text(clock().center(COLS))
            vfd.setCursor(0, 1)
            vfd.text(cpu_state().center(COLS))
            sleep(0.5)

    except KeyboardInterrupt:
        print("Stopping..")
        vfd.clear()
        vfd.text("User interrupted".center(COLS))
        sleep(2)
        vfd.clear()
        print("Stopped")

    finally:
        vfd.clear()

if __name__ == "__main__":
    main()
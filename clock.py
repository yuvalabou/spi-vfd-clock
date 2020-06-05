#!/usr/bin/env python3

import spidev
from time import sleep
from vfd import VFD, COLS
import datetime
import psutil

# Initiate the display
vfd = VFD(0, 0)

print("<--- Clock v0.92 --->")

vfd.home()
welcome = "<--- Clock v0.92 --->"
vfd.text(welcome)
sleep(2)

print("Starting Clock")

def clock():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")

def cpu_state():
    cpu_temp = psutil.sensors_temperatures()['cpu-thermal'][0].current
    return f'{int(psutil.cpu_freq().current)} MHz {cpu_temp:.1f} C'

def get_bytes(t, iface='eth0'):
    with open('/sys/class/net/' + iface + '/statistics/' + t + '_bytes', 'r') as f:
        data = f.read();
        return int(data)

def net_speed():
    tx1 = get_bytes('tx')
    rx1 = get_bytes('rx')
    sleep(0.1)
    tx2 = get_bytes('tx')
    rx2 = get_bytes('rx')
    tx_speed = ((tx2 - tx1) / 1000000.0) * 10
    rx_speed = ((rx2 - rx1) / 1000000.0) * 10

    return f'TX:{tx_speed:.3f} RX:{rx_speed:.3f}'

try:
    while True:
        vfd.home()
        vfd.text(clock().center(COLS))
        vfd.setCursor(0, 1)
        vfd.text(cpu_state().center(COLS))
        vfd.setCursor(0, 2)
        vfd.text(net_speed().center(COLS))
        sleep(0.5)

except KeyboardInterrupt:
    print("Stopping..")
    vfd.clear()
    vfd.text("User interrupted".center(COLS))
    sleep(3)
    vfd.clear()
    print("Stopped")

finally:
    vfd.clear()
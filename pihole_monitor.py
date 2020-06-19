#!/usr/bin/env python3

import spidev
from time import sleep
from vfd import VFD, COLS
import psutil
import socket
import json
from urllib.request import urlopen

vfd = VFD(0, 0)
welcome = "PiHole Monitor"
ip_address = str(socket.gethostbyname(socket.gethostname()))
url = ("http://" + ip_address + "/admin/api.php")

print(welcome)
print(ip_address)
vfd.home()
vfd.text(welcome.center(COLS))
vfd.setCursor(0, 1)
vfd.text('IP:' + ip_address)
sleep(3)

def cpu_state():
    cpu_temp = psutil.sensors_temperatures()['cpu-thermal'][0].current
    return f'{int(psutil.cpu_freq().current)} MHz {cpu_temp:.1f} C'

def get_bytes(t, iface='eth0'):
    with open('/sys/class/net/' + iface + '/statistics/' + t + '_bytes', 'r') as f:
        data = f.read()
        return int(data)

def net_speed():
    tx1 = get_bytes('tx')
    rx1 = get_bytes('rx')
    sleep(1)
    tx2 = get_bytes('tx')
    rx2 = get_bytes('rx')
    tx_speed = (tx2 - tx1) / 1000000.0
    rx_speed = (rx2 - rx1) / 1000000.0
    return f'TX:{tx_speed:.3f} RX:{rx_speed:.3f}'

try:
    while True:
        data = json.load(urlopen(url))
        blocked = data['ads_blocked_today']
        percent = data['ads_percentage_today']
        queries = data['dns_queries_today']
        domains = data['domains_being_blocked']
        print("Blocked" + str(blocked) + "," + "Percent" + str(percent))
        vfd.home()
        vfd.text(cpu_state().center(COLS))
        vfd.setCursor(0, 1)
        vfd.text('Blocked: ' + str(blocked))
        vfd.setCursor(0, 2)
        vfd.text('Percent: ' + str(percent) + "%")
        vfd.setCursor(0, 3)
        vfd.text(net_speed().center(COLS))
        sleep(4)
        vfd.home()
        vfd.text(cpu_state().center(COLS))
        vfd.setCursor(0, 1)
        vfd.text('Queries: ' + str(queries))
        vfd.setCursor(0, 2)
        vfd.text('Domains: ' + str(domains))
        vfd.setCursor(0, 3)
        vfd.text(net_speed().center(COLS))
        sleep(4)

except KeyboardInterrupt:
    print("Stopping..")
    vfd.clear()
    vfd.text("User interrupted".center(COLS))
    sleep(2)
    vfd.clear()
    print("Stopped")

finally:
    vfd.clear()
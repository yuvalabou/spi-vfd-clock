#!/usr/bin/env python

import spidev
import sys
import time
from vfd import VFD
import datetime

vfd = VFD(0,0)
displaySize = 20

try:
    vfd.cls()
    while True:
        now = datetime.datetime.now()
        clock = (now.strftime("%H:%M:%S"))
        vfd.writeStr(clock.center(displaySize))
        time.sleep(0.1)
        vfd.setPosition(0,0)
        time.sleep(0.1)
finally:
   vfd.cls()
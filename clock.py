
#!/usr/bin/env python

import spidev
from time import sleep
from vfd import VFD
import datetime

vfd = VFD(0,0)
displaySize = 20

print("<==== Clock v0.2 ====>")

vfd.setCursor(0, 0)
thistext = "Clock v0.2"
vfd.text(thistext.center(displaySize))
sleep(1)

print("<==== Starting Clock ====>")

try:
    vfd.clear()
    while True:
        now = datetime.datetime.now()
        clock = (now.strftime("%H:%M:%S"))
        vfd.text(clock.center(displaySize))
        sleep(0.1)
        vfd.home()
finally:
   vfd.clear()
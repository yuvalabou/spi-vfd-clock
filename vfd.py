import spidev
import sys
import time

class VFD:
    def __init__(self, spi_num, spi_ce):
        self.spi = spidev.SpiDev()
        self.spi.open(spi_num, spi_ce)
        self.spi.max_speed_hz = 500000
        self.setDisplay(True, False, False)
        self.setDirection(True, False)

    def write(self, data, rs):
        if rs:
            self.spi.writebytes([0xFA, data])
        else:
            self.spi.writebytes([0xF8, data])
        time.sleep(0.00001)

    def writeCmd(self, c):
        self.write(c, False)

    def writeStr(self, s):
        for c in s:
            self.write(ord(c), True)

    def cls(self):
        self.writeCmd(0x01)
        time.sleep(0.005)

    def setPosition(self, x, y):
        self.writeCmd(0x80 | (0x40*y + x))
        time.sleep(0.005)

    def setDirection(self, leftToRight, autoScroll):
        cmd = 4
        if leftToRight:
            cmd = cmd | 2
        if autoScroll:
            cmd = cmd | 1

        self.writeCmd(cmd)

    def setDisplay(self, display, cursor, blink):
        cmd = 8
        if display:
            cmd = cmd | 4
        if cursor:
            cmd = cmd | 2
        if blink:
            cmd = cmd | 1

        self.writeCmd(cmd)
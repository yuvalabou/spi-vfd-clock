"""VFD Lib"""
from time import sleep

import spidev

from .const import *


class VFD:
    def __init__(self, spi_num, spi_ce):
        self.spi = spidev.SpiDev()
        self.spi.open(spi_num, spi_ce)
        self.spi.mode = 3
        self.spi.max_speed_hz = 500000

    def write(self, data, rs):
        """Send data."""
        if rs:
            self.spi.writebytes([VFD_SPIDATA, data])
        else:
            self.spi.writebytes([VFD_SPICOMMAND, data])
        sleep(0.00001)

    def command(self, char):
        self.write(char, False)

    def text(self, strings):
        """Write text."""
        for char in strings:
            self.write(ord(char), True)

    def home(self):
        """Home the cursor."""
        self.command(VFD_RETURNHOME)
        sleep(VFD_SLEEPTIME)

    def clear(self):
        """Clear the display."""
        self.command(VFD_CLEARDISPLAY)
        sleep(VFD_SLEEPTIME)

    def setCursor(self, col, row):
        """Set the cursor to specific cell."""
        _numlines = ROWS
        row_offsets = [0x00, 0x40, 0x14, 0x54]
        if row > _numlines:
            row = _numlines-1
        self.command(VFD_SETDDRAMADDR | (col + row_offsets[row]) )
        sleep(VFD_SLEEPTIME)

    def display(self, _displaycontrol):
        _displaycontrol |=  self.VFD_DISPLAYON
        self.command(VFD_DISPLAYCONTROL | _displaycontrol)

    def blink_on(self):
        _displaycontrol =  VFD_DISPLAYON | VFD_CURSORON | VFD_BLINKON
        self.display(_displaycontrol)

    def blink_off(self):
        _displaycontrol = VFD_DISPLAYON | VFD_CURSOROFF | VFD_BLINKOFF
        self.display(_displaycontrol)

    def scrollDisplayLeft(self):
        self.command(VFD_CURSORSHIFT | VFD_DISPLAYMOVE | VFD_MOVELEFT)

    def scrollDisplayRight(self):
        self.command(VFD_CURSORSHIFT | VFD_DISPLAYMOVE | VFD_MOVERIGHT)

    def autoscroll(self):
        self._displaymode |= VFD_ENTRYSHIFTINCREMENT
        self.command(VFD_ENTRYMODESET | self._displaymode)

    def noAutoscroll(self):
        self._displaymode &= ~VFD_ENTRYSHIFTINCREMENT
        self.command(VFD_ENTRYMODESET | self._displaymode)

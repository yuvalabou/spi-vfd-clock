from time import sleep

import spidev

# data about the display
COLS = 20
ROWS = 4
VFD_SLEEPTIME = 0.005

# commands
VFD_CLEARDISPLAY = 0x01
VFD_RETURNHOME = 0x02
VFD_ENTRYMODESET = 0x04
VFD_DISPLAYCONTROL = 0x08
VFD_CURSORSHIFT = 0x10
VFD_FUNCTIONSET = 0x20
VFD_SETCGRAMADDR = 0x40
VFD_SETDDRAMADDR = 0x80

# flags for display entry mode
VFD_ENTRYRIGHT = 0x00
VFD_ENTRYLEFT = 0x02
VFD_ENTRYSHIFTINCREMENT = 0x01
VFD_ENTRYSHIFTDECREMENT = 0x00

# flags for display on/off control
VFD_DISPLAYON = 0x04
VFD_DISPLAYOFF = 0x00
VFD_CURSORON = 0x02
VFD_CURSOROFF = 0x00
VFD_BLINKON = 0x01
VFD_BLINKOFF = 0x00

# flags for display/cursor shift
VFD_DISPLAYMOVE = 0x08
VFD_CURSORMOVE = 0x00
VFD_MOVERIGHT = 0x04
VFD_MOVELEFT = 0x00

# flags for function set
VFD_8BITMODE = 0x10
VFD_4BITMODE = 0x00
VFD_2LINE = 0x08
VFD_1LINE = 0x00
VFD_BRIGHTNESS25 = 0x03
VFD_BRIGHTNESS50 = 0x02
VFD_BRIGHTNESS75 = 0x01
VFD_BRIGHTNESS100 = 0x00

VFD_5x10DOTS = 0x04
VFD_5x8DOTS = 0x00

VFD_SPICOMMAND = 0xF8
VFD_SPIDATA = 0xFA


class VFD:
    def __init__(self, spi_num, spi_ce):
        self.spi = spidev.SpiDev()
        self.spi.open(spi_num, spi_ce)
        self.spi.mode = 3
        self.spi.max_speed_hz = 500000

    def write(self, data, rs):
        """ Send data """
        if rs:
            self.spi.writebytes([VFD_SPIDATA, data])
        else:
            self.spi.writebytes([VFD_SPICOMMAND, data])
        sleep(0.00001)

    def command(self, char):
        self.write(char, False)

    def text(self, strings):
        for char in strings:
            self.write(ord(char), True)

    def home(self):
        """ Home cursor """
        self.command(VFD_RETURNHOME)
        sleep(VFD_SLEEPTIME)

    def clear(self):
        """ Clear display """
        self.command(VFD_CLEARDISPLAY)
        sleep(VFD_SLEEPTIME)

    def setCursor(self, col, row):
        """ Set cursor position """
        _numlines = ROWS
        row_offsets = [0x00, 0x40, 0x14, 0x54]
        if row > _numlines:
            row = _numlines - 1
        self.command(VFD_SETDDRAMADDR | (col + row_offsets[row]))
        sleep(VFD_SLEEPTIME)

    def display(self, _displaycontrol):
        _displaycontrol |= self.VFD_DISPLAYON
        self.command(VFD_DISPLAYCONTROL | _displaycontrol)

    def blink_on(self):
        _displaycontrol = VFD_DISPLAYON | VFD_CURSORON | VFD_BLINKON
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

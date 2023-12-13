from machine import SPI

bus = 1
device = 0

class lcdspi(object):
    def __init__(self):
        self.spi=SPI(bus, baudrate=1000000)

    def spiwritebyte(self,val):
        self.spi.write(bin(val))
#	self.spi.xfer([val],64000000)

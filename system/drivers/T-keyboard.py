import machine
from machine import Pin

_buf = bytearray(1)
_mv = memoryview(_buf)

# i2c = machine.SoftI2C(scl=machine.Pin(8), sda=machine.Pin(18), freq=400000, timeout=50000)

time.sleep(.5)

def get_key():
    keyboard_device.read(buf=_mv)
    return chr(_buf[0])

def keyboard():
    display.fill(0)
    display.rect(20, 2, width-40, 15, st7789.WHITE)
    buffer = bytearray()
    while True:
        k = get_key()
        
        if k != b'\x00':
            if k == b'\x08':
                buffer=buffer[:-1]
                print(buffer.decode())
                display.text(font, clear, 24, 5, st7789.BLACK)
                display.text(font, buffer.decode(), 25, 5, st7789.YELLOW)
            else:
                buffer += k
                print(buffer.decode())
                display.text(font, clear, 24, 5, st7789.BLACK)
                display.text(font, buffer.decode(), 25, 5, st7789.YELLOW)
        
            if k == b'\r':
                return buffer.decode().strip('\r')
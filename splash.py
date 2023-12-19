import machine
# import utime
import st7789py
import rgb_text


espcolor = st7789py.BLUE
spi = machine.SPI(1, baudrate=40000000, polarity=1)
display = st7789py.ST7789(spi, 240, 240, reset=machine.Pin(5, machine.Pin.OUT), dc=machine.Pin(4, machine.Pin.OUT))
display.init()
#240x240
rgb_text.text(display, 'Welcome to microOS', 80, 120)




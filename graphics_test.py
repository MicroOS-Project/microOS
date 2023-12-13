import machine
# import utime
import st7789py
import rgb_text


espcolor = st7789py.BLUE
spi = machine.SPI(1, baudrate=40000000, polarity=1)
display = st7789py.ST7789(spi, 240, 240, reset=machine.Pin(5, machine.Pin.OUT), dc=machine.Pin(4, machine.Pin.OUT))
display.init()

display.fill_rect(0, 0, 240, 240, st7789py.BLACK)

rgb_text.text(display, 'HELLO!', 10, 10)

display.vline(10, 25, 30, espcolor)
display.hline(20, 25, 30, st7789py.RED)
display.line(65, 65, 120, 120, st7789py.YELLOW)

display.pixel(20, 35, st7789py.MAGENTA)

display.rect(30, 30, 30, 30, st7789py.GREEN)
display.fill_rect(35, 35, 20, 20, st7789py.CYAN)
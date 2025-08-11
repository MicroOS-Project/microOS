import lcd_bus
from micropython import const
import machine

_WIDTH = const(240)
_HEIGHT = const(320)
_BL = const(42)
_DC = const(11)

_MOSI = const(41)
_MISO = const(38)
_SCK = const(40)
_HOST = const(1)

_LCD_CS = const(12)
_LCD_FREQ = const(8000000)

spi_bus = machine.SPI.Bus(
    host=_HOST,
    mosi=_MOSI,
    miso=_MISO,
    sck=_SCK
)

display_bus = lcd_bus.SPIBus(
    spi_bus=spi_bus,
    freq=_LCD_FREQ,
    dc=_DC,
    cs=_LCD_CS
)

import st7789
import task_handler

_MADCTL_MV = const(0x20)
_MADCTL_MX = const(0x40)
_MADCTL_MY = const(0x80)

display = st7789.ST7789(
    data_bus=display_bus,
    display_width=_WIDTH,
    display_height=_HEIGHT,
    backlight_pin=_BL,
    power_pin=10,
    color_space=lv.COLOR_FORMAT.RGB565,
    color_byte_order=st7789.BYTE_ORDER_BGR,
)

display._ORIENTATION_TABLE = (
    0x0,
    _MADCTL_MV | _MADCTL_MY,
    _MADCTL_MY | _MADCTL_MX,
    _MADCTL_MV | _MADCTL_MX
)

display.set_rotation(3)
display.set_power(True)
display.init()
display.set_backlight(100)

try:
    th = task_handler.TaskHandler()
except TypeError:
    print('Task handler is already running. Not starting new task handler')

screen = lv.screen_active()
screen.set_style_bg_color(lv.color_hex(0x000000), 0)

# screen.set_style_text_font(font, 0)

# slider = lv.slider(scrn)
# slider.set_size(250, 25)
# slider.center()
# 
# label = lv.label(scrn)
# label.set_text('HELLO WORLD!')
# label.align(lv.ALIGN.CENTER, 0, -50)

import gt911
from i2c import I2C

touchi2c = I2C.Bus(0, scl=machine.Pin(8), sda=machine.Pin(18), freq=400000)
d=I2C.Device(touchi2c, dev_id=gt911.I2C_ADDR, reg_bits=gt911.BITS)

touch = gt911.GT911(d)

width = 320
height = 240

def displayoff():
    display.set_power(0)

def displayon():
    display.set_power(1)

def setdisplaybacklight(value):
    display.set_backlight(value)
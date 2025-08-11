import st7789

sc = machine.Pin(22, machine.Pin.OUT)

sc.on()

spi = machine.SPI(1, baudrate=40000000, polarity=1)
display = st7789.ST7789(spi, 240, 240, reset=machine.Pin(27, machine.Pin.OUT), dc=machine.Pin(26, machine.Pin.OUT), backlight=sc)
display.init()

width = 240
height = 240
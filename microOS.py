import machine
import utime
import st7789py
import rgb_text


espcolor = st7789py.BLUE
spi = machine.SPI(1, baudrate=40000000, polarity=1)
display = st7789py.ST7789(spi, 240, 240, reset=machine.Pin(5, machine.Pin.OUT), dc=machine.Pin(4, machine.Pin.OUT))
display.init()

display.fill_rect(0, 0, 240, 240, st7789py.BLACK)

with open('systemsettings.txt') as file:
    entries=1
    for line in file:
        line = line.rstrip('\n')
        current_setting = line.split(':')
        sv = current_setting[1]
        sn = current_setting[0]
        if (sn == 'netstat' and entries != 23):
            entries += 1
            rgb_text.text(display, 'Setting net stat', 10, entries*10)
            netstat = True
            utime.sleep(1.25)
        if (sn == 'screenbright' and entries != 23):
            entries += 1
            rgb_text.text(display, 'Setting screen brightness to'+str(sv), 10, entries*10)
            brightness = sv
            utime.sleep(1.25)
        if (sn == 'screenbright' and entries != 23):
            entries += 1
            rgb_text.text(display, 'Setting net name', 10, entries*10)
            netname = sv
            utime.sleep(1.25)
        if (sn == 'netpass' and entries != 23):
            entries += 1
            rgb_text.text(display, 'Setting net pass', 10, entries*10)
            netpass = sv
            utime.sleep(1.25)
        if (sn == 'OSversion' and entries != 23):
            entries += 1
            rgb_text.text(display, 'Getting os version', 10, entries*10)
            osversion = sv
            utime.sleep(1.25)
        elif(entries >= 23):
            display.fill_rect(0, 0, 240, 240, st7789py.BLACK)


display.fill_rect(0, 0, 240, 240, st7789py.BLACK)

display.fill_rect(45, 80, 150, 70, st7789py.WHITE)
# E
display.line(55, 90, 55, 140, espcolor)
display.line(55, 90, 85, 90, espcolor)
display.line(55, 140, 85, 140, espcolor)
display.line(55, 115, 75, 115, espcolor)
utime.sleep(0.5)
# S
display.line(105, 90, 135, 90, espcolor)
display.line(105, 90, 105, 115, espcolor)
display.line(105, 115, 135, 115, espcolor)
display.line(135, 115, 135, 140, espcolor)
display.line(135, 140, 105, 140, espcolor)
utime.sleep(0.5)
# P
display.line(155, 90, 155, 140, espcolor)
display.line(155, 90, 185, 90, espcolor)
display.line(155, 115, 185, 115, espcolor)
display.line(185, 90, 185, 115, espcolor)

rgb_text.text(display, osversion,60, 160)

utime.sleep(0.5)

display.fill_rect(0, 0, 240, 240, st7789py.BLACK)

rgb_text.text(display, 'HELLO!', 10, 10)

display.vline(10, 25, 30, espcolor)
display.hline(20, 25, 30, st7789py.RED)
display.line(65, 65, 120, 120, st7789py.YELLOW)

display.pixel(20, 35, st7789py.MAGENTA)

display.rect(30, 30, 30, 30, st7789py.GREEN)
display.fill_rect(35, 35, 20, 20, st7789py.CYAN)
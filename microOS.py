# MicroOS A PROJECT TO CREATE AN OPERATING SYSTEM FOR MICROCONTROLLERS

import machine
import utime
import st7789py
import rgb_text

def do_connect(name, password):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(name, password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

upamount = 40

espcolor = st7789py.BLUE
spi = machine.SPI(1, baudrate=40000000, polarity=1)
display = st7789py.ST7789(spi, 240, 240, reset=machine.Pin(5, machine.Pin.OUT), dc=machine.Pin(4, machine.Pin.OUT))
display.init()

display.fill_rect(0, 0, 240, 240, st7789py.BLACK)


display.fill_rect(0, 0, 240, 240, st7789py.BLACK)

display.fill_rect(15, 80-upamount, 215, 70, st7789py.WHITE)
display.fill_rect(70, 150-upamount, 100, 70, st7789py.YELLOW)
# M
display.line(20, 140-upamount, 30, 90-upamount, espcolor)
display.line(30, 90-upamount, 40, 140-upamount, espcolor)
display.line(40, 140-upamount, 50, 90-upamount, espcolor)
display.line(50, 90-upamount, 60, 140-upamount, espcolor)

# I
display.line(70, 90-upamount, 100, 90-upamount, espcolor)
display.line(85, 90-upamount, 85, 140-upamount, espcolor)
display.line(70, 140-upamount, 100, 140-upamount, espcolor)

# C
display.line(110, 90-upamount, 140, 90-upamount, espcolor)
display.line(110, 90-upamount, 110, 140-upamount, espcolor)
display.line(110, 140-upamount, 140, 140-upamount, espcolor)


# R
display.line(150, 90-upamount, 150, 140-upamount, espcolor)
display.rect(150, 90-upamount, 25, 25, espcolor)
display.line(150, 115-upamount, 175, 140-upamount, espcolor)

# O
display.rect(190, 90-upamount, 30, 50, espcolor)
display.rect(191, 91-upamount, 28, 48, espcolor)

# O
display.rect(80, 160-upamount, 30, 50, espcolor)
display.rect(81, 161-upamount, 28, 48, espcolor)

# S
display.line(105+20, 90+70-upamount, 135+20, 90+70-upamount, espcolor)
display.line(105+20, 90+70-upamount, 105+20, 115+70-upamount, espcolor)
display.line(105+20, 115+70-upamount, 135+20, 115+70-upamount, espcolor)
display.line(135+20, 115+70-upamount, 135+20, 140+70-upamount, espcolor)
display.line(135+20, 140+70-upamount, 105+20, 140+70-upamount, espcolor)

gc.collect()

with open('systemsettings.txt') as file:
    entries = 20
    for line in file:
        line = line.rstrip('\n')
        current_setting = line.split(':')
        sv = current_setting[1]
        sn = current_setting[0]
#         if (sn == 'screenbright' and entries != 23):
#             rgb_text.text(display, 'Setting screen brightness to'+str(sv), 10, entries*10)
#             backlite.duty(int(sv))
#             utime.sleep(0.5)
        if (sn == 'netname' and entries != 23):
            rgb_text.text(display, 'Setting net name', 10, entries*10)
            ssid = sv
            utime.sleep(0.5)
        if (sn == 'netpass' and entries != 23):
            rgb_text.text(display, 'Setting net pass', 10, entries*10)
            passwd = sv
            utime.sleep(0.5)
        if (sn == 'netstat' and entries != 23):
            if (sv == 'on'):
                rgb_text.text(display, 'Connecting', 10, entries*10)
                do_connect(ssid, passwd)
                utime.sleep(0.5)
            else:
                rgb_text.text(display, 'Wifi is off', 10, entries*10)
        if (sn == 'OSversion' and entries != 23):
            rgb_text.text(display, 'Getting os version', 10, entries*10)
            osversion = sv
            utime.sleep(0.5)


rgb_text.text(display, '       Version ' + osversion, 0, 10)
utime.sleep(5)
 
display.fill_rect(0, 0, 240, 240, st7789py.BLACK)

rgb_text.text(display, 'HELLO!', 10, 10)

display.vline(10, 25, 30, espcolor)
display.hline(20, 25, 30, st7789py.RED)
display.line(65, 65, 120, 120, st7789py.YELLOW)

display.pixel(20, 35, st7789py.MAGENTA)

display.rect(30, 30, 30, 30, st7789py.GREEN)
display.fill_rect(35, 35, 20, 20, st7789py.CYAN)
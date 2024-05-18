import os
os.chdir('/system')
import machine
import time
import st7789
from sound import playsound
import network
from micropython import const
import sys
import random
import vga1_8x8 as font
import vga1_bold_16x32 as fontlarge
import urequests as requests
import _thread as thread

sta_if = network.WLAN(network.STA_IF)

xa = machine.ADC(machine.Pin(36))
ya = machine.ADC(machine.Pin(39))
btn = machine.Pin(32, machine.Pin.IN, machine.Pin.PULL_UP)
sc = machine.Pin(22, machine.Pin.OUT)

sc.on()

xa.atten(xa.ATTN_11DB)
ya.atten(ya.ATTN_11DB)

minval = const(500)
maxval = const(2500)

upamount = 40

espcolor = st7789.BLUE
spi = machine.SPI(1, baudrate=40000000, polarity=1)
display = st7789.ST7789(spi, 240, 240, reset=machine.Pin(27, machine.Pin.OUT), dc=machine.Pin(26, machine.Pin.OUT), backlight=sc)
display.init()

if btn.value() == 0:
    exec(open('microOS.py', 'r').read())
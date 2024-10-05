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
import sdcard

execfile('appRefresh.py')

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

spi = machine.SPI(1, baudrate=40000000, polarity=1)
display = st7789.ST7789(spi, 240, 240, reset=machine.Pin(27, machine.Pin.OUT), dc=machine.Pin(26, machine.Pin.OUT), backlight=sc)
display.init()

os.chdir('/')

try:
    sdspi=machine.SoftSPI(-1, sck=machine.Pin(18), mosi=machine.Pin(23), miso=machine.Pin(19))
    sd = sdcard.SDCard(sdspi, machine.Pin(5))
    os.mount(sd, '/sd')
    print('SD card mounted.')
except Exception as e:
    print('No SD card present.')

LOGGING = True
LOGFILENAME = ''

def log(text):
    if LOGGING:
        logfile=open('/sd/.logs/'+LOGFILENAME+'.log', 'a')
        logfile.write('\n')
        logfile.write(str(time.localtime()[3])+':'+str(time.localtime()[4])+':'+str(time.localtime()[5])+': '+str(text))
        logfile.close()
    else:
        print(str(time.localtime()[3])+':'+str(time.localtime()[4])+': '+str(text))

if btn.value() == 0:
    try:
        logs=os.listdir('/sd/.logs')
        logs.reverse()
        try:
            LOGFILENAME='log_'+str(int(logs[0].strip('log_').strip('.'))+1)
        except:
            LOGFILENAME='log_0'
    except:
        LOGGING = False
    try:
        execfile('/system/microOS.py')
    except Exception as e:
        log('An error ocurred in the system.\nError:\n'+str(e)+'\nPlease refer to the instructions at https://github.com/asherevan/microOS/wiki/Reporting%E2%80%90bugs to report this bug.')
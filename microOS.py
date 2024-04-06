# MicroOS A PROJECT TO CREATE AN OPERATING SYSTEM FOR MICROCONTROLLERS
import os
os.chdir('/system')
import machine
import time
import st7789
import rgb_text
from sound import playsound
import network
from micropython import const
import sys
import random
import vga1_8x8 as font
import uasyncio as asyncio

sta_if = network.WLAN(network.STA_IF)

xa = machine.ADC(machine.Pin(36))
ya = machine.ADC(machine.Pin(39))
btn = machine.Pin(32, machine.Pin.IN, machine.Pin.PULL_UP)
sc = machine.Pin(22, machine.Pin.OUT)

xa.atten(xa.ATTN_11DB)
ya.atten(ya.ATTN_11DB)

sc.on()

minval = const(500)
maxval = const(2500)

def do_connect(name, password):
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(name, password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

def waitscreensaver():
    timepassed=0
    if timepassed >= 400:
        screensaver()
        timepassed=0
        
    if (xa.read() > maxval):
        timepassed=0

    if (xa.read() < minval):
        timepassed=0
        
    if (btn.value() == 0):
        timepassed=0

    timepassed += 1


upamount = 40

espcolor = st7789.BLUE
spi = machine.SPI(1, baudrate=40000000, polarity=1)
display = st7789.ST7789(spi, 240, 240, reset=machine.Pin(27, machine.Pin.OUT), dc=machine.Pin(26, machine.Pin.OUT), backlight=sc)
display.init()

import interpreter

def screensaver():
    cycles=0
    while True:
        if cycles >= 10:
            display.fill(st7789.BLACK)
            display.text(font, 'Micro OS', random.randint(0,185),random.randint(0,230), st7789.color565(random.getrandbits(8),random.getrandbits(8),random.getrandbits(8)))
            cycles=0
#        display.fill_rect(random.randint(0,200), random.randint(0,200), random.randint(0,200),random.randint(0,200))
        if xa.read() >= maxval or xa.read() <= minval or ya.read() >= maxval or ya.read() <= minval or btn.value() == 0:
            break
        cycles+=1
        time.sleep(0.2)
    redrawcanvas()

def redrawcanvas():
    display.fill(st7789.BLACK)

    # menu:
    selected = 0

#apps button
    display.text(font, '  Apps    Settings   Store', 10, 225)
    display.fill_rect(15, 174, 9, 9, st7789.WHITE)
    display.fill_rect(35, 174, 9, 9, st7789.WHITE)
    display.fill_rect(55, 174, 9, 9, st7789.WHITE)

    display.fill_rect(15, 194, 9, 9, st7789.WHITE)
    display.fill_rect(35, 194, 9, 9, st7789.WHITE)
    display.fill_rect(55, 194, 9, 9, st7789.WHITE)

    display.fill_rect(15, 214, 9, 9, st7789.WHITE)
    display.fill_rect(35, 214, 9, 9, st7789.WHITE)
    display.fill_rect(55, 214, 9, 9, st7789.WHITE)

#settings button
    display.fill_rect(107+10, 185, 6, 40, st7789.WHITE)
    display.fill_rect(95+10, 170, 30, 25, st7789.WHITE)
    display.fill_rect(100+10, 170, 20, 20, st7789.BLACK)

#store button
    display.fill_rect(160+18, 195, 40, 25, st7789.WHITE)
    display.fill_rect(165+18, 185, 30, 10, st7789.WHITE)
    display.fill_rect(170+18, 190, 20, 5, st7789.BLACK)

    display.fill_rect(15, 80-upamount, 215, 70, st7789.WHITE)
    display.fill_rect(70, 150-upamount, 100, 70, st7789.YELLOW)

    #show symbol again
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

    over = 1
    cycles = 0

def redrawsettings():
    display.fill(st7789.BLACK)
    
    display.text(font, '           Settings', 0, 1)
    
    display.text(font, 'WiFi Stat:  '+netstat, 2, 20)
    display.text(font, 'WiFi Name:  '+ssid, 2, 35)
    display.text(font, 'WiFi Pass:  '+passwd, 2, 50)
    display.text(font, 'OS Info  >', 2, 65)
    display.text(font, 'Shut Down', 2, 80)
    
    selectedsetting = 0
    
    while True:
        time.sleep(0.15)
        if selectedsetting > 5:
            updatesettings()
            selectedsetting = 0
        if xa.read() < minval:
            settingsfile = 'netname:'+ssid+'\nnetpass:'+passwd+'\nnetstat:'+netstat+'\nOSversion:'+osversion
            file = open('systemsettings.txt', 'w')
            file.write(settingsfile)
            file.close()
            break
        if ya.read() > maxval:
            selectedsetting +=1
            updatesettings()
        if ya.read() < minval:
            selectedsetting -=1
            updatesettings()
        if btn.value() == 0:
            if selectedsetting == 0:
                if netstat == 'off':
                    exec("netstat = 'on'")
                    do_connect(ssid, passwd)
                    display.text(font, 'WiFi Stat:  '+netstat+' ', 2, 20)
                elif netstat == 'on':
                    exec("netstat = 'off'")
                    sta_if.disconnect()
                    sta_if.active(False)
                    display.text(font, 'WiFi Stat:  '+netstat, 2, 20)
            if selectedsetting == 3:
                display.fill(st7789.BLACK)
                display.text(font, '           OS Info', 2, 2) 
                display.text(font, 'OS Version: '+osversion, 2, 20)
                display.text(font, 'Platform: '+sys.platform, 2, 35)
                #display.text(font, 'Firmware Version:'+str(sys.version), 2, 50)
                while True:
                    time.sleep(0.15)
                    if xa.read() <= minval:
                        break
                redrawsettings()
            if selectedsetting == 4:
                sc.off()
                sys.exit()

        display.rect(1, 19+(selectedsetting*15), 238, 12, st7789.WHITE)

def updatesettings():
    for i in range(0, 24):
        display.rect(1, 19+(15*i), 238, 12, st7789.BLACK)

def settings():
    display.fill(st7789.BLACK)
    
    display.text(font, '           Settings', 0, 1)
    
    display.text(font, 'WiFi Stat:  '+netstat, 2, 20)
    display.text(font, 'WiFi Name:  '+ssid, 2, 35)
    display.text(font, 'WiFi Pass:  '+passwd, 2, 50)
    display.text(font, 'OS Info  >', 2, 65)
    display.text(font, 'Shut Down', 2, 80)
    
    selectedsetting = 0
    
    while True:
        time.sleep(0.15)
        if selectedsetting > 5:
            updatesettings()
            selectedsetting = 0
        if xa.read() < minval:
            settingsfile = 'netname:'+ssid+'\nnetpass:'+passwd+'\nnetstat:'+netstat+'\nOSversion:'+osversion
            file = open('systemsettings.txt', 'w')
            file.write(settingsfile)
            file.close()
            break
        if ya.read() > maxval:
            selectedsetting +=1
            updatesettings()
        if ya.read() < minval:
            selectedsetting -=1
            updatesettings()
        if btn.value() == 0:
            if selectedsetting == 0:
                if netstat == 'off':
                    exec("netstat = 'on'")
                    asyncio.create_task(do_connect(ssid, passwd))
                    display.text(font, 'WiFi Stat:  '+netstat, 2, 20)
                elif netstat == 'on':
                    exec("netstat = 'off'")
                    sta_if.disconnect()
                    sta_if.active(False)
                    display.text(font, 'WiFi Stat:  '+netstat, 2, 20)
            if selectedsetting == 3:
                display.fill(st7789.BLACK)
                display.text(font, '           OS Info', 2, 2) 
                display.text(font, 'OS Version: '+osversion, 2, 20)
                display.text(font, 'Platform: '+sys.platform, 2, 35)
                while True:
                    time.sleep(0.15)
                    if xa.read() <= minval:
                        break
                redrawsettings()
            if selectedsetting == 4:
                sc.off()
                sys.exit()

        display.rect(1, 19+(selectedsetting*15), 238, 12, st7789.WHITE)

def updateapps():
    for i in range(1, 24):
        display.rect(5, 10*i, 230, 10, st7789.BLACK)

def app_menu():
    display.fill(st7789.BLACK)

    apps = []
    appamount=0
    selectedapp = 0

    dircontents = os.listdir('/apps')
    for i in dircontents:
        apps.append(i)
        display.text(font, i, 10, 10*appamount)
        appamount += 1
        print(apps)

    updateapps()
    while True:
        if selectedapp >= appamount-1:
            selectedapp = -1
        if selectedapp < -1:
            selectedapp = appamount - 1
            
        if btn.value() == 0:
            interpreter.interpret(apps[selectedapp])

        if ya.read() < minval:
            print(selectedapp)
            updateapps()
            selectedapp -= 1

        if ya.read() > maxval:
            print(selectedapp)
            updateapps()
            selectedapp += 1
        if xa.read() < minval:
            break
            
        display.rect(5, 10 * selectedapp, 230, 10, st7789.RED)

        time.sleep(0.15)
        
    display.fill(st7789.WHITE)
    display.fill_rect(11, 170, 60, 60, st7789.BLACK)
    display.text(font, '  Apps', 10, 225, st7789.BLACK, st7789.WHITE)
    display.line(0, 165, 240, 165, st7789.BLACK)
    display.rect(9+selected*70, 168, 64, 68, espcolor)


display.fill_rect(0, 0, 240, 240, st7789.BLACK)


display.fill_rect(0, 0, 240, 240, st7789.BLACK)

display.fill_rect(15, 80-upamount, 215, 70, st7789.WHITE)
display.fill_rect(70, 150-upamount, 100, 70, st7789.YELLOW)
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

newval = ''
netstat = ''

with open('systemsettings.txt') as file:
    for line in file:
        line = line.rstrip('\n')
        current_setting = line.split(':')
        sv = current_setting[1]
        sn = current_setting[0]
        if sn == 'netname':
            ssid = sv.split('\r')[0]
            
        if sn == 'netpass':
            passwd = sv.split('\r')[0]
            
        if sn == 'netstat':
            if sv == 'on':
                do_connect(ssid, passwd)
            netstat = sv.split('\r')[0]

        if sn == 'OSversion':
            osversion = sv.split('\r')[0]

        if sn == 'new':
            newval = sv.split('\r')[0]

display.text(font, 'Version ' + osversion, 65, 10)
time.sleep(2.5)

display.fill(st7789.BLACK)

# menu:
selected = 0

upamount = upamount + 20

redrawcanvas()

over = 1

hour = 0
curtime = time.localtime()
if curtime[3] > 12:
    hour = curtime[3] - 12
else:
    hour = curtime[3]
display.text(font, str(hour)+':'+str(curtime[4]),100,0)

cycles = 0
timepassed = 0

while True:
    time.sleep(0.15)
    display.rect(9, 168, 64, 68, st7789.BLACK)
    display.rect(9+1*80, 168, 64, 68, st7789.BLACK)
    display.rect(6+2*80, 168, 64, 68, st7789.BLACK)
    if (over == 1):
        display.rect(9+0*80, 168, 64, 68, st7789.RED)
        
    if (over == 2):
        display.rect(9+1*80, 168, 64, 68, st7789.RED)
        
    if (over == 3):
        display.rect(6+2*80, 168, 64, 68, st7789.RED)
        
    if (xa.read() > maxval):
        timepassed=0
        over+=1
    if (xa.read() < minval):
        timepassed=0
        over-=1
        
    if (btn.value() == 0):
        timepassed=0
        if over == 1:
            app_menu()
            redrawcanvas()
        if over == 2:
            print('settings')
            settings()
            redrawcanvas()
        if over == 3:
            print('app store')
 
    if (over>3):
        over=1
        
    if (over<1):
        over=3

    if cycles == 6:
        curtime = time.localtime()
        if curtime[3] > 12:
            hour = curtime[3] - 12
        display.text(font, str(hour)+':'+str(curtime[4]),100,0)
        cycles = 0
        
    if timepassed >= 400:
        screensaver()
        timepassed=0
        
    cycles += 1
    timepassed += 1
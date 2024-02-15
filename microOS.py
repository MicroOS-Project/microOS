# MicroOS A PROJECT TO CREATE AN OPERATING SYSTEM FOR MICROCONTROLLERS
import os
os.chdir('/system')
import machine
import time
import st7789py
import rgb_text
from sound import playsound

vb = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)
cu = machine.Pin(33, machine.Pin.IN, machine.Pin.PULL_UP)
pb = machine.Pin(32, machine.Pin.IN, machine.Pin.PULL_UP)
sc = machine.Pin(22, machine.Pin.OUT)

sc.on()

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
display = st7789py.ST7789(spi, 240, 240, reset=machine.Pin(27, machine.Pin.OUT), dc=machine.Pin(26, machine.Pin.OUT))
display.init()

import interpreter

def redrawcanvas():
    display.fill(st7789py.BLACK)

    # menu:
    selected = 0
    display.line(0, 165, 240, 165, st7789py.WHITE)

#apps button
    display.fill_rect(11, 170, 60, 60, st7789py.BLACK)
    rgb_text.text(display, '  Apps   Settings  Store', 10, 225, color=st7789py.WHITE, background=st7789py.BLACK)
    display.rect(9+selected*70, 168, 64, 68, espcolor)
    display.fill_rect(15, 174, 9, 9, st7789py.WHITE)
    display.fill_rect(35, 174, 9, 9, st7789py.WHITE)
    display.fill_rect(55, 174, 9, 9, st7789py.WHITE)

    display.fill_rect(15, 194, 9, 9, st7789py.WHITE)
    display.fill_rect(35, 194, 9, 9, st7789py.WHITE)
    display.fill_rect(55, 194, 9, 9, st7789py.WHITE)

    display.fill_rect(15, 214, 9, 9, st7789py.WHITE)
    display.fill_rect(35, 214, 9, 9, st7789py.WHITE)
    display.fill_rect(55, 214, 9, 9, st7789py.WHITE)
    
#settings button
    display.fill_rect(107, 185, 6, 40, st7789py.WHITE)
    display.fill_rect(95, 170, 30, 25, st7789py.WHITE)
    display.fill_rect(100, 170, 20, 20, st7789py.BLACK)
    
#store button
    display.fill_rect(160, 195, 40, 25, st7789py.WHITE)
    display.fill_rect(165, 185, 30, 10, st7789py.WHITE)
    display.fill_rect(170, 190, 20, 5, st7789py.BLACK)

    display.fill_rect(15, 80-upamount, 215, 70, st7789py.WHITE)
    display.fill_rect(70, 150-upamount, 100, 70, st7789py.YELLOW)

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

    #from nums import num

    curtime = time.localtime()
    rgb_text.text(display, '            '+str(curtime[3])+':'+str(curtime[4]))

def settings():
    display.fill(st7789py.BLACK)
    
    rgb_text.text(display, '           Settings', 0, 1)
    
    while True:
        if pb.value() == 0:
            break

def updateapps():
    for i in range(1, 24):
        display.rect(5, 10*i, 230, 10, st7789py.BLACK)

def app_menu():
    display.fill(st7789py.BLACK)

    apps = []
    appamount=0
    selectedapp = 0

    dircontents = os.listdir('/apps')
    for i in dircontents:
        apps.append(i)
        rgb_text.text(display, i, 10, 10*appamount)
        appamount += 1
        print(apps)

    updateapps()
    while True:
        if selectedapp >= appamount-1:
            selectedapp = -1
            
        if cu.value() == 0:
            interpreter.interpret(apps[selectedapp])

        if pb.value() == 0:
            break

        if vb.value() == 0:
            print(selectedapp)
            updateapps()
            selectedapp += 1
            
        display.rect(5, 10 * selectedapp, 230, 10, color=st7789py.RED)

        time.sleep(0.15)
        
    display.fill(st7789py.WHITE)
    display.fill_rect(11, 170, 60, 60, st7789py.BLACK)
    rgb_text.text(display, '  Apps', 10, 225, color=st7789py.BLACK, background=st7789py.WHITE)
    display.line(0, 165, 240, 165, st7789py.BLACK)
    display.rect(9+selected*70, 168, 64, 68, espcolor)


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


with open('systemsettings.txt') as file:
    entries = 20
    for line in file:
        line = line.rstrip('\n')
        current_setting = line.split(':')
        sv = current_setting[1]
        sn = current_setting[0]
        if (sn == 'netname' and entries != 23):
            #rgb_text.text(display, 'Setting net name', 10, entries*10)
            ssid = sv
            
        if (sn == 'netpass' and entries != 23):
            #rgb_text.text(display, 'Setting net pass', 10, entries*10)
            passwd = sv
            
        if (sn == 'netstat' and entries != 23):
            if (sv == 'on'):
                #rgb_text.text(display, 'Connecting', 10, entries*10)
                do_connect(ssid, passwd)
                
        if (sn == 'OSversion' and entries != 23):
            #rgb_text.text(display, 'Getting os version', 10, entries*10)
            osversion = sv
            

rgb_text.text(display, '       Version ' + osversion, 0, 10)
time.sleep(2.5)

display.fill(st7789py.BLACK)

# menu:
selected = 0

upamount = upamount + 20

redrawcanvas()

over = 1

curtime = time.localtime()
if curtime[3] > 12:
    hour = curtime[3] - 12
rgb_text.text(display, '            '+str(hour)+':'+str(curtime[4]))

cycles = 0

display.rect(9, 168, 64, 68, st7789py.BLUE)
display.rect(9+1*70, 168, 64, 68, st7789py.BLUE)
display.rect(9+2*70, 168, 64, 68, st7789py.BLUE)

while True:
    time.sleep(0.15)
    display.rect(9, 168, 64, 68, st7789py.BLUE)
    display.rect(9+1*70, 168, 64, 68, st7789py.BLUE)
    display.rect(9+2*70, 168, 64, 68, st7789py.BLUE)
    if (over == 1):
        display.rect(9+0*70, 168, 64, 68, st7789py.RED)
        
    if (over == 2):
        display.rect(9+1*70, 168, 64, 68, st7789py.RED)
        
    if (over == 3):
        display.rect(9+2*70, 168, 64, 68, st7789py.RED)
        
    if (vb.value() == 0):
        over+=1
    if (pb.value() == 0):
        over-=1
        
    if (cu.value() == 0):
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
        rgb_text.text(display, '            '+str(hour)+':'+str(curtime[4]))
        cycles = 0
    cycles += 1
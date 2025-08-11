import lvgl as lv
import os
import machine
import time
import network
from micropython import const
import sys
import random
import urequests as requests
import _thread as threading
import json
import random
import string
import ntptime
import fs_driver

os.chdir('/system/drivers')

index=open('drivers.conf', 'r')
conf = json.load(index)

LOADEDDRIVERS = []
basedrivers = ['display', 'direction', 'storage', 'keyboard']

def loadDriver(key):
    if not conf[key] == None:
        execfile(conf[key])
        LOADEDDRIVERS.append(key)

# Load base drivers
try:
    loadDriver('direction')
except Exception as e:
    print('Could not initialize a driver for directional control:\n'+str(e))

try:
    loadDriver('storage')
except Exception as e:
    print('Could not initialize a driver for external storage:\n'+str(e))

try:
    loadDriver('display')
except Exception as e:
    print('Could not initialize driver for display:\n'+str(e))

try:
    loadDriver('keyboard')
except Exception as e:
    print('Could not initialize a driver for keyboard input:\n'+str(e))

# Load optional drivers
for i in conf:
    if not i in basedrivers:
        if conf[i][0] == True:
            try:
                execfile(conf[i][1])
                LOADEDDRIVERS.append(i)
            except Exception as e:
                print('Could not initialize the '+str(conf[i][0])+' driver:\n'+str(e))

print('Drivers initialized')

os.chdir('/')

# Register filesystem for importing fonts
fs_drv = lv.fs_drv_t()

fs_driver.fs_register(fs_drv, 'D')

# Define function for importing .bin fonts made by https://lvgl.io/tools/fontconverter
def importfont(filename):
    return lv.binfont_create('D:'+filename)

font = importfont('/system/fonts/jetbrains_mono_8.bin')
fontlarge = importfont('/system/fonts/jetbrains_mono_16.bin')

LOGGING = True
LOGFILENAME = ''
PRINTTRACES = True

# Define the loging function so that the OS can tell us if there is a problem
# If a SD card is mounted, we write to a file, otherwise, simply print
def log(text):
    text = str(time.localtime()[3])+':'+str(time.localtime()[4])+':'+str(time.localtime()[5])+': '+str(text)
    if LOGGING:
        logfile=open('/sd/.logs/'+LOGFILENAME+'.log', 'a')
        logfile.write('\n')
        logfile.write(text)
        logfile.close()
    else:
        print(text)

# Only start the OS if the button is not pressed
if not pressed():
    try:
        logs=os.listdir('/sd/.logs')
        logs.reverse()
        try:
            LOGFILENAME='log_'+str(int(logs[0].strip('log_').strip('.'))+1)
        except:
            LOGFILENAME='log_0'
    except:
        LOGGING = False
    if PRINTTRACES == True:
        execfile('/system/microOS.py')
    else:
        try:
            execfile('/system/microOS.py')
        except Exception as e:
            log('An error occurred in the system.\nError:\n'+str(e)+'\nPlease refer to the instructions at https://github.com/MicroOS-Project/microOS/wiki/Reporting%E2%80%90bugs to report this bug.')
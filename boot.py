import os
os.chdir('/system')
import machine
import time
from sound import playsound
import network
from micropython import const
import sys
import random
import vga1_8x8 as font
import vga1_bold_16x32 as fontlarge
import urequests as requests
import _thread as thread
import json
import random
import string

os.chdir('drivers')

index=open('drivers.conf', 'r')
conf = json.load(index)

LOADEDDRIVERS = []
basedrivers = ['display', 'direction', 'storage', 'keyboard']

# Load base drivers
try:
    execfile(conf['display'])
    LOADEDDRIVERS.append('display')
except:
    print('Could not initialize a driver for display.')

try:
    execfile(conf['direction'])
    LOADEDDRIVERS.append('direction')
except:
    print('Could not initialize a driver for directional control.')

try:
    execfile(conf['storage'])
    LOADEDDRIVERS.append('storage')
except:
    print('Could not initialize a driver for external storage.')

try:
    execfile(conf['keyboard'])
    LOADEDDRIVERS.append('keyboard')
except:
    print('Could not initialize driver for keyboard input')

# Load optional drivers
for i in conf:
    if not i in basedrivers:
        if conf[i][0] == True:
            execfile(conf[i][1])
            LOADEDDRIVERS.append(i)

print('Drivers initialized')

os.chdir('/')

execfile('system/appRefresh.py')

LOGGING = True
LOGFILENAME = ''

def log(text):
    if LOGGING:
        logfile=open('/sd/.logs/'+LOGFILENAME+'.log', 'a')
        logfile.write('\n')
        logfile.write(str(time.localtime()[3])+':'+str(time.localtime()[4])+'.'+str(time.localtime()[5])+': '+str(text))
        logfile.close()
    else:
        print(str(time.localtime()[3])+':'+str(time.localtime()[4])+':'+str(time.localtime()[5])+': '+str(text))

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
    try:
        execfile('/system/microOS.py')
    except Exception as e:
        log('An error occurred in the system.\nError:\n'+str(e)+'\nPlease refer to the instructions at https://github.com/asherevan/microOS/wiki/Reporting%E2%80%90bugs to report this bug.')
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

os.chdir('drivers')

index=open('drivers.conf', 'r')
j = json.load(index)

execfile(j['display'])
execfile(j['direction'])
execfile(j['SDreader'])
execfile(j['keyboard'])

print('Drivers initialized')

os.chdir('/')

execfile('system/appRefresh.py')

LOGGING = True
LOGFILENAME = ''

def log(text):
    if LOGGING:
        logfile=open('/sd/.logs/'+LOGFILENAME+'.log', 'a')
        logfile.write('\n')
        logfile.write(str(time.localtime()[3])+':'+str(time.localtime()[4])+':'+str(time.localtime()[5])+': '+str(text))
        logfile.close()
    else:
        print(str(time.localtime()[3])+':'+str(time.localtime()[4])+':'+str(time.localtime()[5])+': '+str(text))

if btn.value() != 0:
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
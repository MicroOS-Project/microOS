import mip
import urequests as requests
import network
import os
import machine

ssid = 'YOUR NETWORK NAME'
password = 'YOUR NETWORK PASS'

sta_if = network.WLAN(network.STA_IF)

FILEPREFIX = 'https://raw.githubusercontent.com/asherevan/microOS/master/'

def downloadfile(filename, path):
    print('Downloading '+filename)
    r=requests.get(FILEPREFIX+path).text
    file=open(filename, 'w')
    file.write(r)
    file.close()

print('Connecting to network: '+ssid)
sta_if.active(True)
sta_if.connect(ssid, password)
while not sta_if.isconnected():
    print('.')

print('Installing SD Card library')
mip.install('sdcard')
print('Installing String library')
mip.install('string')

#create directories
os.mkdir('/system')
os.mkdir('/apps')
os.mkdir('/tmp')
os.mkdir('/system/drivers')

downloadfile('/boot.py', 'boot.py')
downloadfile('/system/microOS.py', 'microOS.py')
downloadfile('/system/functions.py', 'functions.py')
downloadfile('/system/systemsettings.txt', 'systemsettings.txt')
downloadfile('/system/sound.py', 'sound.py')
downloadfile('/system/appRefresh.py', 'appRefresh.py')
downloadfile('/system/drivers/drivers.conf', 'drivers/drivers.conf')
downloadfile('/system/drivers/analog_joystick_driver.py', 'drivers/analog_joystick_driver.py')
downloadfile('/system/drivers/externalSD.py', 'drivers/analog_joystick_driver.py')
downloadfile('/system/drivers/onscreen_keyboard.py', 'drivers/onscreen_keyboard.py')
downloadfile('/system/drivers/st7789_driver.py', 'drivers/st7789_driver.py')

print('MicroOS has now been installed!')
print('You will need to restart your device.')

#os.remove('./installer.py')

#time.sleep(1)
#machine.reset()

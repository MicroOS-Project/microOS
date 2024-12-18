import mip
import urequests as requests
import network
import os
import machine

ssid = 'YOUR NETWORK NAME'
password = 'YOUR NETWORK PASSWORD'

sta_if = network.WLAN(network.STA_IF)

def downloadfile(filename, path):
    r=requests.get(path).text()
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

#create directories
os.mkdir('/system')
os.mkdir('/apps')
os.mkdir('/tmp')
os.mkdir('/system/drivers')

downloadfile('/system/microOS.py', 'https://raw.githubusercontent.com/asherevan/microOS/master/microOS.py')
downloadfile('/system/functions.py', 'https://raw.githubusercontent.com/asherevan/microOS/master/functions.py')
downloadfile('/system/systemsettings.txt', 'https://raw.githubusercontent.com/asherevan/microOS/master/systemsettings.txt')
downloadfile('/system/sound.py', 'https://raw.githubusercontent.com/asherevan/microOS/master/sound.py')
downloadfile('/boot.py', 'https://raw.githubusercontent.com/asherevan/microOS/master/boot.py')
downloadfile('/system/appRefresh.py', 'https://raw.githubusercontent.com/asherevan/microOS/master/appRefresh.py')
downloadfile('/system/drivers/drivers.conf', 'https://raw.githubusercontent.com/asherevan/microOS/master/drivers/drivers.conf')

print('MicroOS has now been installed!')

os.remove('./installer.py')

time.sleep(1)

machine.reset()
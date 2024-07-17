# MicroOS A PROJECT TO CREATE AN OPERATING SYSTEM FOR MICROCONTROLLERS

os.chdir('/system')

sta_if = network.WLAN(network.STA_IF)

ssid = ''
passwd = ''

letters = ('1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','[',']','\\',';','',"'",',',' ',' ',' ','/','.',' ',' ')
lettersupper = ('!','@','#','$','%','^','&','*','(',')','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','{','}','|',':','','"','<',' ',' ',' ','?','>',' ',' ')

nums = ['1','2','3','4','5','6','7','8','9','0','.','-','+','','/','*','=','C']

apps=[]
links=[]

def do_connect(name, password):
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(name, password)
        while not sta_if.isconnected():
            if xa.read() <= minval:
                sta_if.active(False)
                exec('netstat = "off"')
                break
    print('network config:', sta_if.ifconfig())

execfile('functions.py')

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
    
    timepassed=0
    
    while True:
        time.sleep(0.15)
        if xa.read() < minval:
            timepassed=0
            settingsfile = 'netname:'+ssid+'\nnetpass:'+passwd+'\nnetstat:'+netstat+'\nOSversion:'+osversion
            file = open('/system/systemsettings.txt', 'w')
            file.write(settingsfile)
            file.close()
            break
        if ya.read() > maxval:
            timepassed=0
            selectedsetting +=1
            updatesettings()
        if ya.read() < minval:
            timepassed=0
            selectedsetting -=1
            updatesettings()
        if btn.value() == 0:
            timepassed=0
            if selectedsetting == 0:
                if netstat == 'off':
                    exec("netstat = 'on'")
                    display.fill(0)
                    display.text(font, 'Connecting to network:', 10, 100)
                    display.text(font, ssid, 10, 115)
                    do_connect(ssid, passwd)
                    settings()
                elif netstat == 'on':
                    exec("netstat = 'off'")
                    sta_if.disconnect()
                    sta_if.active(False)
                    display.text(font, 'WiFi Stat:  '+netstat, 2, 20)
            if selectedsetting == 1:
                exec('ssid = keyboard()')
                settings()
            if selectedsetting == 2:
                exec('passwd = keyboard()')
                settings()
            if selectedsetting == 3:
                display.fill(st7789.BLACK)
                display.text(font, '           OS Info', 2, 2) 
                display.text(font, 'OS Version: '+osversion, 2, 20)
                display.text(font, 'Platform: '+sys.platform, 2, 35)
                display.text(font, 'IP Address: '+sta_if.ifconfig()[0], 2, 50)
                while True:
                    time.sleep(0.15)
                    if xa.read() <= minval:
                        break
                settings()
            if selectedsetting == 4:
                sc.off()
                sys.exit()

        if selectedsetting < 0:
            timepassed=0
            selectedsetting = 5
            
        if selectedsetting > 5:
            timepassed=0
            selectedsetting = 0


        display.rect(1, 19+(selectedsetting*15), 238, 12, st7789.WHITE)
                
        if timepassed >= 400:
            screensaver()
            timepassed=0

        timepassed += 1        
        
#actualy start booting
        
display.fill_rect(0, 0, 240, 240, st7789.BLACK)

microoswords()

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

os.chdir('/')

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
            appstorecheck()
            redrawcanvas()
 
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
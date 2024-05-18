# MicroOS A PROJECT TO CREATE AN OPERATING SYSTEM FOR MICROCONTROLLERS

ssid = ''
passwd = ''

letters = ('1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','[',']','\\',';','',"'",',',' ',' ',' ','/','.',' ',' ')
lettersupper = ('!','@','#','$','%','^','&','*','(',')','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','{','}','|',':','','"','<',' ',' ',' ','?','>',' ',' ')

import interpreter

def do_connect(name, password):
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(name, password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

def redrawletters():
    letter=0
    for i in range(0,5):
        for n in range(0,10):
            display.text(font, letters[letter], 7+n*24, 153+i*17, st7789.YELLOW)
            letter += 1
    display.fill_rect(190, 218, 50, 20, st7789.BLACK)
    display.fill_rect(70, 218, 74, 20, st7789.BLACK)

    display.rect(74, 218, 68, 15, st7789.WHITE)
    display.rect(194, 218, 44, 15, st7789.WHITE)

    display.text(font, 'UP', 5, 222, st7789.YELLOW)
    display.text(font, 'SPACE', 87, 222, st7789.YELLOW)
    display.text(font, 'ENTER', 196, 222, st7789.YELLOW)

def redrawlettersupper():
    letter=0
    for i in range(0,5):
        for n in range(0,10):
            display.text(font, lettersupper[letter], 7+n*24, 153+i*17, st7789.YELLOW)
            letter += 1
    display.fill_rect(190, 218, 50, 20, st7789.BLACK)
    display.fill_rect(70, 218, 74, 20, st7789.BLACK)

    display.rect(74, 218, 68, 15, st7789.WHITE)
    display.rect(194, 218, 44, 15, st7789.WHITE)

    display.text(font, 'UP', 5, 222, st7789.YELLOW)
    display.text(font, 'SPACE', 87, 222, st7789.YELLOW)
    display.text(font, 'ENTER', 196, 222, st7789.YELLOW)

def keyboard(pretyped=''):
    display.fill(0)
    typed = pretyped
    selected = ''
    letter = 0

    row = 0
    collum = 0
    width = 20

    display.rect(width, 2, 200, 15, st7789.WHITE)

    def updatekeyboard():
        for i in range(0,5):
            for n in range(0,10):
                display.rect(2+n*24, 150+i*17, 20, 15, st7789.WHITE)

    updatekeyboard()

    redrawletters()

    display.rect(2+collum*24, 150+row*17, width, 15, st7789.RED)

    upper = False

    while True:
        time.sleep(0.15)
        display.rect(2+collum*24, 150+row*17, width, 15, st7789.WHITE)

        display.text(font, typed, 25, 5, st7789.YELLOW)
        if xa.read() <= minval:
            collum -= 1
        if xa.read() >= maxval:
            collum += 1

        if ya.read() <= minval:
            row -= 1
        if ya.read() >= maxval:
            row += 1
            
        if row < 0:
            row = 0
        if collum < 0:
            collum = 0
        if row > 4:
            row = 4
        if collum > 9:
            collum = 9
            
        if row == 4 and collum >= 3 and collum <= 5:
            width = 68
        elif row == 4 and collum >= 8 and collum <= 9:
            width = 44
        else:
            width = 20
            
        if btn.value() == 0:
            if selected == 'enter':
                return typed
                break
            else:
                if upper == False:
                    selected = letters[row * 10 + collum]
                    typed = typed + selected
                else:
                    selected = lettersupper[row * 10 + collum]
                    typed = typed + selected
                    upper = False
                    redrawletters()
        if row == 4 and collum == 8:
            selected = 'enter'
        elif row == 4 and collum == 0:
            selected = ''
            upper = True
            redrawlettersupper()

        display.rect(2+collum*24, 150+row*17, width, 15, st7789.RED)
        
def unubstructingkeyboard(pretyped=''):
    typed = pretyped
    selected = ''
    letter = 0
    row = 0
    collum = 0
    width = 20

    display.rect(width, 2, 200, 15, st7789.WHITE)

    def updatekeyboard():
        for i in range(0,5):
            for n in range(0,10):
                display.rect(2+n*24, 150+i*17, 20, 15, st7789.WHITE)

    updatekeyboard()
    
    redrawletters()

    display.rect(2+collum*24, 150+row*17, width, 15, st7789.RED)

    upper = False

    while True:
        time.sleep(0.15)
        display.rect(2+collum*24, 150+row*17, width, 15, st7789.WHITE)

        display.text(font, typed, 25, 5, st7789.YELLOW)
        if xa.read() <= minval:
            collum -= 1
        if xa.read() >= maxval:
            collum += 1

        if ya.read() <= minval:
            row -= 1
        if ya.read() >= maxval:
            row += 1
            
        if row < 0:
            row = 0
        if collum < 0:
            collum = 0
        if row > 4:
            row = 4
        if collum > 9:
            collum = 9
            
        if row == 4 and collum >= 3 and collum <= 5:
            width = 68
        elif row == 4 and collum >= 8 and collum <= 9:
            width = 44
        else:
            width = 20
            
        if btn.value() == 0:
            if selected == 'enter':
                return typed
                break
            else:
                if upper == False:
                    selected = letters[row * 10 + collum]
                    typed = typed + selected
                else:
                    selected = lettersupper[row * 10 + collum]
                    typed = typed + selected
                    upper = False
                    redrawletters()
        if row == 4 and collum == 8:
            selected = 'enter'
        elif row == 4 and collum == 0:
            selected = ''
            upper = True
            redrawlettersupper()

        display.rect(2+collum*24, 150+row*17, width, 15, st7789.RED)

def screensaver():
    cycles=0
    while True:
        if cycles >= 10:
            display.fill(st7789.BLACK)
            display.text(fontlarge, 'Micro OS', random.randint(10,110),random.randint(10,230), st7789.color565(random.getrandbits(8),random.getrandbits(8),random.getrandbits(8)))
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

def appstorecheck():
    display.fill(0)
    if sta_if.isconnected():
        appstore()
    else:
        display.text(font, 'No WiFi. Exit?', 75, 100)
        display.text(font, 'OK', 112, 127)
        display.rect(108, 124, 24, 14, st7789.WHITE)
        while True:
            time.sleep(0.25)
            if not btn.value():
                break

def split_string(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]

def appstore():
    apps = []
    links = []
    display.fill(0)
    
    display.text(font, 'App Store', 75, 1)
    
    r=requests.get('https://raw.githubusercontent.com/asherevan/microOS-apps/master/index.txt')
    file=open('apps.txt', 'w')
    file.write(r.text)
    file.close()

    with open('apps.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            apps.append(line.split(':')[0])
            links.append(line.split(':')[1])

    line = 0
    selected = 0
    for i in apps:
        display.text(font, i, 2, 12+10*line)
        line += 1

    while True:
        time.sleep(0.15)
        display.rect(1, 11+10*selected, 238, 10, st7789.BLACK)

        if xa.read() <= minval:
            break
        if ya.read() >= maxval:
            selected += 1
        if ya.read() <= minval:
            selected -= 1
        if selected < 0:
            selected = line-1
        if selected > line-1:
            selected = 0

        if btn.value() == 0:
            display.fill(0)
            display.text(font, apps[selected], 75, 1)
            r=requests.get('https://raw.githubusercontent.com/asherevan/microOS-apps/master/'+apps[selected]+'/details.txt')
            results=r.text
            line = 0
            for i in split_string(results, 30):
                display.text(font, i, 2, 12+10*line)
                line +=1

            display.rect(20, 217, 200, 12, st7789.WHITE)
            if not apps[selected] in os.listdir():
                display.text(font, 'INSTALL', 85, 218)
            else:
                display.text(font, 'REMOVE', 90, 218)
            while True:
                time.sleep(0.15)
                if xa.read() <= minval:
                    break
                if btn.value() == 0:
                    r=requests.get('https://raw.githubusercontent.com/asherevan/microOS-apps/master/'+apps[selected]+'/main.py')
                    file=open('/apps/'+apps[selected]+'/main.py', 'w')
                    file.write(r.text)
                    file.close()
            appstore()

        display.rect(1, 11+10*selected, 238, 10, st7789.RED)

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
            file = open('systemsettings.txt', 'w')
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
                    do_connect(ssid, passwd)
                    display.text(font, 'WiFi Stat:  '+netstat+'  ', 2, 20)
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

        #timepassed += 1

def updateapps():
    for i in range(0, 24):
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
    
    print(appamount)

    updateapps()
    
    while True:
        time.sleep(0.15)
        
        if btn.value() == 0:
            interpreter.interpret('/apps/'+apps[selectedapp]+'/main.py')
            app_menu()

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

        if selectedapp >= appamount:
            updateapps()
            selectedapp = 0
        if selectedapp < 0:
            updateapps()
            selectedapp = appamount-1

        display.rect(5, 10 * selectedapp, 230, 10, st7789.RED)
        
        
#actualy start booting
        
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
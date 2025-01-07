def microoswords():
    display.fill_rect(15, 40-20, 215, 70, st7789.WHITE)
    display.fill_rect(70, 110-20, 100, 70, st7789.YELLOW)
    # M
    display.line(20, 100-20, 30, 50-20, st7789.BLUE)
    display.line(30, 50-20, 40, 100-20, st7789.BLUE)
    display.line(40, 100-20, 50, 50-20, st7789.BLUE)
    display.line(50, 50-20, 60, 100-20, st7789.BLUE)

    # I
    display.line(70, 50-20, 100, 50-20, st7789.BLUE)
    display.line(85, 50-20, 85, 100-20, st7789.BLUE)
    display.line(70, 100-20, 100, 100-20, st7789.BLUE)

    # C
    display.line(110, 50-20, 140, 50-20, st7789.BLUE)
    display.line(110, 50-20, 110, 100-20, st7789.BLUE)
    display.line(110, 100-20, 140, 100-20, st7789.BLUE)


    # R
    display.line(150, 50-20, 150, 100-20, st7789.BLUE)
    display.rect(150, 50-20, 25, 25, st7789.BLUE)
    display.line(150, 75-20, 175, 100-20, st7789.BLUE)

    # O
    display.rect(190, 50-20, 30, 50, st7789.BLUE)
    display.rect(191, 51-20, 28, 48, st7789.BLUE)

    # O
    display.rect(80, 120-20, 30, 50, st7789.BLUE)
    display.rect(81, 121-20, 28, 48, st7789.BLUE)

    # S
    display.line(105+20, 120-20, 135+20, 120-20, st7789.BLUE)
    display.line(105+20, 120-20, 105+20, 145-20, st7789.BLUE)
    display.line(105+20, 145-20, 135+20, 145-20, st7789.BLUE)
    display.line(135+20, 145-20, 135+20, 170-20, st7789.BLUE)
    display.line(135+20, 170-20, 105+20, 170-20, st7789.BLUE)

def screensaver():
    cycles=0
    while True:
        if cycles >= 10:
            display.fill(st7789.BLACK)
            display.text(fontlarge, 'Micro OS', random.randint(10,110),random.randint(10,230), st7789.color565(random.getrandbits(8),random.getrandbits(8),random.getrandbits(8)))
            cycles=0
#        display.fill_rect(random.randint(0,200), random.randint(0,200), random.randint(0,200),random.randint(0,200))
        if pressed() or left() or right() or up() or down():
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

    #show symbol again
    microoswords()
    
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
            if pressed() or left():
                break

def split_string(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]

def appstore():
    apps = []
    links = []
    display.fill(0)
    
    display.text(font, 'App Store', 75, 1)
    
    try:
        with open('/system/apps.txt') as file:
            for line in file:
                line = line.rstrip('\n')
                apps.append(line.split(';')[0])
                links.append(line.split(';')[1])
    except:
        r=requests.get('https://raw.githubusercontent.com/asherevan/microOS-apps/master/index.txt')
        file=open('/system/apps.txt', 'w')
        file.write(r.text)
        file.close()
        with open('/system/apps.txt') as file:
            for line in file:
                line = line.rstrip('\n')
                apps.append(line.split(';')[0])
                links.append(line.split(';')[1])
    print(apps)
    print(links)

    line = 0
    selected = 0
    for i in apps:
        display.text(font, i, 2, 12+10*line)
        line += 1

    while True:
        time.sleep(0.15)
        display.rect(1, 11+10*selected, 238, 10, st7789.BLACK)

        if left():
            break
        if down():
            selected += 1
        if up():
            selected -= 1
        if selected < 0:
            appsrefresh()
            appstore()
            selected = line-1
        if selected > line-1:
            selected = 0

        if pressed():
            display.fill(0)
            display.text(font, apps[selected], 75, 1)
            r=requests.get(links[selected]+'details.txt')
            results=r.text
            line = 0
            for i in split_string(results, 29):
                display.text(font, i, 2, 12+10*line)
                line += 1

            display.rect(20, 217, 200, 12, st7789.WHITE)
            if not apps[selected] in os.listdir('/apps'):
                display.text(font, 'INSTALL', 85, 218)
            else:
                display.text(font, 'REMOVE', 90, 218, st7789.RED)
            while True:
                time.sleep(0.15)
                if left():
                    break
                if pressed():
                    if not apps[selected] in os.listdir('/apps'):
                        display.text(font, 'Installing', 80, 218, st7789.BLUE)
                        os.mkdir('/apps/'+apps[selected])
                        try:
                            r=requests.get(links[selected]+'files.txt').text
                            files=r.split('\n')
                            for i in files:
                                r = requests.get(links[selected]+i).text
                                file=open('/apps/'+apps[selected]+'/'+i, 'w')
                                file.write(r)
                                file.close()
                        except:
                            r = requests.get(links[selected]+'main.py').text
                            file=open('/apps/'+apps[selected]+'/main.py', 'w')
                            file.write(r)
                            file.close()
                        appstore()
                    else:
                        for i in os.listdir('/apps/'+apps[selected]):
                            os.remove('/apps/'+apps[selected]+'/'+i)
                        os.rmdir('/apps/'+apps[selected])
                        appstore()
            appstore()

        display.rect(1, 11+10*selected, 238, 10, st7789.RED)

def appsrefresh():
    display.fill(0)
    display.text(font, 'Refreshing Apps...', 48, 104)
    r=requests.get('https://raw.githubusercontent.com/asherevan/microOS-apps/master/index.txt')
    file=open('/system/apps.txt', 'w')
    file.write(r.text)
    file.close()

    with open('/system/apps.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            apps.append(line.split(';')[0])
            links.append(line.split(';')[1])


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
        
        if pressed():
            execfile('/apps/'+apps[selectedapp]+'/main.py')
            app_menu()

        if up():
            print(selectedapp)
            updateapps()
            selectedapp -= 1

        if down():
            print(selectedapp)
            updateapps()
            selectedapp += 1

        if left():
            break

        if selectedapp >= appamount:
            updateapps()
            selectedapp = 0
        if selectedapp < 0:
            updateapps()
            selectedapp = appamount-1

        display.rect(5, 10 * selectedapp, 230, 10, st7789.RED)


def savesettings():
    exec('settingsfile = "OSversion:"+osversion')
    exec('networkfile = netname:"+ssid+"\\nnetpass:"+passwd+"\\nnetstat:"+netstat')
    file = open('/system/systemsettings.txt', 'w')
    file.write(settingsfile)
    file.close()
    file = open('/system/networkConfig.txt', 'w')
    file.write(networkfile)
    file.close()

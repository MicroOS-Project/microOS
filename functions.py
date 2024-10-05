def microoswords():
    display.fill_rect(15, 80-upamount, 215, 70, st7789.WHITE)
    display.fill_rect(70, 150-upamount, 100, 70, st7789.YELLOW)
    # M
    display.line(20, 140-upamount, 30, 90-upamount, st7789.BLUE)
    display.line(30, 90-upamount, 40, 140-upamount, st7789.BLUE)
    display.line(40, 140-upamount, 50, 90-upamount, st7789.BLUE)
    display.line(50, 90-upamount, 60, 140-upamount, st7789.BLUE)

    # I
    display.line(70, 90-upamount, 100, 90-upamount, st7789.BLUE)
    display.line(85, 90-upamount, 85, 140-upamount, st7789.BLUE)
    display.line(70, 140-upamount, 100, 140-upamount, st7789.BLUE)

    # C
    display.line(110, 90-upamount, 140, 90-upamount, st7789.BLUE)
    display.line(110, 90-upamount, 110, 140-upamount, st7789.BLUE)
    display.line(110, 140-upamount, 140, 140-upamount, st7789.BLUE)


    # R
    display.line(150, 90-upamount, 150, 140-upamount, st7789.BLUE)
    display.rect(150, 90-upamount, 25, 25, st7789.BLUE)
    display.line(150, 115-upamount, 175, 140-upamount, st7789.BLUE)

    # O
    display.rect(190, 90-upamount, 30, 50, st7789.BLUE)
    display.rect(191, 91-upamount, 28, 48, st7789.BLUE)

    # O
    display.rect(80, 160-upamount, 30, 50, st7789.BLUE)
    display.rect(81, 161-upamount, 28, 48, st7789.BLUE)

    # S
    display.line(105+20, 90+70-upamount, 135+20, 90+70-upamount, st7789.BLUE)
    display.line(105+20, 90+70-upamount, 105+20, 115+70-upamount, st7789.BLUE)
    display.line(105+20, 115+70-upamount, 135+20, 115+70-upamount, st7789.BLUE)
    display.line(135+20, 115+70-upamount, 135+20, 140+70-upamount, st7789.BLUE)
    display.line(135+20, 140+70-upamount, 105+20, 140+70-upamount, st7789.BLUE)


def numpad(textx=25, texty=10):
    def redraw():
        num = 0
        for i in range(0, 3):
            for n in range(0, 6):
                display.text(fontlarge, nums[num], 13+40*n, 130+34*i)
                num +=1
        for i in range(0, 3):
            for n in range(0, 6):
                display.rect(3+40*n, 130+34*i, 34, 30, st7789.BLUE)

    redraw()

    row = 0
    collum = 0

    entered = ''

    while True:
        time.sleep(0.25)
        display.rect(3+40*collum, 130+34*row, 34, 30, st7789.BLUE)
        if btn.value() == 0:
            if nums[row*6+collum] == '=':
                return entered
            elif nums[row*6+collum] == 'C':
                entered = ''
                display.fill_rect(11, texty, 220, 32, st7789.BLACK)
                display.text(fontlarge, entered, textx, texty, st7789.BLUE)
                print(entered)
            else:
                entered += nums[row*6+collum]
                display.fill_rect(11, texty, 220, 32, st7789.BLACK)
                display.text(fontlarge, entered, textx, texty, st7789.BLUE)

        if xa.read() < minval:
            collum -= 1
        if xa.read() > maxval:
            collum += 1
        if ya.read() < minval:
            row -= 1
        if ya.read() > maxval:
            row += 1

        if row > 2:
            row = 2
        if row < 0:
            row = 0
        if collum > 5:
            collum = 5
        if collum < 0:
            collum = 0

        display.rect(3+40*collum, 130+34*row, 34, 30, st7789.BLACK)

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
            if not btn.value() or xa.read() <= minval:
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

        if xa.read() <= minval:
            break
        if ya.read() >= maxval:
            selected += 1
        if ya.read() <= minval:
            selected -= 1
        if selected < 0:
            appsrefresh()
            appstore()
            selected = line-1
        if selected > line-1:
            selected = 0

        if btn.value() == 0:
            display.fill(0)
            display.text(font, apps[selected], 75, 1)
            r=requests.get(links[selected]+'details.txt')
            results=r.text
            line = 0
            for i in split_string(results, 30):
                display.text(font, i, 2, 12+10*line)
                line += 1

            display.rect(20, 217, 200, 12, st7789.WHITE)
            if not apps[selected] in os.listdir('/apps'):
                display.text(font, 'INSTALL', 85, 218)
            else:
                display.text(font, 'REMOVE', 90, 218, st7789.RED)
            while True:
                time.sleep(0.15)
                if xa.read() <= minval:
                    break
                if btn.value() == 0:
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
        
        if btn.value() == 0:
            execfile('/apps/'+apps[selectedapp]+'/main.py')
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
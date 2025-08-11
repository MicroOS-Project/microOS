#TODO Make all functions delete all unnecessary vars after they are done with them

def initmain():
    global mainmenu, drawstats, openappslist, opensettings, openstore
    mainmenu = lv.obj()

    drawstats = True

    # Apps list button
    appsbutton = lv.button(mainmenu)
    appsbutton.align(lv.ALIGN.BOTTOM_LEFT, 5, -5)
    appsbutton.set_size(65, 65)
    #TODO replace with actual icon
    appslabel = lv.label(appsbutton)
    appslabel.set_text('Apps')
    appslabel.center()

    # Settings button
    settingsbutton = lv.button(mainmenu)
    settingsbutton.align(lv.ALIGN.BOTTOM_MID, 0, -5)
    settingsbutton.set_size(65, 65)
    #TODO replace with actual icon
    settingslabel = lv.label(settingsbutton)
    settingslabel.set_text('Settings')
    settingslabel.center()

    # App Store button
    storebutton = lv.button(mainmenu)
    storebutton.align(lv.ALIGN.BOTTOM_RIGHT, -5, -5)
    storebutton.set_size(65, 65)
    #TODO replace with actual icon
    storelabel = lv.label(storebutton)
    storelabel.set_text('App Store')
    storelabel.center()
    
    def openappslist(event):
        code = event.get_code()
        if code == lv.EVENT.CLICKED:
            drawstats = False
            log('Opening apps list')
            app_menu()

    def opensettings(event):
        code = event.get_code()
        if code == lv.EVENT.CLICKED:
            drawstats = False
            log('Opening settings main page')
            settings()
    
    def openstore(event):
        code = event.get_code()
        if code == lv.EVENT.CLICKED:
            drawstats = False
            log('Opening app store')
            appstorecheck()

    appsbutton.add_event_cb(openappslist, lv.EVENT.ALL, None)
    settingsbutton.add_event_cb(opensettings, lv.EVENT.ALL, None)
    storebutton.add_event_cb(openstore, lv.EVENT.ALL, None)

    microoswords(mainmenu)

#TODO Also here. This one will take some work
def initsettings():
    global settingsscreen, optionslist, infolist, infoscreen, wifimenuscreen, wifimenulist, wifilistscreen, networkslist, getpassscreen, password, scanningscreen, connectingscreen, connectinglabel, brightnessscreen, brightnessslider, timezonescreen, timezoneinput
    
    def backcb(e):
        settings()
    
    def brightnesscb(e):
        global brightnessslider, display
        display.set_backlight(round(brightnessslider.get_value()*2))

    settingsscreen = lv.obj()
    optionslist = lv.list(settingsscreen)
    optionslist.set_size(width, height)
    
    infoscreen = lv.obj()
    infolist = lv.list(infoscreen)
    infolist.set_size(width, height)
    
    scanningscreen = lv.obj()
    scanninglabel = lv.label(scanningscreen)
    scanninglabel.set_text('Scanning')
    scanninglabel.center()
    scanningspinner = lv.spinner(scanningscreen)
    scanningspinner.set_size(50, 50)
    scanningspinner.align_to(scanninglabel, lv.ALIGN.CENTER, 0, 25)
    
    wifimenuscreen = lv.obj()
    wifimenulist = lv.list(wifimenuscreen)
    wifimenulist.set_size(width, height)
    wifimenulist.set_pos(0, 0)
    
    wifilistscreen = lv.obj()
    networkslist = lv.list(wifilistscreen)
    networkslist.set_size(width, height)
    
    getpassscreen = lv.obj()
    bb = lv.button(getpassscreen)
    bb.set_size(36, 36)
    bb.set_pos(2, 2)
    bb.add_event_cb(netslistcb, lv.EVENT.PRESSED, None)
    password = lv.textarea(getpassscreen)
    password.set_size(width-76, 36)
    password.set_pos(38, 2)
    submitb = lv.button(getpassscreen)
    submitb.set_size(36, 36)
    submitb.set_pos(width-38, 2)
    submitb.add_event_cb(connectnetcb, lv.EVENT.PRESSED, None)
#     password = lv.textarea(getpassscreen)
#     password.set_size(width-80, 36)
#     password.set_placeholder_text('WiFi Password')
#     password.set_password_mode(1)
#     kb = lv.keyboard(getpassscreen)
#     kb.set_textarea(password)
#     submitb = lv.button(getpassscreen)
#     submitb.set_size(36, 36)
#     submitb.align_to(password, lv.ALIGN.OUT_RIGHT_MID, 0, 0)
#     submitt = lv.label(submitb)
#     submitt.set_text(lv.SYMBOL.NEW_LINE)
#     submitt.center()
#     submitb.add_event_cb(connectnetcb, lv.EVENT.PRESSED, None)
    connectingscreen = lv.obj()
    passwd = password.get_text()
    connectinglabel = lv.label(connectingscreen)
    connectinglabel.center()
    connectingspinner = lv.spinner(connectingscreen)
    connectingspinner.set_size(60, 60)
    connectingspinner.align_to(connectinglabel, lv.ALIGN.CENTER, 0, 60)
    
    brightnessscreen = lv.obj()
    brightnessslider = lv.slider(brightnessscreen)
    brightnessslider.set_range(0, 50)
    brightnessslider.set_width(width-80)
    brightnessslider.center()
    brightnessslider.add_event_cb(brightnesscb, lv.EVENT.VALUE_CHANGED, None)
    l1 = lv.label(brightnessscreen)
    l1.set_pos(40, round(height/2)-30)
    l1.set_text('0')
    l2 = lv.label(brightnessscreen)
    l2.set_pos(width-50, round(height/2)-30)
    l2.set_text('100')
    brightback = lv.button(brightnessscreen)
    brightback.set_size(40, 40)
    brightback.align(lv.ALIGN.TOP_LEFT, 1, 1)
    brightbackt = lv.label(brightback)
    brightbackt.set_text('Back')
    brightbackt.center()
    brightback.add_event_cb(backcb, lv.EVENT.PRESSED, None)
    
    timezonescreen = lv.obj()
    timezoneinput = lv.textarea(timezonescreen)
    timezoneinput.set_size(200, 30)
    timezoneinput.center()
    timezoneback = lv.button(timezonescreen)
    timezoneback.align(lv.ALIGN.TOP_LEFT, 1, 1)
    timezoneback.add_event_cb(backcb, lv.EVENT.PRESSED, None)

def initappslist():
    global alscreen, appslist
    alscreen = lv.obj()

    appslist = lv.list(alscreen)
    appslist.set_size(width, height)
    appslist.set_style_bg_color(lv.color_hex(0x000000), 0)
    appslist.set_style_border_color(lv.color_hex(0x000000), 0)

def initappstore():
    global asscreen, aslist, ascscreen
    asscreen = lv.obj()
    
    aslist = lv.list(asscreen)
    aslist.set_size(width, height)
    aslist.set_style_bg_color(lv.color_hex(0x000000), 0)
    aslist.set_style_border_color(lv.color_hex(0x000000), 0)
    
    ascscreen = lv.obj()
    nowifilabel = lv.label(ascscreen)
    nowifilabel.set_text('No WiFi. Exit?')
    nowifilabel.center()
    okbutton = lv.button(ascscreen)
    oklabel = lv.label(okbutton)
    oklabel.set_text('Ok')
    oklabel.center()
    okbutton.align(lv.ALIGN.CENTER, 0, 50)
    def exitasc(event):
        redrawcanvas()
    okbutton.add_event_cb(exitasc, lv.EVENT.PRESSED, None)

def initscreens():
    initmain()
    initappslist()
    initsettings()
    initappstore()

def gettime():
    timehere = list(time.localtime())
    
    timehere[3] += TIMEZONE
    
    if timehere[3] < 0:
        timehere[3] += 24
        timehere[2] -= 1
    return tuple(timehere)

def microoswords(disp):
    fontextralarge = importfont('/system/fonts/jetbrains_mono_thin_50.bin')
    microoslabel = lv.label(disp)
    microoslabel.set_text('MicroOS')
    microoslabel.set_style_text_font(fontextralarge, 0)
    microoslabel.center()
#     display.fill_rect(15, 40-20, 215, 70, st7789.WHITE)
#     display.fill_rect(70, 110-20, 100, 70, st7789.YELLOW)
#     # M
#     display.line(20, 100-20, 30, 50-20, st7789.BLUE)
#     display.line(30, 50-20, 40, 100-20, st7789.BLUE)
#     display.line(40, 100-20, 50, 50-20, st7789.BLUE)
#     display.line(50, 50-20, 60, 100-20, st7789.BLUE)
# 
#     # I
#     display.line(70, 50-20, 100, 50-20, st7789.BLUE)
#     display.line(85, 50-20, 85, 100-20, st7789.BLUE)
#     display.line(70, 100-20, 100, 100-20, st7789.BLUE)
# 
#     # C
#     display.line(110, 50-20, 140, 50-20, st7789.BLUE)
#     display.line(110, 50-20, 110, 100-20, st7789.BLUE)
#     display.line(110, 100-20, 140, 100-20, st7789.BLUE)
# 
# 
#     # R
#     display.line(150, 50-20, 150, 100-20, st7789.BLUE)
#     display.rect(150, 50-20, 25, 25, st7789.BLUE)
#     display.line(150, 75-20, 175, 100-20, st7789.BLUE)
# 
#     # O
#     display.rect(190, 50-20, 30, 50, st7789.BLUE)
#     display.rect(191, 51-20, 28, 48, st7789.BLUE)
# 
#     # O
#     display.rect(80, 120-20, 30, 50, st7789.BLUE)
#     display.rect(81, 121-20, 28, 48, st7789.BLUE)
# 
#     # S
#     display.line(105+20, 120-20, 135+20, 120-20, st7789.BLUE)
#     display.line(105+20, 120-20, 105+20, 145-20, st7789.BLUE)
#     display.line(105+20, 145-20, 135+20, 145-20, st7789.BLUE)
#     display.line(135+20, 145-20, 135+20, 170-20, st7789.BLUE)
#     display.line(135+20, 170-20, 105+20, 170-20, st7789.BLUE)

# Define the screensaver which shows whenever you have not been active for more than a certain ammount of time

def screensaver():
    cycles=0
    while True:
        if cycles >= 10:
            text = lv.label(screen)
            text.set_style_text_font(fontlarge)
            text.set_text('MicroOS')
            # random X and Y
            textX = random.randint(0, width)
            textY = random.randint(0, height)
            # random color
            textcolor = lv.color_hex(hex(random.randint(0, 16777215)))
            # Set position and color
            text.set_pos(textX, textY)
            text.set_style_text_color(textcolor)
            cycles=0
#        display.fill_rect(random.randint(0,200), random.randint(0,200), random.randint(0,200),random.randint(0,200))
        if pressed() or left() or right() or up() or down():
            text.delete()
            del text
            del textX
            del textY
            del textcolor
            break
        cycles+=1
        time.sleep(0.2)
    redrawcanvas()

def redrawcanvas():
    log('Main menu')
    global drawstats, mainmenu

    drawstats = True

    lv.screen_load_anim(mainmenu, lv.SCR_LOAD_ANIM.FADE_IN, 150, 0, False)

def inittimelabel():
    global timelabel, batterylabel, mainmenu
    hour = 0
    curtime = gettime()
    if curtime[3] > 12:
        hour = curtime[3] - 12
    else:
        hour = curtime[3]
    timenow = str(hour)+':'+str(curtime[4])
    timelabel = lv.label(mainmenu)
    timelabel.set_text(timenow)
    timelabel.align(lv.ALIGN.TOP_MID, 0, 1)

def drawtopbar():
    global timelabel, batterylabel, mainmenu
    if sta_if.isconnected():
        inittimelabel()

    if 'battery' in LOADEDDRIVERS:
        percentage = calcPercentage()
        text = ''
        if percentage == 'CH':
            text = 'Charging'
        else:
            text = percentage+'%'
#             if len(text) == 3:
#                 text = '     '+text
#             else:
#                 text = '      '+text

        batterylabel = lv.label(mainmenu)
        batterylabel.set_text(text)
        batterylabel.align(lv.ALIGN.TOP_RIGHT, -1, 1)

def redrawtopbar():
    global timelabel, batterylabel
    # Only draw the time if you are connected to WiFi
    if sta_if.isconnected():
        try:
            type(timelabel)
        except:
            inittimelabel()
        hour = 0
        curtime = gettime()
        if curtime[3] > 12:
            hour = curtime[3] - 12
        else:
            hour = curtime[3]
        timenow = str(hour)+':'+str(curtime[4])
        timelabel.set_text(timenow)
    # Only draw the battery percentage if the battery driver is loaded
    if 'battery' in LOADEDDRIVERS:
        percentage = calcPercentage()
        text = ''
        if percentage == 'CH':
            text = 'Charging'
        else:
            if int(percentage) > 100:
                percentage = '100'
            text = percentage+'%'
#             if len(text) == 3:
#                 text = '     '+text
#             else:
#                 text = '      '+text
        batterylabel.set_text(text)

def appstorecheck():
    global ascscreen
    if sta_if.isconnected():
        appstore()
    else:        
        lv.screen_load_anim(ascscreen, lv.SCR_LOAD_ANIM.FADE_IN, 150, 0, False)

def split_string(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]

#TODO finish this up
def appstore():
    def openappcb():
        pass

    apps = []
    links= []
#     display.fill(0)
    
    
#     display.text(font, 'App Store', 75, 1)
    
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
    
    aslist.clean()
    
    for i in apps:
        item = aslist.add_button('app item', i)
        item.add_event_cb(openappcb, lv.EVENT.ALL, None)
#         display.text(font, i, 2, 12+10*line)
#         line += 1

#     while True:
#         time.sleep(0.15)
#         display.rect(1, 11+10*selected, 238, 10, st7789.BLACK)
# 
#         if left():
#             break
#         if down():
#             selected += 1
#         if up():
#             selected -= 1
#         if selected < 0:
#             appsrefresh()
#             appstore()
#             selected = line-1
#         if selected > line-1:
#             selected = 0
# 
#         if pressed():
#             display.fill(0)
#             display.text(font, apps[selected], 75, 1)
#             r=requests.get(links[selected]+'details.txt')
#             results=r.text
#             line = 0
#             for i in split_string(results, 29):
#                 display.text(font, i, 2, 12+10*line)
#                 line += 1
# 
#             display.rect(20, 217, 200, 12, st7789.WHITE)
#             if not apps[selected] in os.listdir('/apps'):
#                 display.text(font, 'INSTALL', 85, 218)
#             else:
#                 display.text(font, 'REMOVE', 90, 218, st7789.RED)
#             while True:
#                 time.sleep(0.15)
#                 if left():
#                     break
#                 if pressed():
#                     if not apps[selected] in os.listdir('/apps'):
#                         display.text(font, 'Installing', 80, 218, st7789.BLUE)
#                         os.mkdir('/apps/'+apps[selected])
#                         try:
#                             r=requests.get(links[selected]+'files.txt').text
#                             files=r.split('\n')
#                             for i in files:
#                                 r = requests.get(links[selected]+i).text
#                                 file=open('/apps/'+apps[selected]+'/'+i, 'w')
#                                 file.write(r)
#                                 file.close()
#                         except:
#                             r = requests.get(links[selected]+'main.py').text
#                             file=open('/apps/'+apps[selected]+'/main.py', 'w')
#                             file.write(r)
#                             file.close()
#                         appstore()
#                     else:
#                         for i in os.listdir('/apps/'+apps[selected]):
#                             os.remove('/apps/'+apps[selected]+'/'+i)
#                         os.rmdir('/apps/'+apps[selected])
#                         appstore()
#             appstore()

#         display.rect(1, 11+10*selected, 238, 10, st7789.RED)

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

def start_app(filename):
    global drawstats
    #TODO add app security here
    drawstats = False
    execfile(filename)
    drawstats = True

#TODO Need to fix after we switched to the lv.obj tactic. DONE!
def app_menu():
    global alscreen, appslist
    apps = []
    dircontents = os.listdir('/apps')
    
    appslist.clean()
    
    def startappcb(event):
        code = event.get_code()
        obj = event.get_target()
        if code == lv.EVENT.PRESSED:
            filename = '/apps/'+apps[obj.get_index()]+'main.py'
            start_app(filename)
            app_menu()
            
    def exitmenu(event):
        code = event.get_code()
        if code == lv.EVENT.PRESSED:
            redrawcanvas()

    exitbutton=appslist.add_button('exitbutton', '< Exit Menu')
    exitbutton.add_event_cb(exitmenu, lv.EVENT.ALL, None)
    for i in dircontents:
        appbutton=appslist.add_button('applistelement', i)
        appbutton.add_event_cb(startappcb, lv.EVENT.ALL, None)
        apps.append(i)

    lv.screen_load_anim(alscreen, lv.SCR_LOAD_ANIM.FADE_IN, 150, 0, False)

#     while True:
#         time.sleep(0.15)
#         
#         if pressed():
#             execfile('/apps/'+apps[selectedapp]+'/main.py')
#             app_menu()
# 
#         if up():
#             print(selectedapp)
#             updateapps()
#             selectedapp -= 1
# 
#         if down():
#             print(selectedapp)
#             updateapps()
#             selectedapp += 1
# 
#         if left():
#             break
# 
#         if selectedapp >= appamount:
#             updateapps()
#             selectedapp = 0
#         if selectedapp < 0:
#             updateapps()
#             selectedapp = appamount-1
# 
#         display.rect(5, 10 * selectedapp, 230, 10, st7789.RED)

def savesettings():
    global osversion, TIMEZONE, ssid, passwd, netstat
    settingsfile = "OSversion:"+osversion+"\ntimezone:"+str(TIMEZONE)+'\nbrightness:'+str(round(display.get_backlight()))
    networkfile = "netname:"+ssid+"\nnetpass:"+passwd+"\nnetstat:"+netstat
    file = open('/system/systemsettings.txt', 'w')
    file.write(settingsfile)
    file.close()
    file = open('/system/networkConfig.txt', 'w')
    file.write(networkfile)
    file.close()
    print('Settings saved')

def encodestring(e):
    tobeencoded=e
    encodedchars = []
    for i in tobeencoded:
        encodedchars.append(i+string.printable[random.randint(0, 95)])
    encodedchars.reverse()
    encoded=''
    for i in encodedchars:
        encoded+=i
    return encoded

def decodestring(d):
    todecode = d
    todecode = todecode[::2]
    todecode = list(todecode)
    todecode.reverse()
    decoded = ''
    for i in todecode:
        decoded+=i
    return decoded

def startnewthread(function, params):
    return threading.start_new_thread(function, params)

# The function that is run in background to ensure the top bar is always up-to-date
def topbarrefresh(t):
    global drawstats
    if drawstats == True:
        redrawtopbar()

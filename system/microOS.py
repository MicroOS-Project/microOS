# Micro OS
# A PROJECT TO CREATE AN OPERATING SYSTEM FOR MICROCONTROLLERS

#TODO Fix contexts to make everything more secure

os.chdir('/system')

sta_if = network.WLAN(network.STA_IF)

ssid = ''
passwd = ''

networks = []

selectedsetting = 0

letters = ('1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','[',']','\\',';','',"'",',',' ',' ',' ','/','.',' ',' ')

lettersupper = ('!','@','#','$','%','^','&','*','(',')','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','{','}','|',':','','"','<',' ',' ',' ','?','>',' ',' ')

nums = ['1','2','3','4','5','6','7','8','9','0','.','-','+','','/','*','=','C']

apps=[]
links=[]

tasks = []

log('Variables defined')

#TODO Improve this system
def do_connect(name, password):
    global netstat, ssid
    if not sta_if.isconnected():
        print('Connecting to network...')
        sta_if.active(True)
        sta_if.connect(name, password)
        while not sta_if.isconnected():
            if left():
                sta_if.active(False)
                netstat = "off"
                break
        ssid = name
    log('Connected to network')
#    ntptime.settime()
#    log('NTP time set')
    print('network config:', sta_if.ifconfig())

execfile('functions.py')

# Define settings here because otherwise WiFi would raise an error when we try to do anything with it.
# Settings is converted to LVGL

# def redrawwifi():
#     display.fill(0)
#     display.text(font, 'Network', 92, 1)
#     display.text(font, 'Wi-Fi status', 2, 20)
#     # Draw the ON/OFF switch
#     display.fill_circle(150, 24, 6, st7789.WHITE)
#     display.fill_circle(145, 24, 6, st7789.WHITE)
#     if netstat == 'on':
#         display.fill_circle(150, 24, 5, st7789.BLUE)
#     else:
#         display.fill_circle(145, 24, 5, st7789.BLUE)
# 
#     if sta_if.isconnected():
#         display.text(font, 'Network:        '+split_string(ssid, 10)[0]+'...', 2, 35)
#     else:
#         display.text(font, 'Networks  >', 2, 35)
#     selectedsetting = 0

def switchcb(event):
    global netstat
    code = event.get_code()
    if code == lv.EVENT.VALUE_CHANGED:
        state = s.get_state()
        if state == 51:
            netstat = 'off'
            sta_if.active(False)
        elif state == 50:
            netstat = 'on'
            do_connect(ssid, passwd)

#     if pressed():
#         passwd = keyboard()
#         display.fill(0)
#         display.text(font, 'Connecting to network:', round(width/2-22*8/2), round(height/2)-4)
#         display.text(font, networks[selectedsetting], round(width/2-(len(networks[selectedsetting])/2*8)), round(height/2-4+10))
#         ssid = networks[selectedsetting]
#         netstat="on"
#         do_connect(ssid, passwd)
#         savesettings()
#         redrawwifi()
#         break

def checkconnected(t):
    if sta_if.isconnected():
        t.delete()
        settings()
    else:
        log('Connecting Wifi...')

def connectnetcb(event):
    global ssid, passwd, netname, netstat, password, connectingscreen, connectinglabel, ct
    connectinglabel.set_text('Connecting to '+netname)
    passwd = password.get_text()
    lv.screen_load(connectingscreen)
#     do_connect(netname, passwd)
    sta_if.active(True)
    sta_if.connect(netname, passwd)
    netstat = 'on'
    ssid = netname
    ct = lv.timer_create(checkconnected, 500, None)
    savesettings()

def getpasscb(event):
    global networks, ssid, passwd, netname, password, getpassscreen
    code = event.get_code()
    obj = event.get_target_obj()
    index = obj.get_index()-1
    netname = networks[index]
    del networks
#     password.clean()
    lv.screen_load_anim(getpassscreen, lv.SCR_LOAD_ANIM.FADE_IN, 150, 0, False)

def leavenetslistcb(event):
    code = event.get_code()
    if code == lv.EVENT.PRESSED:
        settings()

def netslist():
    global networks, wifilistscreen, wifilistlist, scanningscreen
    
    netsammount = 0
    
#    lv.screen_load(scanningscreen)

    sta_if.active(True)
    nets = sta_if.scan()
    sta_if.active(False)
    networks = []
    
    # You can utilize a lv.timer_create here to make an auto-refresh here. Just make sure to delete it afterwards!

    networkslist.clean()
    
    leavenetslistbtn = networkslist.add_button('exit button', '< Back')
    leavenetslistbtn.add_event_cb(leavenetslistcb, lv.EVENT.ALL, None)
    
    for i in nets:
        if i[0] != b'':
            netlistitem = networkslist.add_button('network list item', i[0].decode('utf-8'))
            netlistitem.add_event_cb(getpasscb, lv.EVENT.PRESSED, None)
            networks.append(i[0].decode('utf-8'))
            netsammount += 1

    if netsammount == 0:
        nonetslabel=networkslist.add_text('No Networks Found')
        nonetslabel.center()
    
    lv.screen_load_anim(wifilistscreen, lv.SCR_LOAD_ANIM.FADE_IN, 150, 0, False)

def netslistcb(event):
    code = event.get_code()
    if code == lv.EVENT.PRESSED:
        netslist()

def wifimenu():
    global wifimenulist, wifimenuscreen, netstat
    
    wifimenulist.clean()
    
    backbtn = wifimenulist.add_button('backbtn', '< Back')
    backbtn.add_event_cb(opensettings, lv.EVENT.ALL, None)
    
    netstatlabel = wifimenulist.add_text('WiFi Status: ')
    netstatswitch = lv.switch(wifimenuscreen)
    netstatswitch.set_size(30, 15)
    netstatswitch.set_pos(width-35, 40) # TODO Make this an actual floating position
    if netstat == 'on':
        netstatswitch.add_state(lv.STATE.CHECKED)
    else:
        if netstatswitch.has_state(lv.STATE.CHECKED):
            netstatswitch.clear_state(lv.STATE.CHECKED)
    # netstatswitch.add_event_cb(, lv.EVENT.VALUE_CHANGED, None)
    
    if sta_if.isconnected():
        netslistbtn = wifimenulist.add_button('network name', 'Network:        '+ssid)
    else:
        netslistbtn = wifimenulist.add_button('networks list', 'Networks  >')

    netslistbtn.add_event_cb(netslistcb, lv.EVENT.ALL, None)

    lv.screen_load_anim(wifimenuscreen, lv.SCR_LOAD_ANIM.FADE_IN, 150, 0, False)

def wifimenucb(event):
    wifimenu()

def osinfomenu():
    global infolist, infoscreen
    def exitlist(event):
        global leaveosinfo
        code = event.get_code()
        if code == lv.EVENT.PRESSED:
            settings()
    
    infolist.clean()
    leave = infolist.add_button('exit', '< Back')
    leave.add_event_cb(exitlist, lv.EVENT.ALL, None)
    infolist.add_text('OS Version: '+osversion)
    infolist.add_text('\nPlatform: '+sys.platform)
    infolist.add_text('\nFirmware Version: '+os.uname().release)
    memfree = gc.mem_free()
    divisor = (1000000, 'MB')
    infolist.add_text('\nFree RAM: '+str(round(memfree/divisor[0], 2))+divisor[1])
    ip = sta_if.ifconfig()[0]
    if not ip == '0.0.0.0':
        infolist.add_text('\nIP Address: '+ip)

    lv.screen_load_anim(infoscreen, lv.SCR_LOAD_ANIM.FADE_IN, 150, 0, False)

def osinfocb(event):
    osinfomenu()

def checkforupdate():
    #TODO Actually check for updates here
    print('check for update here')

def checkupdatecb(event):
    checkforupdate()
    settings()

def shutdown():
    screen = lv.screen_active()
    screen.clean()
    #TODO Put wake up method here
    machine.deepsleep()

def shutdowncb(event):
    shutdown()

def leavesettingscb(event):
    redrawcanvas()

def changebrightness(event):
    global brightnessscreen, brightnessslider
    brightnessslider.set_value(round(display.get_backlight()/2), 0)
    lv.screen_load_anim(brightnessscreen, lv.SCR_LOAD_ANIM.FADE_IN, 150, 0, False)

def timezonecb(event):
    global timezonescreen, timezoneinput
    timezoneinput.set_text(str(TIMEZONE))
    lv.screen_load_anim(timezonescreen, lv.SCR_LOAD_ANIM.FADE_IN, 150, 0, False)

def settings():
    global netstat, ssid, passwd, settingsscreen, optionslist

    optionslist.clean()

    backbutton = optionslist.add_button('back button', 'Back')
    backbutton.add_event_cb(leavesettingscb, lv.EVENT.PRESSED, None)
    
    wifibutton = optionslist.add_button('wifi button', 'WiFi  >')
    wifibutton.add_event_cb(wifimenucb, lv.EVENT.PRESSED, None)

    osinfobutton = optionslist.add_button('info button', 'Device Info  >')
    osinfobutton.add_event_cb(osinfocb, lv.EVENT.PRESSED, None)
    
    brightnessbutton = optionslist.add_button('brightness', 'Display Brightness  >')
    brightnessbutton.add_event_cb(changebrightness, lv.EVENT.PRESSED, None)

    timebutton = optionslist.add_button('timezone', 'Set Timezone  >')
    timebutton.add_event_cb(timezonecb, lv.EVENT.PRESSED, None)
    
    volumebutton = optionslist.add_button('volume', 'Adjust Volume  >')
    # TODO Complete these buttons ^^^

    if sta_if.isconnected():
        checkupdatebtn = optionslist.add_button('update button', 'Check For Updates')
        checkupdatebtn.add_event_cb(checkupdatecb, lv.EVENT.PRESSED, None)

    # TODO Make this instead go to a popup menu of "Shutdown", "Reboot", or maybe even "Reboot Into Bootloader"
    shutdownbtn = optionslist.add_button('shutdown btn', 'Shutdown')
    shutdownbtn.add_event_cb(shutdowncb, lv.EVENT.PRESSED, None)

    lv.screen_load_anim(settingsscreen, lv.SCR_LOAD_ANIM.FADE_IN, 150, 0, False)

# TODO Make the screensaver work again

#     while True:
#         time.sleep(0.15)
#         if left():
#             timepassed=0
#             break
#         if down():
#             timepassed=0
#             selectedsetting +=1
#             updatesettings()
#         if up():
#             timepassed=0
#             selectedsetting -=1
#             updatesettings()
#         if pressed():
#             timepassed=0
#             if selectedsetting == 0:
#                 # WiFi Menu
#                 redrawwifi()
#                 while True:
#                     time.sleep(0.15)
#                     if left():
#                         break
#                     if down():
#                         selectedsetting += 1
#                         updatesettings()
#                     if up():
#                         selectedsetting -= 1
#                         updatesettings()
#                     if pressed():
#                         if selectedsetting == 0:
#                             if netstat == 'on':
#                                 netstat = "off"
#                                 sta_if.active(False)
#                                 redrawwifi()
#                             else:
#                                 netstat = "on"
#                                 do_connect(ssid, passwd)
#                                 redrawwifi()
#                         if selectedsetting == 1:
#                             display.fill(0)
#                             netlistdown=21
#                             sta_if.active(True)
#                             display.text(font, 'Scanning...', round(width/2-44), round(height/2-4))
#                             nets=sta_if.scan()
#                             netsammount=0
#                             display.fill(0)
#                             display.text(font, 'Networks', 88, 1)
#                             selectedsetting = 0
#                             for i in nets:
#                                 if i[0] != b'':
#                                     display.text(font, i[0], 2, netlistdown)
#                                     networks.append(i[0].decode('utf-8'))
#                                     netlistdown+=15
#                                     netsammount += 1
#                             print(networks)
#                             if netsammount == 0:
#                                 display.text(font, 'No Networks Found', round(width/2-19*8/2), round(height/2-4))
#                                 while True:
#                                     time.sleep(0.15)
#                                     if left():
#                                         redrawwifi()
#                                         break
#                             else:
#                                 # Select network
#                                 display.rect(1, 19+(selectedsetting*15), width-2, 12, st7789.WHITE)
#                                 while True:
#                                     time.sleep(0.15)
#                                     if left():
#                                         redrawwifi()
#                                         break
#                                     if up():
#                                         selectedsetting-=1
#                                         updatesettings()
#                                         display.rect(1, 19+(selectedsetting*15), width-2, 12, st7789.WHITE)
#                                     if down():
#                                         selectedsetting+=1
#                                         updatesettings()
#                                         display.rect(1, 19+(selectedsetting*15), width-2, 12, st7789.WHITE)
#                                     if pressed():
#                                         passwd = keyboard()
#                                         display.fill(0)
#                                         display.text(font, 'Connecting to network:', round(width/2-22*8/2), round(height/2)-4)
#                                         display.text(font, networks[selectedsetting], round(width/2-(len(networks[selectedsetting])/2*8)), round(height/2-4+10))
#                                         ssid = networks[selectedsetting]
#                                         netstat="on"
#                                         do_connect(ssid, passwd)
#                                         savesettings()
#                                         redrawwifi()
#                                         break
# 
#                                     if selectedsetting < 0:
#                                         selectedsetting = netsammount
#                                         updatesettings()
#                                         display.rect(1, 19+(selectedsetting*15), width-2, 12, st7789.WHITE)
#                                     if selectedsetting > netsammount:
#                                         selectedsetting = 0
#                                         updatesettings()
#                                         display.rect(1, 19+(selectedsetting*15), width-2, 12, st7789.WHITE)
#                                     
#                             selectedsetting=0
# 
#                     if selectedsetting < 0:
#                         timepassed=0
#                         selectedsetting = 2
# 
#                     if selectedsetting > 2:
#                         timepassed=0
#                         selectedsetting = 0
#                     display.rect(1, 19+(selectedsetting*15), width-2, 12, st7789.WHITE)
# 
#                 settings()
#             if selectedsetting == 1:
#                 display.fill(st7789.BLACK)
#                 display.text(font, '           OS Info', 2, 2) 
#                 display.text(font, 'OS Version: '+osversion, 2, 20)
#                 display.text(font, 'Platform: '+sys.platform, 2, 35)
#                 display.text(font, 'Firmware: '+os.uname().release, 2, 50)
#                 ip = sta_if.ifconfig()[0]
#                 if not ip == '0.0.0.0':
#                     display.text(font, 'IP Address: '+ip, 2, 65)
#                 while True:
#                     time.sleep(0.15)
#                     if left():
#                         break
#                 settings()
#             if selectedsetting == 2:
#                 if sta_if.isconnected():
#                     print('check for updates')
#                 else:
#                     display.off()
#                     sys.exit()
#             if selectedsetting == 3:
#                 display.off()
#                 sys.exit()
# 
#         if selectedsetting < 0:
#             timepassed=0
#             if sta_if.isconnected():            
#                 selectedsetting = 3
#             else:
#                 selectedsetting = 2
#             
#         if selectedsetting > 2:
#             timepassed=0
#             if sta_if.isconnected() and selectedsetting > 3:
#                 selectedsetting = 0
#             elif not sta_if.isconnected():
#                 selectedsetting = 0
# 
#         display.rect(1, 19+(selectedsetting*15), width-2, 12, st7789.WHITE)
#                 
#         if timepassed >= 400:
#             screensaver()
#             break
#             timepassed=0
# 
#         timepassed += 1  

log('functions defined')

bootscreen = lv.obj()

microoswords(bootscreen)

netstat = ''

#retrieve settings
log('Retrieving settings values')

with open('systemsettings.txt') as file:
    for line in file:
        line = line.rstrip('\n')
        current_setting = line.split(':')
        sv = current_setting[1]
        sn = current_setting[0]
        if sn == 'OSversion':
            osversion = sv.strip()
        elif sn == 'timezone':
            TIMEZONE = int(sv.strip())
        elif sn == 'brightness':
            display.set_backlight(int(sv.strip()))

versioncharlen = len('Version '+ osversion)
versionlabel = lv.label(bootscreen)
versionlabel.set_text('Version ' + osversion)
versionlabel.align(lv.ALIGN.CENTER, 0, 80)

lv.screen_load(bootscreen)

# network settings:
with open('/system/networkConfig.txt') as file:
    for line in file:
        line = line.rstrip('\n')
        currentline = line.split(':', 1)
        n = currentline[0]
        v = currentline[1]
        
        if n == 'stat':
            netstat = v.strip()
            
        elif n == 'name':
            ssid = v.strip()
            
        elif n == 'pass':
            passwd = v.strip()

if netstat == 'on':
    do_connect(ssid, passwd)

time.sleep(2.5)

del versionlabel

# menu:
selected = 0

initscreens()

redrawcanvas()

drawtopbar()

del bootscreen

#over = 1

cycles = 0
timepassed = 0

os.chdir('/')

#startnewthread(topbarrefresher, ())

topbartimer = lv.timer_create(topbarrefresh, 1000, None)

# TODO Make the screensaver work again

# while True:
#     time.sleep(0.15)
#     display.rect(9, 168, 64, 68, st7789.BLACK)
#     display.rect(9+1*80, 168, 64, 68, st7789.BLACK)
#     display.rect(6+2*80, 168, 64, 68, st7789.BLACK)
#     if (over == 1):
#         display.rect(9+0*80, 168, 64, 68, st7789.RED)
#         
#     if (over == 2):
#         display.rect(9+1*80, 168, 64, 68, st7789.RED)
#         
#     if (over == 3):
#         display.rect(6+2*80, 168, 64, 68, st7789.RED)
#         
#     if right():
#         timepassed=0
#         over+=1
#     if left():
#         timepassed=0
#         over-=1
#         
#     if pressed():
#         timepassed=0
#         if over == 1:
#             log('Select app')
#             app_menu()
#             redrawcanvas()
#         if over == 2:
#             log('Settings')
#             settings()
#             redrawcanvas()
#         if over == 3:
#             log('App store')
#             appstorecheck()
#             redrawcanvas()
#  
#     if (over>3):
#         over=1
#         
#     if (over<1):
#         over=3
# 
#     if cycles == 6:
#         drawtopbar()
#         cycles = 0
#         
#     if timepassed >= 400:
#         screensaver()
#         timepassed=0
#         
#     cycles += 1
#     timepassed += 1

log('Erasing /tmp directory')

# Erase /tmp dir so it's ready for the next run (Not yet needed but I put it here anyway)
for filename in os.listdir('/tmp'):
    os.remove(filename)
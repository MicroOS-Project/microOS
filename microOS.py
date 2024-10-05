# MicroOS A PROJECT TO CREATE AN OPERATING SYSTEM FOR MICROCONTROLLERS



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



log('Variables defined')



def do_connect(name, password):

    if not sta_if.isconnected():

        print('Connecting to network...')

        sta_if.active(True)

        sta_if.connect(name, password)

        while not sta_if.isconnected():

            if xa.read() <= minval:

                sta_if.active(False)

                exec('netstat = "off"')

                break

    print('network config:', sta_if.ifconfig())



execfile('functions.py')



#define settings here because otherwise WiFi would get an error when we try to do anything with it.



def updatesettings():

    for i in range(0, 24):

        display.rect(1, 19+(15*i), 238, 12, st7789.BLACK)

        

def redrawwifi():

    display.fill(0)

    display.text(font, '           Network', 0, 1)

    display.text(font, 'SSID     '+ssid+'  >', 2, 20)

    displaypass=''

    for i in range(0, len(passwd)):

        displaypass += '*'

    display.text(font, 'Password  '+displaypass, 2, 35)

    selectedsetting = 0



def settings():

    display.fill(st7789.BLACK)

    

    display.text(font, '           Settings', 0, 1)



    display.text(font, 'Wi-Fi     '+netstat+'  >', 2, 20)

    display.text(font, 'OS Info  >', 2, 35)

    if sta_if.isconnected():

        display.text(font, 'Check For Updates', 2, 50)

        display.text(font, 'Shut Down', 2, 65)

    else:

        display.text(font, 'Shut Down', 2, 50)



    selectedsetting = 0

    

    timepassed=0

    

    networks=[]

    

    while True:

        time.sleep(0.15)

        if xa.read() < minval:

            timepassed=0

            exec('settingsfile = "netname:"+ssid+"\\nnetpass:"+passwd+"\\nnetstat:"+netstat+"\\nOSversion:"+osversion')

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

                redrawwifi()

                while True:

                    time.sleep(0.15)

                    if xa.read() <= minval:

                        break

                    if ya.read() >= maxval:

                        selectedsetting += 1

                        updatesettings()

                    if ya.read() <= minval:

                        selectedsetting -= 1

                        updatesettings()

                    if btn.value() == 0:

                        if selectedsetting == 0:

                            display.fill(0)

                            netlistdown=2

                            sta_if.active(True)

                            display.text(font, 'Scanning...', 76, 115)

                            nets=sta_if.scan()

                            print(nets)

                            netsammount=0

                            display.fill(0)

                            selectedsetting = 0

                            for i in nets:

                                if i[0] != b'':

                                    display.text(font, i[0], 2, netlistdown)

                                    print(i[0].decode('utf-8'))

                                    networks += i[0].decode('utf-8')

                                    netlistdown+=15

                                    netsammount += 1

                            print(networks)

                            sta_if.active(False)

                            if netsammount == 0:

                                display.text(font, 'No Networks Found', 52, 116)

                            else:

                                display.rect(1, 1+(selectedsetting*15), 238, 12, st7789.WHITE)

                                while True:

                                    time.sleep(0.15)

                                    if xa.read() <= minval:

                                        redrawwifi()

                                        break

                                    if ya.read() <= minval:

                                        selectedsetting-=1

                                        updatesettings()

                                        display.rect(1, 1+(selectedsetting*15), 238, 12, st7789.WHITE)

                                    if ya.read() >= maxval:

                                        selectedsetting+=1

                                        updatesettings()

                                        display.rect(1, 1+(selectedsetting*15), 238, 12, st7789.WHITE)

                                        

                                    if btn.value() == 0:

                                        passwd = keyboard()

                                        display.fill(0)

                                        display.text(font, 'Connecting to network:', 32, 116)

                                        display.text(font, networks[selectedsetting], round(240-((len(networks[selectedsetting])/2)*8)), 126)

                                        exec('ssid = networks[selectedsetting]')

                                        exec('netstat="on"')

                                        do_connect(ssid, passwd)

                                        redrawwifi()

                                        break

                                    

                                    if selectedsetting < 0:

                                        selectedsetting = netsammount

                                        updatesettings()

                                        display.rect(1, 1+(selectedsetting*15), 238, 12, st7789.WHITE)

                                    if selectedsetting > netsammount:

                                        selectedsetting = 0

                                        updatesettings()

                                        display.rect(1, 1+(selectedsetting*15), 238, 12, st7789.WHITE)

                                    

                            selectedsetting=0



#                 if netstat == 'off':

#                     exec("netstat = ' on'")

#                     display.fill(0)

#                     display.text(font, 'Connecting to network:', 10, 100)

#                     display.text(font, ssid, 10, 115)

#                     do_connect(ssid, passwd)

#                     settings()

#                 elif netstat == 'on':

#                     exec("netstat = 'off'")

#                     sta_if.disconnect()

#                     sta_if.active(False)

#                     display.text(font, 'WiFi Stat:  '+netstat, 2, 20)

#             if selectedsetting == 1:

#                 exec('ssid = keyboard()')

#                 settings()

#             if selectedsetting == 2:

#                 exec('passwd = keyboard()')

#                 settings()

                    if selectedsetting < 0:

                        timepassed=0

                        selectedsetting = 2



                    if selectedsetting > 2:

                        timepassed=0

                        selectedsetting = 0

                    display.rect(1, 19+(selectedsetting*15), 238, 12, st7789.WHITE)



                settings()

            if selectedsetting == 1:

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

            if selectedsetting == 2:

                if sta_if.isconnected():

                    print('check for updates')

                else:

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

            break

            timepassed=0



        timepassed += 1        



log('functions defined')



display.fill(0)



microoswords()



netstat = ''



#retrieve settings



log('Retrieving settings values')



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



log('Starting main loop')



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



log('Current time is '+str(hour)+':'+str(curtime[4]))



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

            log('Select app')

            app_menu()

            redrawcanvas()

        if over == 2:

            log('Settings')

            settings()

            redrawcanvas()

        if over == 3:

            log('App store')

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



log('Erasing flash')

#erase /tmp dir so it's ready for the next run

for filename in os.listdir('/tmp'):

    os.remove(filename)
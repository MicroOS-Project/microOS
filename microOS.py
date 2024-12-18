# Micro OS

# A PROJECT TO CREATE AN OPERATING SYSTEM FOR MICROCONTROLLERS



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

            if left():

                sta_if.active(False)

                exec('netstat = "off"')

                break

    print('network config:', sta_if.ifconfig())



execfile('functions.py')



#define settings here because otherwise WiFi would raise an error when we try to do anything with it.



def updatesettings():

    for i in range(0, round(height/10, 0)):

        display.rect(1, 19+(15*i), width-2, 12, st7789.BLACK)

        

def redrawwifi():

    display.fill(0)

    display.text(font, 'Network', 92, 1)

    display.text(font, 'Wi-Fi status', 2, 20)

    # Draw the ON/OFF switch

    display.fill_circle(150, 24, 6, st7789.WHITE)

    display.fill_circle(145, 24, 6, st7789.WHITE)

    if netstat == 'on':

        display.fill_circle(150, 24, 5, st7789.BLUE)

    else:

        display.fill_circle(145, 24, 5, st7789.BLUE)



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

    

    while True:

        time.sleep(0.15)

        if left():

            timepassed=0

            break

        if down():

            timepassed=0

            selectedsetting +=1

            updatesettings()

        if up():

            timepassed=0

            selectedsetting -=1

            updatesettings()

        if pressed():

            timepassed=0

            if selectedsetting == 0:

                # WiFi Menu

                redrawwifi()

                while True:

                    time.sleep(0.15)

                    if left():

                        break

                    if down():

                        selectedsetting += 1

                        updatesettings()

                    if up():

                        selectedsetting -= 1

                        updatesettings()

                    if pressed():

                        if selectedsetting == 0:

                            display.fill(0)

                            netlistdown=2

                            sta_if.active(True)

                            display.text(font, 'Scanning...', round(width/2-44), round(height/2-4))

                            nets=sta_if.scan()

                            netsammount=0

                            display.fill(0)

                            selectedsetting = 0

                            for i in nets:

                                if i[0] != b'':

                                    display.text(font, i[0], 2, netlistdown)

                                    networks.append(i[0].decode('utf-8'))

                                    netlistdown+=12

                                    netsammount += 1

                            print(networks)

                            if netsammount == 0:

                                display.text(font, 'No Networks Found', round(width/2-19*8/2), round(height/2-4))

                            else:

                                # Select network

                                display.rect(1, 1+(selectedsetting*12), width-2, 12, st7789.WHITE)

                                while True:

                                    time.sleep(0.15)

                                    if left():

                                        redrawwifi()

                                        break

                                    if up():

                                        selectedsetting-=1

                                        updatesettings()

                                        display.rect(1, 1+(selectedsetting*12), width-2, 12, st7789.WHITE)

                                    if down():

                                        selectedsetting+=1

                                        updatesettings()

                                        display.rect(1, 1+(selectedsetting*12), width-2, 12, st7789.WHITE)

                                        

                                    if pressed():

                                        passwd = keyboard()

                                        display.fill(0)

                                        display.text(font, 'Connecting to network:', round(width/2-22*8/2), round(height/2)-4)

                                        display.text(font, networks[selectedsetting], round(width/2-(len(networks[selectedsetting])/2*8)), round(height/2-4+10))

                                        exec('ssid = networks[selectedsetting]')

                                        exec('netstat="on"')

                                        do_connect(ssid, passwd)

                                        savesettings()

                                        redrawwifi()

                                        break



                                    if selectedsetting < 0:

                                        selectedsetting = netsammount

                                        updatesettings()

                                        display.rect(1, 1+(selectedsetting*12), width-2, 12, st7789.WHITE)

                                    if selectedsetting > netsammount:

                                        selectedsetting = 0

                                        updatesettings()

                                        display.rect(1, 1+(selectedsetting*12), width-2, 12, st7789.WHITE)

                                    

                            selectedsetting=0



                    if selectedsetting < 0:

                        timepassed=0

                        selectedsetting = 2



                    if selectedsetting > 2:

                        timepassed=0

                        selectedsetting = 0

                    display.rect(1, 19+(selectedsetting*15), width-2, 12, st7789.WHITE)



                settings()

            if selectedsetting == 1:

                display.fill(st7789.BLACK)

                display.text(font, '           OS Info', 2, 2) 

                display.text(font, 'OS Version: '+osversion, 2, 20)

                display.text(font, 'Platform: '+sys.platform, 2, 35)

                display.text(font, 'Firmware: '+os.uname().release, 2, 50)

                ip = sta_if.ifconfig()[0]

                if ip == '0.0.0.0':

                    display.text(font, 'IP Address: '+ip, 2, 65)

                while True:

                    time.sleep(0.15)

                    if left():

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





        display.rect(1, 19+(selectedsetting*15), width-2, 12, st7789.WHITE)

                

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

#         if sn == 'netname':

#             ssid = sv.split('\r')[0]

#             

#         if sn == 'netpass':

#             passwd = sv.split('\r')[0]

#             

#         if sn == 'netstat':

#             netstat = sv.split('\r')[0]



        if sn == 'OSversion':

            osversion = sv.split('\r')[0]



versioncharlen = len('Version '+ osversion)

display.text(font, 'Version ' + osversion, round(width/2-versioncharlen*8/2), 190)

time.sleep(2.5)



# network settings:

with open('/system/networkConfig.txt') as file:

    for line in file:

        line = line.rstrip('\n')

        currentline = line.split(':', 1)

        ln = currentline[0]

        lv = currentline[1]

        

        if ln == 'stat':

            netstat = lv.strip('\r')

            

        elif ln == 'name':

            ssid = lv.strip('\r')

            

        elif ln == 'pass':

            passwd = lv.strip('\r')



if netstat == 'on':

    do_connect(ssid, passwd)



display.fill(st7789.BLACK)



log('Starting main loop')



# menu:

selected = 0



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

        

    if right():

        timepassed=0

        over+=1

    if left():

        timepassed=0

        over-=1

        

    if pressed():

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



log('Erasing /tmp directory')

#erase /tmp dir so it's ready for the next run

for filename in os.listdir('/tmp'):

    os.remove(filename)
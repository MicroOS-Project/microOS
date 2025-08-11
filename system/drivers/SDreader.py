import sdcard

sdspi=machine.SoftSPI(-1, sck=machine.Pin(40), mosi=machine.Pin(41), miso=machine.Pin(38, machine.Pin.IN))
sd = sdcard.SDCard(sdspi, machine.Pin(39))
os.mount(sd, '/sd')
print('SD card mounted.')
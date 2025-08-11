import sdcard

try:
    sdspi=machine.SoftSPI(-1, sck=machine.Pin(18), mosi=machine.Pin(23), miso=machine.Pin(19))
    sd = sdcard.SDCard(sdspi, machine.Pin(5))
    os.mount(sd, '/sd')
    print('SD card mounted.')
except Exception as e:
    print('No SD card present.')
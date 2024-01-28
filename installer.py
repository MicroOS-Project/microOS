def do_connect(name, password):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(name, password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

do_connect('netname','netpass')

from sys import path

path.append('/system')

import mip

mip.install('github:Respite09/microOS', target='/system')

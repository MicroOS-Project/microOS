xa = machine.ADC(machine.Pin(36))
ya = machine.ADC(machine.Pin(39))
btn = machine.Pin(32, machine.Pin.IN, machine.Pin.PULL_UP)

xa.atten(xa.ATTN_11DB)
ya.atten(ya.ATTN_11DB)

minval = const(500)
maxval = const(2500)

def left():
    return xa.read()<=minval

def right():
    return xa.read()>=maxval

def up():
    return ya.read()<=minval

def down():
    return ya.read()>=maxval

def pressed():
    return btn.value()==0
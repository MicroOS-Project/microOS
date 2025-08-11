from machine import Pin

tb_up = Pin(3, mode=Pin.IN, pull=Pin.PULL_UP)
tb_down = Pin(15, mode=Pin.IN, pull=Pin.PULL_UP)
tb_left = Pin(1, mode=Pin.IN, pull=Pin.PULL_UP)
tb_right = Pin(2, mode=Pin.IN, pull=Pin.PULL_UP)
tb_click = Pin(0, mode=Pin.IN, pull=Pin.PULL_UP)
tb_up_value = tb_up.value()
tb_down_value = tb_down.value()
tb_left_value = tb_left.value()
tb_right_value = tb_right.value()

def left():
    global tb_left_value
    if tb_left.value() != tb_left_value:
        tb_left_value = tb_left.value()
        return True
    else:
        return False

def right():
    global tb_right_value
    if tb_right.value() != tb_right_value:
        tb_right_value = tb_right.value()
        return True
    else:
        return False

def up():
    global tb_up_value
    if tb_up.value() != tb_up_value:
        tb_up_value = tb_up.value()
        return True
    else:
        return False

def down():
    global tb_down_value
    if tb_down.value() != tb_down_value:
        tb_down_value = tb_down.value()
        return True
    else:
        return False

def pressed():
    return not tb_click.value()
bat = machine.ADC(machine.Pin(4))
bat.width(machine.ADC.WIDTH_12BIT)
bat.atten(machine.ADC.ATTN_11DB)

voltagefull = 3.91
voltagecharging = 4.1

def readvoltage():
    return ((bat.read_u16() * 3.3) / 65535)/ (100/200)

def calcPercentage():
    voltage = readvoltage()
    diff = voltagefull-voltage
    if voltage >= voltagecharging:
        percent = 'CH'
    else:
        percent = str(100-round(diff/voltagefull*100))
    try:
        # Determines if the percentage is less than 10% and if so, log that the battery is low
        if int(percent) < 10:
            log('Battery is low! (Less than 10%)')
    except:
        # The percent is "CH" so it cannot convert to int and returns a error
        pass
    return percent
from machine import DAC, Pin
import time

dac = DAC(Pin(25))  # create an DAC object acting on a pin

def playsound(i, length, vol=255):
    for j in range(0, length):
        dac.write(0)
        time.sleep_us(i)
        dac.write(vol)
        time.sleep_us(i)
        
#         
# while True:
#     sound = int(input('value: '))
#     playsound(sound, 1000)
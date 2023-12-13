import lcd
import utime
import uos

from lcd import USE_HORIZONTAL

DC =  4
RES = 5
BLK = 12

ColorTab=['RED','GREEN','BLUE','YELLOW','BROWN']
Direction=['Rotation:0','Rotation:90','Rotation:180','Rotation:270']

mylcd = lcd.ST7789V(RES,DC,BLK)
mylcd.lcdinit()
import lcd_spi
from machine import Pin as GPIO
import utime

"""Define the size of the LCD"""
LCD_W = 240
LCD_H = 240

USE_HORIZONTAL=0 #Define the clockwise rotation direction of LCD screen:
                 #// 0-0 degree rotation, 1-90 degree rotation, 2-180 degree rotation, 3-270 degree rotation

# Initialize spi
myspi = lcd_spi.lcdspi()

class ST7789V(object):
    """class for ST7789V 240*240 1.3inch IPS SPI LCD module."""
    def __init__(self,res,dc,blk):
        # set lcd display parameter
        self.width = 0 #LCD width
        self.height = 0 #LCD height
        self.lcdid = 0  #LCD ID
        self.lcddir = 0 #LCD display direction
        self.wramcmd = 0x2C #Start writing gram instruction
        self.setxcmd = 0x2A #Set X coordinate command
        self.setycmd = 0x2B #Set Y coordinate command
        self.setdircmd = 0x36 #Set lcd display direction command
        self.xoffset = 0 #Set X coordinate offset
        self.yoffset = 0  #Set Y coordinate offset
        # Initialize oled pin
        self.lcdled = blk
        self.lcdrs = dc
        self.lcdrst = res
    def lcdledset(self):
        self.lcdledpin.value(True)
    def lcdledclr(self):
        self.lcdledpin.value(False)
    def lcdrsset(self):
        self.lcdrspin.value(True)
    def lcdrsclr(self):
        self.lcdrspin.value(False)
    def lcdrstset(self):
        self.lcdrstpin.value(True)
    def lcdrstclr(self):
        self.lcdrstpin.value(False)
    def lcdwrreg(self,value):
        self.lcdrsclr()
        myspi.spiwritebyte(value)
    def lcdwrdata(self,value):
        self.lcdrsset()
        myspi.spiwritebyte(value)
    def lcdwritereg(self,reg,value):
        self.lcdwrreg(reg)
        self.lcdwrdata(value)
    def lcdwriteram(self):
        self.lcdwrreg(self.wramcmd)
    def lcdwrite16bitdata(self,value):
        self.lcdrsset()
        myspi.spiwritebyte(value>>8)
        myspi.spiwritebyte(value)
    def lcdsetwindows(self,xstart,ystart,xend,yend):
        self.lcdwrreg(self.setxcmd)
        self.lcdwrdata((xstart+self.xoffset)>>8)
        self.lcdwrdata(xstart+self.xoffset)
        self.lcdwrdata((xend+self.xoffset)>>8)
        self.lcdwrdata(xend+self.xoffset)
        self.lcdwrreg(self.setycmd)
        self.lcdwrdata((ystart+self.yoffset)>>8)
        self.lcdwrdata(ystart+self.yoffset)
        self.lcdwrdata((yend+self.yoffset)>>8)
        self.lcdwrdata(yend+self.yoffset)
        self.lcdwriteram()
    def lcdsetcursor(self,xpos,ypos):
        self.lcdsetwindows(xpos,ypos,xpos,ypos)
    def lcddrawpoint(self,x,y,color):
        self.lcdsetcursor(x,y)
        self.lcdwrite16bitdata(color)
    def lcdclear(self,color):
        self.lcdsetwindows(0,0,self.width-1,self.height-1)
        self.lcdrsset()
        for i in range(0,self.height):
            for m in range(0,self.width):
                myspi.spiwritebyte(color>>8)
                myspi.spiwritebyte(color)
    def lcdgpioinit(self):
        self.lcdledpin=GPIO(self.lcdled,GPIO.OUT)
        self.lcdrspin=GPIO(self.lcdrs,GPIO.OUT)
        self.lcdrstpin=GPIO(self.lcdrst,GPIO.OUT)
    def lcdreset(self):
        self.lcdrstclr()
        utime.sleep(0.02)
        self.lcdrstset()
        utime.sleep(0.02)
    def lcddirection(self,value):
        if value == 0:
            self.width = LCD_W
            self.height = LCD_H
            self.xoffset = 0
            self.yoffset = 0
            self.lcdwritereg(self.setdircmd,0)
        elif value == 1:
            self.width = LCD_H
            self.height = LCD_W
            self.xoffset = 0
            self.yoffset = 0   
            self.lcdwritereg(self.setdircmd,(1 << 6)|(1 << 5))
        elif value == 2:
            self.width = LCD_W
            self.height = LCD_H
            self.xoffset = 0
            self.yoffset = 80      
            self.lcdwritereg(self.setdircmd,(1 << 6)|(1 << 7))
        elif value == 3:
            self.width = LCD_H
            self.height = LCD_W
            self.xoffset = 80
            self.yoffset = 0        
            self.lcdwritereg(self.setdircmd,(1 << 5)|(1 << 7))

    def lcdinit(self):
        self.lcdgpioinit() #LCD GPIO initialization
        self.lcdreset()    #LCD reset
        """init ST7789V"""        
        self.lcdwrreg(0x36); 
        self.lcdwrdata(0x00);
        self.lcdwrreg(0x3A); 
        self.lcdwrdata(0x05);
        self.lcdwrreg(0xB2);
        self.lcdwrdata(0x0C);
        self.lcdwrdata(0x0C);
        self.lcdwrdata(0x00);
        self.lcdwrdata(0x33);
        self.lcdwrdata(0x33);
        self.lcdwrreg(0xB7); 
        self.lcdwrdata(0x35);  
        self.lcdwrreg(0xBB);
        self.lcdwrdata(0x19);
        self.lcdwrreg(0xC0);
        self.lcdwrdata(0x2C);
        self.lcdwrreg(0xC2);
        self.lcdwrdata(0x01);
        self.lcdwrreg(0xC3);
        self.lcdwrdata(0x12);   
        self.lcdwrreg(0xC4);
        self.lcdwrdata(0x20);  
        self.lcdwrreg(0xC6); 
        self.lcdwrdata(0x0F);    
        self.lcdwrreg(0xD0); 
        self.lcdwrdata(0xA4);
        self.lcdwrdata(0xA1);
        self.lcdwrreg(0xE0);
        self.lcdwrdata(0xD0);
        self.lcdwrdata(0x04);
        self.lcdwrdata(0x0D);
        self.lcdwrdata(0x11);
        self.lcdwrdata(0x13);
        self.lcdwrdata(0x2B);
        self.lcdwrdata(0x3F);
        self.lcdwrdata(0x54);
        self.lcdwrdata(0x4C);
        self.lcdwrdata(0x18);
        self.lcdwrdata(0x0D);
        self.lcdwrdata(0x0B);
        self.lcdwrdata(0x1F);
        self.lcdwrdata(0x23);
        self.lcdwrreg(0xE1);
        self.lcdwrdata(0xD0);
        self.lcdwrdata(0x04);
        self.lcdwrdata(0x0C);
        self.lcdwrdata(0x11);
        self.lcdwrdata(0x13);
        self.lcdwrdata(0x2C);
        self.lcdwrdata(0x3F);
        self.lcdwrdata(0x44);
        self.lcdwrdata(0x51);
        self.lcdwrdata(0x2F);
        self.lcdwrdata(0x1F);
        self.lcdwrdata(0x1F);
        self.lcdwrdata(0x20);
        self.lcdwrdata(0x23);
        self.lcdwrreg(0x21); 
        self.lcdwrreg(0x11); 
        self.lcdwrreg(0x29); 
        self.lcddirection(USE_HORIZONTAL)
        self.lcdledset()
#        self.lcdclear(0xFFFF)

#would be image function
#     def lcdimage(self,image):
# 	"""set the value of Python Image Library to lcd GRAM"""
# 	imgwidth,imgheight = image.size
# 	if imgwidth != self.width or imgheight != self.height:
# 	    raise ValueError('Image must be same dimensions as display({0}x{1}).' .format(self.width, self.height))
# 	img = np.asarray(image)
#         pix = np.zeros((self.width,self.height,2), dtype = np.uint8)
#         pix[...,[0]] = np.add(np.bitwise_and(img[...,[0]],0xF8),np.right_shift(img[...,[1]],5))
#         pix[...,[1]] = np.add(np.bitwise_and(np.left_shift(img[...,[1]],3),0xE0),np.right_shift(img[...,[2]],3))
#         pix = pix.flatten().tolist()
# 	self.lcdsetwindows(0,0,imgwidth-1,imgheight-1)
#         self.lcdrsset()
# 	for i in range(0,len(pix),4096):
#             myspi.spi.writebytes(pix[i:i+4096])	

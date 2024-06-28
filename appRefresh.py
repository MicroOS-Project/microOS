class Canvas:
    def __init__(self, backcolor, n):
        self.n = n
        self.canvas = open('/tmp/canvas-'+str(self.n), 'w')
        self.canvas.write('display.fill('+str(backcolor)+')\n')
        display.fill(int(backcolor))

    def add_rect(self, x, y, w, h, color):
        self.canvas.write('display.rect('+str(x)+','+str(y)+','+str(w)+','+str(h)+','+str(color)+')\n')
        display.rect(x, y, w, h, color)

    def add_fill_rect(self, w, h, x, y, color):
        self.canvas.write('display.fill_rect('+str(x)+','+str(y)+','+str(w)+','+str(h)+','+str(color)+')\n')
        display.fill_rect(x, y, w, h, color)

    def add_line(self, x, y, x2, y2, color):
        self.canvas.write('display.line('+str(x)+','+str(y)+','+str(x2)+','+str(y2)+','+str(color)+')\n')
        display.line(x, y, x2, y2, color)

    def add_circle(self, r, x, y, color):
        self.canvas.write('display.circle('+str(r)+','+str(x)+','+str(y)+','+str(color)+')\n')
        display.circle(r, x, y, color)

    def add_fill_circle(self, r, x, y, color):
        self.canvas.write('display.fill_circle('+str(r)+','+str(x)+','+str(y)+','+str(color)+')\n')
        display.fill_circle(r, x, y, color)
        
    def add_jpg(self, file, x, y):
        self.canvas.write('display.jpg('+str(file)+','+str(x)+','+str(y)+')\n')
        display.jpg(file, x, y)
        
    def add_png(self, file, x, y):
        self.canvas.write('display.png('+str(file)+','+str(x)+','+str(y)+')\n')
        display.png(file, x, y)
        
#     def add_text(self, font, text, x, y, c=st7789.WHITE, bd=st7789.BLACK):
#         self.canvas.write('display.text('+str(font)+','+text+','+str(x)+','+str(y)+','+str(c)+','+str(bd)+')\n')
#         display.text(font, text, x, y, c, bd)
        
    def save(self):
        self.canvas.close()

    def redraw(self):
        try:
            execfile('/tmp/canvas-'+str(self.n))
        except:
            print('Error in canvas file!')
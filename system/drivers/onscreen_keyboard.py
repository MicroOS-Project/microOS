def numpad(textx=25, texty=10):
    def redraw():
        num = 0
        for i in range(0, 3):
            for n in range(0, 6):
                display.text(fontlarge, nums[num], 13+40*n, 130+34*i)
                num +=1
        for i in range(0, 3):
            for n in range(0, 6):
                display.rect(3+40*n, 130+34*i, 34, 30, st7789.BLUE)

    redraw()

    row = 0
    collum = 0

    entered = ''

    while True:
        time.sleep(0.25)
        display.rect(3+40*collum, 130+34*row, 34, 30, st7789.BLUE)
        if btn.value() == 0:
            if nums[row*6+collum] == '=':
                return entered
            elif nums[row*6+collum] == 'C':
                entered = ''
                display.fill_rect(11, texty, 220, 32, st7789.BLACK)
                display.text(fontlarge, entered, textx, texty, st7789.BLUE)
                print(entered)
            else:
                entered += nums[row*6+collum]
                display.fill_rect(11, texty, 220, 32, st7789.BLACK)
                display.text(fontlarge, entered, textx, texty, st7789.BLUE)

        if xa.read() < minval:
            collum -= 1
        if xa.read() > maxval:
            collum += 1
        if ya.read() < minval:
            row -= 1
        if ya.read() > maxval:
            row += 1

        if row > 2:
            row = 2
        if row < 0:
            row = 0
        if collum > 5:
            collum = 5
        if collum < 0:
            collum = 0

        display.rect(3+40*collum, 130+34*row, 34, 30, st7789.BLACK)

def redrawletters():
    letter=0
    for i in range(0,5):
        for n in range(0,10):
            display.text(font, letters[letter], 7+n*24, 153+i*17, st7789.YELLOW)
            letter += 1
    display.fill_rect(190, 218, 50, 20, st7789.BLACK)
    display.fill_rect(70, 218, 74, 20, st7789.BLACK)

    display.rect(74, 218, 68, 15, st7789.WHITE)
    display.rect(194, 218, 44, 15, st7789.WHITE)

    display.text(font, 'UP', 5, 222, st7789.YELLOW)
    display.text(font, 'SPACE', 87, 222, st7789.YELLOW)
    display.text(font, 'ENTER', 196, 222, st7789.YELLOW)

def redrawlettersupper():
    letter=0
    for i in range(0,5):
        for n in range(0,10):
            display.text(font, lettersupper[letter], 7+n*24, 153+i*17, st7789.YELLOW)
            letter += 1
    display.fill_rect(190, 218, 50, 20, st7789.BLACK)
    display.fill_rect(70, 218, 74, 20, st7789.BLACK)

    display.rect(74, 218, 68, 15, st7789.WHITE)
    display.rect(194, 218, 44, 15, st7789.WHITE)

    display.text(font, 'UP', 5, 222, st7789.YELLOW)
    display.text(font, 'SPACE', 87, 222, st7789.YELLOW)
    display.text(font, 'ENTER', 196, 222, st7789.YELLOW)

def keyboard(pretyped=''):
    display.fill(0)
    typed = pretyped
    selected = ''
    letter = 0

    row = 0
    collum = 0
    width = 20

    display.rect(width, 2, 200, 15, st7789.WHITE)

    def updatekeyboard():
        for i in range(0,5):
            for n in range(0,10):
                display.rect(2+n*24, 150+i*17, 20, 15, st7789.WHITE)

    updatekeyboard()

    redrawletters()

    display.rect(2+collum*24, 150+row*17, width, 15, st7789.RED)

    upper = False

    while True:
        time.sleep(0.15)
        display.rect(2+collum*24, 150+row*17, width, 15, st7789.WHITE)

        display.text(font, typed, 25, 5, st7789.YELLOW)
        if xa.read() <= minval:
            collum -= 1
        if xa.read() >= maxval:
            collum += 1

        if ya.read() <= minval:
            row -= 1
        if ya.read() >= maxval:
            row += 1
            
        if row < 0:
            row = 0
        if collum < 0:
            collum = 0
        if row > 4:
            row = 4
        if collum > 9:
            collum = 9
            
        if row == 4 and collum >= 3 and collum <= 5:
            width = 68
        elif row == 4 and collum >= 8 and collum <= 9:
            width = 44
        else:
            width = 20
            
        if btn.value() == 0:
            if selected == 'enter':
                return typed
                break
            else:
                if upper == False:
                    selected = letters[row * 10 + collum]
                    typed = typed + selected
                else:
                    selected = lettersupper[row * 10 + collum]
                    typed = typed + selected
                    upper = False
                    redrawletters()
        if row == 4 and collum == 8:
            selected = 'enter'
        elif row == 4 and collum == 0:
            selected = ''
            upper = True
            redrawlettersupper()

        display.rect(2+collum*24, 150+row*17, width, 15, st7789.RED)
        
def unubstructingkeyboard(pretyped=''):
    typed = pretyped
    selected = ''
    letter = 0
    row = 0
    collum = 0
    width = 20

    display.rect(width, 2, 200, 15, st7789.WHITE)

    def updatekeyboard():
        for i in range(0,5):
            for n in range(0,10):
                display.rect(2+n*24, 150+i*17, 20, 15, st7789.WHITE)

    updatekeyboard()
    
    redrawletters()

    display.rect(2+collum*24, 150+row*17, width, 15, st7789.RED)

    upper = False

    while True:
        time.sleep(0.15)
        display.rect(2+collum*24, 150+row*17, width, 15, st7789.WHITE)

        display.text(font, typed, 25, 5, st7789.YELLOW)
        if xa.read() <= minval:
            collum -= 1
        if xa.read() >= maxval:
            collum += 1

        if ya.read() <= minval:
            row -= 1
        if ya.read() >= maxval:
            row += 1
            
        if row < 0:
            row = 0
        if collum < 0:
            collum = 0
        if row > 4:
            row = 4
        if collum > 9:
            collum = 9
            
        if row == 4 and collum >= 3 and collum <= 5:
            width = 68
        elif row == 4 and collum >= 8 and collum <= 9:
            width = 44
        else:
            width = 20
            
        if btn.value() == 0:
            if selected == 'enter':
                return typed
                break
            else:
                if upper == False:
                    selected = letters[row * 10 + collum]
                    typed = typed + selected
                else:
                    selected = lettersupper[row * 10 + collum]
                    typed = typed + selected
                    upper = False
                    redrawletters()
        if row == 4 and collum == 8:
            selected = 'enter'
        elif row == 4 and collum == 0:
            selected = ''
            upper = True
            redrawlettersupper()

        display.rect(2+collum*24, 150+row*17, width, 15, st7789.RED)
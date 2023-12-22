import framebuf

def text(display, text, x=0, y=0, height=10, color=0xffff, background=0x0000):
    x = min(display.width - 1, max(0, x))
    y = min(display.height - 1, max(0, y))
    w = display.width - x
    h = min(display.height - y, height)
    buffer = bytearray(display.width * h * 2)
    fb = framebuf.FrameBuffer(buffer, w, h, framebuf.RGB565)
    for line in text.split('\n'):
        fb.fill(background)
        fb.text(line, 1, 1, color)
        display.blit_buffer(buffer, x, y, w, h)
        y += 8;
        if y >= display.height:
            break
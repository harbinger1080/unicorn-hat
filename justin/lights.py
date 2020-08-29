import colorsys as col
import unicornhat as uh
import time

uh.set_layout(uh.AUTO)
uh.rotation(0)
uh.brightness(0.25)
width,height=uh.get_shape()

columns = 0
t = 15

def set_pixel_hsv(x, y, h, s, v):
    r, g, b = [int(x*255) for x in col.hsv_to_rgb(h, s, v)]
    uh.set_pixel(x,y,r,g,b)

while (t):
    columns = t % 15
    mins, secs = divmod(t, 60)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    print(timeformat, end='\r')

    for y in range(height):
        for x in range(columns):
            uh.set_pixel(x,y,3, 130, 255)
            uh.show()
    time.sleep(1)
    t -= 1
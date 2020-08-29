import colorsys as col
import unicornhat as uh
import time
#print(col.hsv_to_rgb(1.0,1.0,1.0))

uh.set_layout(uh.AUTO)
uh.rotation(0)
uh.brightness(0.25)
width,height=uh.get_shape()

def set_pixel_hsv(x, y, h, s, v):
    r, g, b = [int(x*255) for x in col.hsv_to_rgb(h, s, v)]
    uh.set_pixel(x,y,r,g,b)

def countdown(t):
    while(t):
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins,secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1

while True:
    for y in range(height):
        for x in range(2):
            #print("x{}, y{}".format(x,y))
            uh.set_pixel(x,y,3, 130, 255)
            uh.show()
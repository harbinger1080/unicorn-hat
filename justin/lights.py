import colorsys as col
import unicornhat as uh
import time
import math

uh.set_layout(uh.AUTO)
uh.rotation(0)
uh.brightness(0.25)
width,height=uh.get_shape()

#determine the scale of the timer
#One column = X secs
csec = 60
#each dot = X secs
dotst = csec/4

mins = 0
secs = 0
t = int(input("How many seconds? "))

def dcounter(ldots):
    i = math.ceil(ldots)
    while i > 0:
        for x in range(width):
            for y in range(height):
                if (i == 1):
                    if (ldots % 1 == 0):
                        sat = 1.0
                    else:    
                        sat = (1.0 * (ldots % 1))
                    i -= 1
                    set_pixel_hsv(x, y, .58, sat, 1.0)
                if (i > 1):
                    uh.set_pixel_hsv(x, y, .58, 1.0, 1.0)
                else:
                    uh.set_pixel(x, y, 0, 0, 0)
    uh.show()

def set_pixel_hsv(x, y, h, s, v):
    r, g, b = [int(c*255) for c in col.hsv_to_rgb(h, s, v)]
    uh.set_pixel(x, y, r, g, b)

while (t):
    mins, secs = divmod(t, 60)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    print(timeformat, end='\r')
    lights = t/dotst
    dcounter(lights)
    time.sleep(1)
    t -= 1
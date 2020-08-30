import colorsys as col
import unicornhat as uh
import time
import math

uh.set_layout(uh.AUTO)
uh.rotation(0)
uh.brightness(0.25)
width,height=uh.get_shape()

mins = 0
secs = 0
t = int(input("How many minutes? "))

def dcounter(ldots):
    i = int(ldots)
    while i > 0:
        for x in range(width):
            for y in range(height):
                if (i > 0):
                    uh.set_pixel(x,y, 3, 130, 255)
                    i -= 1
                else:
                    uh.set_pixel(x,y, 0, 0, 0)
    uh.show()

while (t):
    print(t)
    mins, secs = divmod(t, 60)
    print(mins,secs)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    #print(timeformat, end='\r')
    lights = t//15
    if (lights < 1):
        lights = 0
    dcounter(lights)

    time.sleep(1)
    t -= 1
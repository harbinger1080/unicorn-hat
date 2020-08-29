import colorsys as col
import unicornhat as uh
import time
import math

uh.set_layout(uh.AUTO)
uh.rotation(0)
uh.brightness(0.25)

t = (int(input("How many minutes? "))*60)
i=0

def dcounter(totaldots):
    width = math.ceil(totaldots/4)
    for x in range(width):
        dots = math.ceil(totaldots - x * 4)
        if (dots > 4):
            dots = 4
        for y in range(dots):
            #print(x, y, end="\n")
            uh.set_pixel(x,y,3, 130, 255)
            uh.show()


while (t):
    mins, secs = divmod(t, 60)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    print(timeformat, end='\r')
    dcounter(mins//3.75)
    time.sleep(1)
    t -= 1
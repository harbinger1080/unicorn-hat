import colorsys as col
import unicornhat as uh
import time
import math

uh.set_layout(uh.AUTO)
uh.rotation(0)
uh.brightness(0.25)

mins = 0
secs = 0
t = int(input("How many minutes? "))

def dcounter(totaldots):
    print(totaldots)
    width = math.ceil(totaldots/4)
    for x in range(width):
        dots = round(totaldots/(x+1))
        for y in range(4):
            #print(x,y)
            if (y < dots):
                uh.set_pixel(x,y, 3, 130, 255)
            else:
                uh.set_pixel(x,y, 0, 0, 0)
    totaldots -= dots
    uh.show()

while (t):
    print(t)
    mins, secs = divmod(t, 60)
    print(mins,secs)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    #print(timeformat, end='\r')
    lremaining = t//15
    if (lremaining <= 1):
        lremaining = 1
    dcounter(lremaining)

    time.sleep(1)
    t -= 1
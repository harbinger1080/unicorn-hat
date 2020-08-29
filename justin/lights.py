import colorsys as col
import unicornhat as uh
import time
import math

uh.set_layout(uh.AUTO)
uh.rotation(0)
uh.brightness(0.25)

t = int(input("How many seconds? "))

def dcounter(totaldots):
    width = math.ceil(totaldots/4)
    for x in range(width):
        if (totaldots <= 4):
            dots = totaldots
        else:
            dots = 4
        for y in range(dots):
            uh.set_pixel(x,y,3, 130, 255)
            uh.show()
        totaldots -= dots


while (t):
    mins, secs = divmod(t, 60)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    print(timeformat, end='\r')
    dcounter(t//15)
    time.sleep(1)
    t -= 1
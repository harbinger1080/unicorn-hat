import colorsys as col
import unicornhat as uh
import time

uh.set_layout(uh.AUTO)
uh.rotation(0)
uh.brightness(0.25)
width,height=uh.get_shape()

t = 90

while (t):
    dots = (t * 60)//225
    print (dots)
    mins, secs = divmod(t, 60)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    print(timeformat, end='\r')

    for dot in range(dots):
        for y in range(height):
            for x in range(width):
                uh.set_pixel(x,y,3, 130, 255)
                uh.show()
        time.sleep(1)
        t -= 1
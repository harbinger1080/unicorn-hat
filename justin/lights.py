import colorsys as col
import unicornhat as uh
#print(col.hsv_to_rgb(1.0,1.0,1.0))

uh.set_layout(uh.AUTO)
uh.rotation(0)
uh.brightness(0.25)
width,height=uh.get_shape()

def set_pixel_hsv(x, y, h, s, v):
    r, g, b = [int(x*255) for x in col.hsv_to_rgb(h, s, v)]
    uh.set_pixel(x,y,r,g,b)

for y in range(4):
    for x in range(8):
        #print("x{}, y{}".format(x,y))
        set_pixel_hsv(x,y,(1.0/8)*x,(1.0/4)*y,1.0)

uh.show()
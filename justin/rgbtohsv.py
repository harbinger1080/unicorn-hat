import colorsys as col 
#import unicornhat as uh

rgb = col.hsv_to_rgb(.58, 1.0 * .4, 1.0)
rgb = [int(x*255) for x in rgb]
print(rgb)
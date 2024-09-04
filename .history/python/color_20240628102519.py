import getpixelcolor
color= getpixelcolor.pixel(700, 408)
print(color)
while (color != (0, 172, 193) or color != (24, 193, 219)):
color= getpixelcolor.pixel(700, 408)

    print(color)
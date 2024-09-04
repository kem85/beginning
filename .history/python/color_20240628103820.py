import getpixelcolor
color= getpixelcolor.pixel(700, 408)
# while (color != (0, 172, 193) or color != (24, 193, 219)):
color= getpixelcolor.pixel(700, 408)
print(color)
if(color == (0, 172, 193) or color == (24, 193, 219)):
        break
temp = "true"
with open("C:/Users/kem7/Documents/GitHub/beginning/output.txt", "w") as file:
    file.write("true")
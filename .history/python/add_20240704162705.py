f = open("C:/Users/kem7/Documents/GitHub/beginning/minecraft.txt", "r")
ch= f.read()
x = chr(ord(ch) + 1)
if(x=='z'):

    x = 'a'

with open("C:/Users/kem7/Documents/GitHub/beginning/minecraft.txt", "w") as file:
    file.write(str(x))
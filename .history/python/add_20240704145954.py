f = open("C:/Users/kem7/Documents/GitHub/beginning/minecraft.txt", "r")
ch= f.read()
x = chr(ord(ch) + 1)
with open("C:/Users/kem7/Documents/GitHub/beginning/minecraft.txt", "w") as file:
    file.write(str(x))
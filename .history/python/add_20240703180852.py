f = open("output.txt", "r")
ch= f.read()
x = chr(ord(ch) + 1)
print(x)

with open("output.txt", "w") as file:
    file.write(str(temp))
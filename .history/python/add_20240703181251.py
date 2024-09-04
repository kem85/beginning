f = open("output.txt", "r")
ch= f.read()
x = chr(ord(ch) + 1)
with open("C:\Users\kem7\Documents\GitHub\beginning\output.txt", "w") as file:
    file.write(str(x))
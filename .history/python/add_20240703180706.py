f = open("output.txt", "r")
word = f.read()

with open("output.txt", "w") as file:
    file.write(str(temp))
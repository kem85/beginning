f = open("output.txt", "r")
link = f.read()

with open("output.txt", "w") as file:
    file.write(str(temp))
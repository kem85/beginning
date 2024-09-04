import sys
print(sys.argv)
with open("output.txt", "w") as file:
    file.write(str(value))
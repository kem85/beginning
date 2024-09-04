import sys
import pyperclip
f = open("C:/Users/kem7/Documents/GitHub/beginning/link.txt", "r")
link = f.read()
lst = []
num = ""
for count, i in enumerate(link):
    if i == '-':
        lst.append(count)
max = max(lst)+1
for i in link[max:]:
    num += i
temp = link[:max] + str(int(num)+1)
with open("C:/Users/kem7/Documents/GitHub/beginning/link.txt", "w") as file:
    file.write(str(temp))
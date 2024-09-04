import sys
import pyperclip
f = open("link.txt", "r")
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
with open("link.txt", "w") as file:
    file.write(str(temp))
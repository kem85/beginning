import sys
import pyperclip
link = sys.argv[1]
lst = []
num = ""
for count, i in enumerate(link):
    if i == '-':
        lst.append(count)
max = max(lst)+1
for i in link[max:]:
    num += i
temp = link[:max] + str(int(num)+1)
with open("output.txt", "w") as file:
    file.write(str(temp))

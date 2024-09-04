import sys
link = sys.arv[1]
link = link[len(link)-1] + 1
with open("output.txt", "w") as file:
    file.write(str(link))
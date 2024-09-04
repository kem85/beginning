import sys
link = sys.arv[1]
link = link[len(link)]
with open("output.txt", "w") as file:
    file.write(str(sys.argv[1]))
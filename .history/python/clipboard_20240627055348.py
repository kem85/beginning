import sys

link = "https://fmovies24.to/tv/house-qk23/7-8"
temp = list(link)
temp[link[len(link)-1]] = slice(int(link[len(link)-1])+1)
link =temp.join("")
print(link)
# with open("output.txt", "w") as file:
#     file.write(str(link))
import sys

link = "https://fmovies24.to/tv/house-qk23/7-8"
temp = list(link)
temp[len(temp)-1] = chr(temp[len(link)-1])
link = "".join(temp)
print(link)
# with open("output.txt", "w") as file:
#     file.write(str(link))
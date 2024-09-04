import sys

link = "https://fmovies24.to/tv/house-qk23/7-99"
temp = list(link)
temp[len(temp)-1] = str(int(temp[len(temp)-1])+1)
link = "".join(temp)
print(link)
# with open("output.txt", "w") as file:
#     file.write(str(link))
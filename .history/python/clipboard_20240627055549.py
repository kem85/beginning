import sys

link = "https://fmovies24.to/tv/house-qk23/7-8"
temp = list(link)
temp[len(temp)-1] = chr(int(link[len(link)-1])+1)
new_string = "".join(temp)
print(temp)
# with open("output.txt", "w") as file:
#     file.write(str(link))
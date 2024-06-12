import os
import random
def maker(x):
    for i in range(x+1)[1:]:
        dic = "pablo"+str(i);
        parent_dir = "D:/Assignment/2023-2024/Term 2/test"
        path = os.path.join(parent_dir, dic) 
        os.mkdir(path)


def main():
    g = int(input())
    maker(g)
if __name__ == "__main__":
    main()
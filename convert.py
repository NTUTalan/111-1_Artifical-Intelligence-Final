import numpy as np # 匯入numpy模組
import sys
from PIL import Image

white = np.array([255, 255, 255])
black = np.array([0, 0, 0])
red = np.array([237, 28, 36])
yellow = np.array([255, 242, 0])
blue = np.array([0, 0, 255])

def main(fileName):
    temp = np.loadtxt(".\\shortest\\" + fileName + "_solution.csv", dtype = np.int, delimiter = ',')
    a = np.empty([temp.shape[0], temp.shape[1], 3], dtype = np.uint8)

    for i in range(0, len(temp)):
        for j in range(0,len(temp[i])):
            if temp[i, j] == 1:
                a[i, j] = black
            elif temp[i, j] == 0:
                a[i, j] = white
            elif temp[i, j] == 2:
                a[i, j] = yellow
            elif temp[i, j] == 3:
                a[i, j] = red
            elif temp[i, j] == -1:
                a[i, j] = blue
                
    img = Image.fromarray(a)
    img.save(".\\shortest\\" + fileName + '_solution.png')
    img.show()

if(__name__ == '__main__'):
    main(sys.argv[1])
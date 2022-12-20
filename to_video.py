import numpy as np # 匯入numpy模組
import os
from PIL import Image
import cv2
import re
import sys

white = np.array([255, 255, 255])
black = np.array([0, 0, 0])
red = np.array([237, 28, 36])
yellow = np.array([255, 242, 0])
blue = np.array([0, 0, 255])

def main(mapName):
    directory = "..\\moving_path\\"
    fileList = list(filter(lambda file: bool(re.search(".png", file)), os.listdir(directory + mapName)))
    newFileList = [int(file.split(".")[0]) for file in fileList]
    newFileList.sort()

    testImg = cv2.imread(directory + mapName + "\\" + "0.png")
    fps = 60
    size = (testImg.shape[1], testImg.shape[0])
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    videoWrite = cv2.VideoWriter(directory + mapName + "\\" + "video.mp4", fourcc, fps, size)
    for file_num in newFileList:
        img = cv2.imread(directory + mapName + "\\" + str(file_num) + ".png")
        videoWrite.write(img)
    videoWrite.release()

if(__name__ == '__main__'):
    args = sys.argv[1:]
    print("Processing...")
    main(args[0])
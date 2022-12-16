import os
import cv2
import numpy as np

EMPTY_CELL = 0
OBSTACLE_CELL = 1
START_CELL = 2
GOAL_CELL = 3
white = np.array([255, 255, 255])
black = np.array([0, 0, 0])
red = np.array([36, 28, 237])
yellow = np.array([0, 242, 255])

# if __name__ == "__main__":
#   map_path = os.getcwd()
#   maplist = os.listdir(map_path)
#   maplist.sort
#   for map in maplist:
#     img = cv2.imread(map, cv2.IMREAD_COLOR)
#     data = np.zeros([img.shape[1], img.shape[0]])
#     for i in range(img.shape[1]):
#       for j in range(img.shape[0]):
#         if (img[i, j] == white).all():
#           data[i, j] = EMPTY_CELL
#         elif (img[i, j] == black).all():
#           data[i, j] = OBSTACLE_CELL
#         elif (img[i, j] == red).all():
#           data[i, j] = START_CELL
#         elif (img[i, j] == yellow).all():
#           data[i, j] = GOAL_CELL
      
#     np.savetxt(os.path.splitext(map)[0]+'.csv', data, delimiter=',', fmt='%d')

name = "test_map"
img = cv2.imread(name + ".png", cv2.IMREAD_COLOR)
print(img.shape[0], img.shape[1])
data = np.zeros([img.shape[1], img.shape[0]])
for i in range(img.shape[1]):
  for j in range(img.shape[0]):
    if (img[i, j] == white).all():
      data[i, j] = EMPTY_CELL
    elif (img[i, j] == black).all():
      data[i, j] = OBSTACLE_CELL
    elif (img[i, j] == red).all():
      data[i, j] = START_CELL
    elif (img[i, j] == yellow).all():
      data[i, j] = GOAL_CELL
      
np.savetxt(name +'.csv', data, delimiter=',', fmt='%d')
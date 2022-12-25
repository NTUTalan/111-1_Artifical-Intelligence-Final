# -*- coding: UTF-8 -*-
import numpy as np
import point as pt
import sys
from PIL import Image
import time

'''
point => 中心座標
direction => 方向 
'''

mapName = "" # 地圖名稱
name = 0

def printResultTime(time):
    hour = time // 3600
    min = (time % 3600) // 60
    sec = ((time % 3600) // 60) % 60
    print("執行時間: %d小時 %d分 %d秒" % (hour, min, sec))

def drawPath(point, map):
    '''
    畫圖的小函式
    '''
    global name 
    temp = np.copy(map)
    n = 0
    while(point.parent != None):
        temp[point.x, point.y] = 127
        point = point.parent
        n += 1
    for i in range(0, len(temp)):
        for j in range(0,len(temp[i])):
            if temp[i, j] == 1: temp[i, j] = 0
            elif temp[i, j] == 0: temp[i, j] = 255      
    img = Image.fromarray(temp).convert("L")
    img.save('..\\moving_path\\' + mapName + "\\" + str(name) + '.png')
    name += 1
    
def getCost(now, stop):
    return now.costFromInit + pt.distance(now, stop)
           
def isMovable(point, direction, map):
    # 透過point的x, y 去看isMovable
    # i => x axis bias
    # j => y axis bias
    max_y = map.shape[0] - 1
    max_x = map.shape[1] - 1
    testPt = Move(point, direction)
    for i in range(-10, 11): 
        for j in range(-10, 11):
            # 是否在圓形內
            if(pt.distance(testPt, pt.Point([testPt.x + i, testPt.y + j])) < 10):
                if(testPt.x + i < 0 or testPt.y + j < 0):
                    return False
                if(testPt.x + i > max_x or testPt.y + j > max_y):
                    return False
                if(map[testPt.x + i, testPt.y + j] == 1):
                    return False
    return True

def Move(point, direction):
    result = pt.Point(point)
    if(direction == 0): 
        result.y += -1
    elif(direction == 1): 
        result.x += 1
        result.y += -1
    elif(direction == 2): 
        result.x += 1
    elif(direction == 3):
        result.x += 1
        result.y += 1
    elif(direction == 4):
        result.y += 1
    elif(direction == 5):
        result.x += -1
        result.y += +1
    elif(direction == 6):
        result.x += -1
    elif(direction == 7):
        result.x += -1
        result.y += -1
    else: raise Exception("Direction not defined")
    return result

def solution(map):
    startTime = time.time()

    frontier = list()
    opened = list()
    costList = list()

    startPoint = pt.Point(np.where(map == 2))
    stopPoint = pt.Point(np.where(map == 3))
    print("distance(start, stop) = " + str(pt.distance(startPoint, stopPoint)))

    currentPoint = startPoint # 指定Initial Node
    while 1:
        # print(currentPoint)
        # drawPath(currentPoint, map)
        '''
        加入已走過的點 & frontier刪除已走過的點
        '''
        opened.append(currentPoint)
        if(currentPoint in frontier):
            del costList[frontier.index(currentPoint)]
            frontier.remove(currentPoint)
        '''
        如果為最解結束迴圈, 否則繼續進行
        '''
        if(currentPoint == stopPoint):
            print(currentPoint.costFromInit)
            break
        '''
        可行動的點
        '''
        test = [] 
        # 測試8個方向
        for i in range(8):  
            if(isMovable(currentPoint, i, map)):
                p = Move(currentPoint, i)
                if(p in opened): continue # 測試是否已走過  
                if(p in frontier): continue # 測試是否在frontier內
                p.parent = currentPoint
                p.costFromInit = currentPoint.costFromInit + pt.distance(p, currentPoint)       
                test.append(p)
        costList.extend([getCost(movable_pt, stopPoint) for movable_pt in test])
        frontier.extend(test)
        '''
        判斷Cost, 進下個點
        '''
        next = frontier[costList.index(min(costList))]
        currentPoint = next

    endTime = time.time()    
    printResultTime(endTime - startTime)
    ("在" + str(currentPoint) + "結束")
    while(currentPoint.parent != None):
        map[currentPoint.x, currentPoint.y] = -1
        currentPoint = currentPoint.parent
    np.savetxt('.\\shortest\\' + mapName + "_solution.csv", map, delimiter = ",")

if(__name__ == "__main__"):
    args = sys.argv[1:]
    mapName = args[0]
    mapFile = np.genfromtxt(".\\ai_map\\" + mapName + ".csv", delimiter=',')
    print("Finding...")
    solution(mapFile)
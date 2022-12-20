# -*- coding: UTF-8 -*-
import numpy as np
import point as pt
import sys
from PIL import Image
'''
point => 中心座標
direction => 方向 
以正方形來跑
中心x座標+-10
中心y座標+-10
'''

mapName = "" # 地圖名稱
name = 0

def drawPath(point, map):
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

def isMovable_little(point, direction, map):
    max_y = map.shape[0] - 1
    max_x = map.shape[1] - 1
    testPt = Move_8(point, direction)
    if(testPt.x < 0 or testPt.y < 0):
        return False
    if(testPt.x > max_x or testPt.y > max_y):
        return False
    if(map[testPt.x, testPt.y] == 1):
        return False
    return True
def Move_8(point, direction):
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
    frontier = list()
    opened = list()

    startPoint = pt.Point(np.where(map == 2))
    stopPoint = pt.Point(np.where(map == 3))
    # print(startPoint)
    # print(stopPoint)
    currentPoint = startPoint # 指定Initial Node
    while 1:
        print(currentPoint)
        drawPath(currentPoint, map)
        '''
        加入已走過的點
        '''
        # opened.append(currentPoint)
        if(currentPoint in frontier):
            frontier.remove(currentPoint)
        '''
        如果為最解結束迴圈, 否則繼續進行
        '''
        if(currentPoint == stopPoint):
            print(costList)
            print(currentPoint.costFromInit)
            break
        '''
        可行動的點
        '''
        test = [] 
        # 測試8個方向
        for i in range(8):  
            if(isMovable_little(currentPoint, i, map)):
                p = Move_8(currentPoint, i)
                # 測試是否已走過
                # if(p in opened): continue
                # 測試是否在frontier內
                # if(p in frontier): continue
                p.parent = currentPoint
                if(currentPoint.parent != None):
                    if(p.x == currentPoint.parent.x and p.y == currentPoint.parent.y): continue
                p.costFromInit = currentPoint.costFromInit + pt.distance(p, currentPoint)       
                test.append(p)
        
        frontier.extend(test)
        # print(frontier)
        '''
        判斷Cost, 進下個點
        '''
        costList = [getCost(movable_pt, stopPoint) for movable_pt in frontier]
        # print(costList)
        next = frontier[costList.index(min(costList))]
        # frontier.remove(currentPoint)  
        # print(next)
        currentPoint = next
        
    ("在" + str(currentPoint) + "結束")
    while(currentPoint.parent != None):
        map[currentPoint.x, currentPoint.y] = -1
        currentPoint = currentPoint.parent

    np.savetxt('.\\shortest\\' + mapName + "-path.csv", map, delimiter = ",")

if(__name__ == "__main__"):
    args = sys.argv[1:]
    mapName = args[0]
    mapFile = np.genfromtxt(".\\ai_map\\" + mapName + ".csv", delimiter=',')
    solution(mapFile)
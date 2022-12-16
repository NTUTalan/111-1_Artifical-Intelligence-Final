# -*- coding: UTF-8 -*-
import numpy as np
import point as pt
import sys
sys.setrecursionlimit(5000)
'''
point => 中心座標
direction => 方向 (4種 順時針, 編號0~3) 
以正方形來跑
中心x座標+-10
中心y座標+-10
'''

mapName = "medium-medium" # 地圖名稱

def getCost(now, stop):
    return now.costFromInit + pt.distance(now, stop)
           
def isMovable(point, direction, map):
    # 透過point的x, y 去看isMovable
    # i => x axis bias
    # j => y axis bias
    max_y = map.shape[0] - 1
    max_x = map.shape[1] - 1
    testPt = pt.Point(point)
    Move(testPt, direction)
    for i in range(-10, 11): 
        for j in range(-10, 11):
            if(testPt.x + i < 0 or testPt.y +j < 0):
                return False
            if(testPt.x + i > max_x or testPt.y + j > max_y):
                return False
            if(map[testPt.x + i, testPt.y + j] == 1):
                return False
    return True

def Move(point, direction):
    result = pt.Point(point)
    if(direction == 0): result.y += -1
    elif(direction == 1): result.x += 1
    elif(direction == 2): result.y += 1
    elif(direction == 3): result.x += -1
    else: raise Exception("Direction not defined")
    # 如需要斜走，之後再加
    return result

def solution(map):
    frontier = list()
    opened = list()

    def recursive(point):
        print("Enter: ", end = "")
        print(point)
        
        # 加入已走過的點
        if(len(opened) != 0):
            point.costFromInit = point.parent.costFromInit + pt.distance(point, point.parent)
        opened.append(point)  

        # 如果為解回傳這個點
        if(point == stopPoint):
            return point

        # 可行動的點
        test = []
        for i in range(4):  
            if(isMovable(point, i, map)):
                p = Move(point, i)
                p.setParent(point)
                test.append(p)
        for test_point in opened:
            if(test_point in test):
                test.remove(test_point)
        for test_point in frontier:
            if(test_point in test):
                test.remove(test_point)
        # for test_point in frontier:
        #     if(pt.distance(test_point, point) > 99):
        #         frontier.remove(test_point)
        print(frontier)
        print(test)
        frontier.extend(test)

        # 判斷Cost, 進下個點
        costList = []
        for movable_pt in frontier:
            costList.append(getCost(movable_pt, stopPoint))
        next = frontier[costList.index(min(costList))]
        print(costList)
        print(next)
        recursive(next)

    startPoint = pt.Point(np.where(map == 2))
    stopPoint = pt.Point(np.where(map == 3))

    lastPoint = recursive(startPoint)
    print(stopPoint)
    while(lastPoint.parent != None):
        map[lastPoint.x, lastPoint.y] = -1
        lastPoint = lastPoint.parent

    np.savetxt('.\\shortest\\' + mapName + "-path.csv", map, delimiter = ",")

if(__name__ == "__main__"):
    mapFile = np.genfromtxt(".\\ai_map\\" + mapName + ".csv", delimiter=',')
    solution(mapFile) 
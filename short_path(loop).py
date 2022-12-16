# -*- coding: UTF-8 -*-
import numpy as np
import point as pt
'''
point => 中心座標
direction => 方向 
以正方形來跑
中心x座標+-10
中心y座標+-10
'''

mapName = "big-easy" # 地圖名稱

def getCost(now, stop):
    return now.costFromInit + pt.distance(now, stop)
           
def isMovable(point, direction, map):
    # 透過point的x, y 去看isMovable
    # i => x axis bias
    # j => y axis bias
    max_y = map.shape[0] - 1
    max_x = map.shape[1] - 1
    testPt = pt.Point(point)
    Move_8(testPt, direction)
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

def Move_4(point, direction):
    result = pt.Point(point)
    if(direction == 0): result.y += -1
    elif(direction == 1): result.x += 1
    elif(direction == 2): result.y += 1
    elif(direction == 3): result.x += -1
    else: raise Exception("Direction not defined")
    return result

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
        result.y += -1
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
    currentPoint = startPoint # 指定Initial Node
    while 1:
        print("Enter: ", end = "")
        print(currentPoint)
        '''
        加入已走過的點
        '''
        opened.append(currentPoint) 
        if(currentPoint in frontier):
            frontier.remove(currentPoint)
        '''
        如果為解結束迴圈
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
                p = Move_8(currentPoint, i)
                p.setParent(currentPoint)
                test.append(p)
        # 測試是否已走過
        for test_point in opened:
            if(test_point in test):
                test.remove(test_point)
        # 測試是否在frontier內
        for test_point in frontier:
            if(test_point in test):
                test.remove(test_point)
        frontier.extend(test)
        '''
        判斷Cost, 進下個點
        '''
        costList = [getCost(movable_pt, stopPoint) for movable_pt in frontier]
        next = frontier[costList.index(min(costList))]  
        currentPoint = next
        currentPoint.costFromInit = currentPoint.parent.costFromInit + pt.distance(currentPoint, currentPoint.parent)
        



    ("在" + str(currentPoint) + "結束")
    while(currentPoint.parent != None):
        map[currentPoint.x, currentPoint.y] = -1
        currentPoint = currentPoint.parent

    np.savetxt('.\\shortest\\' + mapName + "-path.csv", map, delimiter = ",")

if(__name__ == "__main__"):
    mapFile = np.genfromtxt(".\\ai_map\\" + mapName + ".csv", delimiter=',')
    solution(mapFile) 
import math

class Point:
    def __init__(self, data = None):
        if(type(data) == list):
            self.x = data[0]
            self.y = data[1]
            self.parent = None
        elif(type(data) == tuple):
            self.x = data[0][0]
            self.y = data[1][0]
            self.parent = None
        elif(type(data) == Point):
            self.x = data.x
            self.y = data.y
            self.parent = data.parent
        self.costFromInit = 0
    def setParent(self, p):
        self.parent = p
    def isSame(self, p):
        if(self.x == p.x and self.y == p.y):
            return True
        return False
    def isInList(self, list):
        for item in list:
            if(self.isSame(item)): return True
        return False
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    def __repr__(self):
        return str(self)
    def __eq__(self, __o: object) -> bool:
        if(__o == None):
            return False
        if(self.x == __o.x and self.y == __o.y): return True
        return False
def distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
class robot:
    def __init__(self, location):
        self.location = location # [x, y]
        self.degree = 0 # 定義如pdf

    def turnRight(self):
        if(self.degree >= 180): self.degree = -135
        else: self.degree += 45

    def foward(self):
        if(self.degree == 0): self.locationChange(0, 1)
        elif(self.degree == 45): self.locationChange(1, 1)
        elif(self.degree == 90): self.locationChange(1, 1)
        elif(self.degree == 135): self.locationChange(1, 1)
        elif(self.degree == 180 or self.degree == -180): self.locationChange(1, 1)
        elif(self.degree == 45): self.locationChange(1, 1)
        elif(self.degree == 45): self.locationChange(1, 1)
        elif(self.degree == 45): self.locationChange(1, 1)
    
    def locationChange(self, x_bias, y_bias):
        self.location[0] += x_bias
        self.location[1] += y_bias
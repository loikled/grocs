from math import sqrt,pi

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return '('+str(self.x)+', '+str(self.y)+')'

    def distance_from(self, point):
        return sqrt(abs(point.x - self.x)**2 + abs(point.y - self.y)**2)

def distance(a,b):
    return a.distance_from(b)


from math import sqrt,sin,cos,atan,pi
from geometry import *

class Position(Point):
    def __init__(self, x = 0, y = 0, angle = 0, speed = 0, acceleration = 0):
        Point.__init__(self,x,y)
        self.angle = angle
        self.speed = speed
        self.acceleration = acceleration
        
    def __repr__(self):
        return 'x: {self.x}, y: {self.y}, angle: {self.angle}, speed: {self.speed}, accel: {self.acceleration}'.format(self = self)

    def future_pos(self, delta_ms):
        next_pos = position()
        next_pos.acceleration = self.acceleration
        next_pos.speed = self.speed + (self.acceleration*delta_ms)/1000
        delta_d = delta_ms*self.speed
        next_pos.x = self.x + cos((self.angle*2*pi/360))*delta_d
        next_pos.y = self.y + sin((self.angle*2*pi/360))*delta_d
        next_pos.angle = self.angle
        return next_pos
    
    def get_point_at_dist(self, distance):
        return Point(self.x + cos((self.angle*2*pi/360))*distance, 
                     self.y + sin((self.angle*2*pi/360))*delta_d)
      
        
if __name__ == '__main__':
    origin = position()
    a = position(10,10)
    b = position(20,20)
    print 'test of distances, 0 -> a: ' + str(origin.distance_from(a))
    print 'distance between a and b: ' + str(distance_between(a,b))

    c = position(0,0,30,0,1.0)
    print 'start pos c: ' + str(c)
    for i in range(10):
        d = c.future_pos(100)
        c = d
        print 't = {}ms, new pos: '.format(100*i) + str(d)


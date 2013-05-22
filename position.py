from math import sqrt,sin,cos,atan,pi
from geometry import *

class Position(Point):
    def __init__(self, x = 0, y = 0, angle = 0, acceleration = 0, l_speed = 0, r_speed = 0):
        Point.__init__(self,x,y)
        self.angle = angle
        self.r_speed = r_speed #rotation speed in degrees/s to move in curves, negative when turning right
        self.l_speed = l_speed #linear speed in m/s, for straight forward movements
        self.acceleration = acceleration
        
    def __repr__(self):
        return 'x: {self.x}mm, y: {self.y}mm, angle: {self.angle}, r_speed: {self.r_speed}, l_speed: {self.l_speed}, accel: {self.acceleration}'.format(self = self)
    
    def future_pos(self, delta_ms):
        """Compute the position we will be in delta_ms by going forward,
        taking into account the acceleration, linear speed and rotation speed"""
        next_pos = Position()
        next_pos.acceleration = self.acceleration
        next_pos.l_speed = self.l_speed + float(self.acceleration*delta_ms)/1000
        next_pos.r_speed = self.r_speed
        delta_d = delta_ms*self.l_speed # d in mm, dont need to divide by 1000
        delta_r = float(delta_ms*self.r_speed)/1000
        print delta_d,delta_r
        print 'delta r: ' + str(delta_r)
        next_pos.angle = self.angle + delta_r
        next_pos.x = self.x + cos((self.angle*2*pi/360))*delta_d
        next_pos.y = self.y + sin((self.angle*2*pi/360))*delta_d
        return next_pos

    def get_point_at_dist(self, distance):
        return Point(self.x + cos((self.angle*2*pi/360))*distance, 
                     self.y + sin((self.angle*2*pi/360))*distance)

    def angle_to(self, point):
        "return the absolute angle of the vector(self,point)"
        delta_x = point.x - self.x
        delta_y = point.y - self.y
        return (atan(delta_y/delta_x)*360)/(2*pi)
        
if __name__ == '__main__':
    origin = Position()
    a = Position(10,10)
    b = Position(13,14)
    print 'test of distances, 0 -> a: ' + str(origin.distance_from(a))
    print 'distance between a and b: ' + str(distance(a,b))
    print 'angle between a and b: ' + str(a.angle_to(b))
    c = Position(0,0,30,1.0,0.5,1)
    print 'start pos c: ' + str(c)
    for i in range(10):
        d = c.future_pos(100)
        c = d
        print 't = {}ms, new pos: '.format(100*(i+1)) + str(d)


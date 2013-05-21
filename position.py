from math import sqrt,sin,cos,atan,pi

class position:
    def __init__(self, x = 0, y = 0, angle = 0, speed = 0, acceleration = 0):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.acceleration = acceleration
        
    def __repr__(self):
        return 'x: {self.x}, y: {self.y}, angle: {self.angle}, speed: {self.speed}, accel: {self.acceleration}'.format(self = self)

    def distance_from(self, point):
        return sqrt(abs(point.x - self.x)**2 + abs(point.y - self.y)**2)

    def future_pos(self, delta_ms):
        next_pos = position()
        next_pos.acceleration = self.acceleration
        next_pos.speed = self.speed + (self.acceleration*delta_ms)/1000
        delta_d = delta_ms*next_pos.speed
        next_pos.x = self.x + cos((self.angle*2*pi/360))*delta_d
        next_pos.y = self.y + sin((self.angle*2*pi/360))*delta_d
        next_pos.angle = self.angle
        return next_pos

def distance_between(a,b):
    return a.distance_from(b)

if __name__ == '__main__':
    origin = position()
    a = position(10,10)
    b = position(20,20)
    c = position(0,0,0,0,1.0)
    d = c.future_pos(100)
    print 'test of distances, 0 -> a: ' + str(origin.distance_from(a))
    print 'distance between a and b: ' + str(distance_between(a,b))
    print 'start pos c: ' + str(c)
    print ' end pos: ' + str(d)

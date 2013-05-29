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

class Segment:
    """a segment is composed of two points"""
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.length = self.start.distance_from(self.end)
    
    def __repr__(self):
        return str(self.start) + ' -- ' + str(self.length) +  ' -- ' + str(self.end)

class Polygon:
    """create a lists of points each connected to the next one"""
    def __init__(self, point_list = [(0,0),(0,0),(0,0)]):
        self.points = []
        for (a,b) in point_list:
            self.points.append(Point(a,b))
        self.center = Point()
        self.update_center()
    
    def update_center(self):
        if len(self.points)> 0:
            self.center.x = sum(point.x for point in self.points)/len(self.points)
            self.center.y = sum(point.y for point in self.points)/len(self.points)

    def get_points(self):
        point_list = []
        for point in self.points:
            point_list.append((point.x,point.y))
        return point_list

    def add_point(self, point):
        self.points.append(point)
        update_center()
        
    def contains(self, point):
        return False
    
    def get_edges(self):
        edges = []
        for (a,b) in zip(self.points[:-1],self.points[1:]):
            edges.append(Segment(a,b))
        edges.append(Segment(self.points[-1],self.points[0]))
        return edges

    def __repr__(self):
        res =''
        for point in self.points:
            res += str(point)
        res += '\n'
        for segment in self.get_edges():
            res += str(segment) + '\n'
        return res

if __name__ == '__main__':
    a = Point(0,0)
    b = Point(3,4)
    c = Polygon()
    print c
    square = Polygon([(0,0),(1,0),(1,1),(0,1)])
    print 'a: ' + str(a) + ', b: ' + str(b)
    print 'distance ab: ' + str(a.distance_from(b))
    for segment in square.get_edges():
        print str(segment)

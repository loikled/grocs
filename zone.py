from geometry import Point

class Zone:
    states = ["free", "taken"]

    def __init__(self, name = 'zone', number = 0):
        self.items = []
        self.state = "free"
        self.is_crossable = True
        self.childrens = []
        self.neighbors = []
        self.number = number
        self.name = name
        self.id = self.name + str(self.number)
        self.polygon = []
        self.center = Point(0,0)

    def __repr__(self):
        string = 'id: '+self.id + ', state: ' + self.state + ', crossable: ' + str(self.is_crossable) + '\n'
        string += 'Polygon: '+ str(self.polygon)
        string += '\nitems in: ' + str(self.items) + '\n'
        string += 'neighbors: ' +str(self.neighbors) + '\n'
        string += 'childrens: ' + str(self.childrens) + '\n'
        return string
    
    def set_polygon(self, points):
        self.polygon = points
        self.center.x = sum(point.x for point in self.polygon)/len(self.polygon)
        self.center.y = sum(point.y for point in self.polygon)/len(self.polygon)
             
    def add_child(self, subzone):
        self.childrens.append(subzone)
    
    def add_item(self, item):
        self.items.append(item)
        
if __name__ == '__main__':
    background = Zone('background')
    background.add_child('start_left')
    background.add_child('start_right')
    square = [Point(0,0), Point(3000,0),Point(3000,2000),Point(0,2000)]
    background.set_polygon(square)

    print 'test zone: '
    print str(background)
    

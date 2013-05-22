from geometry import *

class Zone(Polygon):
    states = ["free", "taken"]

    def __init__(self, name = 'zone', number = 0):
        Polygon.__init__(self)
        self.items = []
        self.state = "free"
        self.is_crossable = True
        self.childrens = []
        self.neighbors = []
        self.number = number
        self.name = name
        self.id = self.name + str(self.number)
        self.polygon = Polygon()

    def __repr__(self):
        string = 'id: '+self.id + ', state: ' + self.state + ', crossable: ' + str(self.is_crossable) + '\n'
        string += 'Polygon: '+ str(self.polygon)
        string += '\nitems in: ' + str(self.items) + '\n'
        string += 'neighbors: ' +str(self.neighbors) + '\n'
        string += 'childrens: ' + str(self.childrens) + '\n'
        return string
    
    def set_polygon(self, points):
        self.polygon = Polygon(points)
             
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

from position import *

class robot:
    def __init__(self, name = 'robot', big = True, color = 'red'):
        self.name = name
        self.is_big = big
        self.color = color
        self.actions = []
        self.start_zone = None
        self.pos = position() # x,y,theta,speed,acceleration

    def can_take(self, item):
        return False
    

    

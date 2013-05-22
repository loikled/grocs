from position import *

class robot:
    def __init__(self, name = 'robot', color = 'red'):
        self.name = name
        self.color = color
        self.actions = []
        self.start_zone = None
        self.pos = Position() # x,y,theta,speed,acceleration
        self.current_action = None

    def can_take(self, item):
        return False
    

    

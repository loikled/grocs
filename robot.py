from position import *

class robot:
"""robot class, performs actions in the game, actions that take time"""
    def __init__(self, name = 'robot', color = 'red'):
        self.name = name
        self.color = color
        self.actions = []
        self.start_zone = None
        self.pos = Position() # x,y,theta,speed,acceleration
        self.current_action = None

    def can_take(self, item):
        return False

    def orient_to(self, point):
        next_angle = self.pos.angle_to(point)
        
    def move(self, distance):
        next_point = self.pos.get_point_at_dist(distance)
        
    

    

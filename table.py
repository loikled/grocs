from zone import *

class table:
    def __init__(self):
            self.root_zone = None
            self.zones_map = {}
            self.red_robots = []
            self.blue_robots = []
            self.elements = []

    def add_zone(self, zone):
        self.zones_map[zone.id] = zone
        
    def load_config(self, config_file):
            

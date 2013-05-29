import pygame
from pygame.locals import *
from table import *
from collections import deque
from pygame.transform import scale

class Graphics:
    def __init__(self):
        pygame.init()
        self.screen_width = 640
        self.screen_height = 480
        self.surfaces = {}
        self.clock = pygame.time.Clock()
        self.fps = 30
        self.screen = pygame.display.set_mode([self.screen_width,self.screen_height])
        self.screen.fill([255,255,255])
        self.ratio_x = 1.0
        self.ratio_y = 1.0
        
    def load_table(self, table):
        self.table = table
        for zone in table.zones_map.values():
            name = zone.name+".bmp"
            print 'loading: '+ name
            self.surfaces[zone.id] = pygame.image.load(name).convert()

        background = self.table.zones_map['background0']
        #background is always a rect 3rd points has max x,y
        self.set_ratio(background.points[2].x, background.points[2].y)

    def set_ratio(self, background_x, background_y):
        self.ratio_x = float(self.screen.get_width())/background_x
        self.ratio_y = float(self.screen.get_height())/background_y
        print 'reduction ratio = '+ str(self.ratio_x) +', ' +str(self.ratio_y)
    
    def refresh_table(self):
        """breadth first exploration of the map from the background
            to display zones on each other in the right order"""
        start_node = self.table.zones_map['background0']
        to_display = []
        to_visit = deque([start_node.id])
        while len(to_visit) > 0:
            current_zone = to_visit.popleft()
            to_display.append(current_zone)
            for children in self.table.zones_map[current_zone].childrens:
                to_visit.append(children)
        #print to_display
        for zone_id in to_display:
            self.blit_zone(self.table.zones_map[zone_id])

    def blit_zone(self, zone):
        left_corner_reduced = Point()
        left_corner = zone.points[0]
        left_corner_reduced.x = int(left_corner.x*self.ratio_x)
        left_corner_reduced.y = int(left_corner.y*self.ratio_y)
        
        s = self.surfaces[zone.id]
        current_surface = scale(s, (int(s.get_width()*self.ratio_x),
                                    int(s.get_height()*self.ratio_y)))
        #print 'bliting: ' +zone.id + ' at: ' + str(left_corner_reduced)
        self.screen.blit(current_surface,(left_corner_reduced.x,left_corner_reduced.y))
        
    def main_loop(self):
        do_continue = True
        while do_continue:
            self.clock.tick(self.fps)
            self.screen.fill([255,255,255])
            self.refresh_table()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    do_continue = False # Be IDLE friendly!
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        do_continue = False # Be IDLE friendly
            pygame.display.update()
        pygame.quit()    

if __name__ == '__main__':
    g = Graphics()    
    background = Zone('background')
    square = [(0,0), (3000,0), (3000,2000), (0,2000)]
    background.set_polygon(square)
    up_left = Zone('start_red')
    square = [(0,0), (500,0), (500,500), (0,500)]
    up_left.set_polygon(square)
    up_right = Zone('start_blue')
    square = [(3000-500,0), (3000,0), (3000,500), (3000-500,500)]
    up_right.set_polygon(square)

    down_left = Zone('start_red',1)
    square = [(0,2000-500), (500,2000-500), (500,2000), (0,2000)]
    down_left.set_polygon(square)
    down_right = Zone('start_blue',1)
    square = [(3000-500,2000-500), (3000,2000-500), (3000,2000), (3000-500,2000)]
    down_right.set_polygon(square)

    background.add_child(up_left.id)
    background.add_child(up_right.id)
    background.add_child(down_left.id)
    background.add_child(down_right.id)
    
    table = Table()
    table.set_root(background)
    table.add_zone(up_left)
    table.add_zone(up_right)
    table.add_zone(down_left)
    table.add_zone(down_right)
    
    g.load_table(table)
    g.main_loop()

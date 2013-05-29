from json import loads,dumps,load,dump
from Zone import *
from Element import *
from Geometry import *
from Table import *

def serialize(obj):
    if isinstance(obj, Point):
        return {"__class__" : "Point",
               "x" : obj.x,
               "y" : obj.y
                }
    if isinstance(obj, Zone):   
        return {"__class__" : "Zone",
                "items" : obj.items,
                "childrens" : obj.childrens,
                "name" : obj.name,
                "number": obj.number,
                "neighbors" : obj.neighbors,
                "points": obj.get_points()
                }
    if isinstance(obj, Polygon):
        return  {"__class__" : "Polygon",
                 "points": obj.get_points()
                }
    if isinstance(obj, Element):
        return {"__class__" : "Element",
                "moveable" : obj.moveable,
                "contains" : obj.contains,
                "base_points" : obj.base_points,
                "name" : obj.name,
                "number": obj.number,
                "start_zone": obj.start_zone}

    raise TypeError(repr(obj) + " n'est pas sérialisable !")

def unserialize(obj_dict):
    if "__class__" in obj_dict:
        if obj_dict["__class__"] == "Zone":
            obj = Zone(obj_dict["name"], obj_dict["number"])
            obj.items = obj_dict["items"]
            obj.childrens = obj_dict["childrens"]
            obj.neighbors = obj_dict["neighbors"]
            obj.set_polygon(obj_dict["points"])
            return obj
    else:
        return None

if __name__ == '__main__':
    
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

    with open("test.json", "w") as File:
        dump(table.zones_map, File, default=serialize, indent=4)
    
    File.close()
    
    table_loaded = Table()
    tmp = {}
    with open("test.json", "r") as File:
       tmp = load(File)
        
    print 'tmp: ' + str(tmp)
    for (key,value) in tmp.items():
        table_loaded.add_zone(unserialize(value))
    File.close()
    print table_loaded

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
    if isinstance(obj, Table):
        return {"__class__" : "Table",
                "root_zone" : obj.root_zone,
                "zones_map" : obj.zones_map.values(),
                "blue_robots" : obj.blue_robots,
                "red_robots": obj.red_robots,
                "elements" : obj.elements
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
        
        if obj_dict["__class__"] == "Table":
            obj = Table()
            obj.root_zone = obj_dict["root_zone"]
            for zone in  obj_dict["zones_map"]:
                obj.add_zone(zone)
            obj.red_robots = obj_dict["red_robots"]
            obj.blue_robots = obj_dict["blue_robots"]
            obj.elements = obj_dict["elements"]
            return obj
    else:
        return None

def load_config(config_file):
    if config_file != '':
        table = Table()
        with open(config_file, "r") as conf:
            table  = load(conf, object_hook=unserialize)
        conf.close()
    return table 

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
        dump(table, File, default=serialize, indent=4) 
    File.close()
    
    table_loaded = load_config("test.json")
    print table_loaded

from json import loads,dumps
from Zone import *
from Element import *
from Geometry import *

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
    background.add_child('start_left')
    background.add_child('start_right')
    square = [(0,0), (3000,0), (3000,2000), (0,2000)]
    background.set_polygon(square)

    print 'test zone: '
    print str(background)
   
    a_serialized = dumps(serialize(background))
    print a_serialized
    b = unserialize(loads(a_serialized))
    print b

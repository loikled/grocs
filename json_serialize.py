from json import loads,dumps
import Zone
import Element

def serialize(obj):
    if isinstance(obj, Zone):   
        return {"__class__" : "Zone",
                "items" : obj.items,
                "childrens" : obj.childrens,
                "name" : obj.name,
                "number": obj.number,
                "neighbors" : obj.neighbors,
                "polygon": obj.polygon
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
            obj = Playlist(obj_dict["name"], obj_dict["number"])
            obj.items = obj_dict["items"]
            obj.childrens = obj_dict["childrens"]
            obj.neighbors = obj_dict["neighbors"]
            obj.set_polygon(obj_dict["polygon"])
            return obj
    return objet

if '__name__' == '__main__':
    A = Zone("Background", 1)
    square = [Point(0,0), Point(0,1), Point(1,1), Point(1,0)]
    A.set_polygon(square)
    a_serialized = dumps(serialize(a))
    print a_serialized
    b = unserialize(loads(a_serialized))
    print b

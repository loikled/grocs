class zone:
    states = ["free", "taken"]

    def __init__(self, name = 'zone', number = 0):
        self.items = []
        self.state = "free"
        self.is_crossable = True
        self.childrens = []
        self.neighbors = []
        self.number = number
        self.name = name

    def add_child(self, subzone):
        self.childrens.append(subzone)
    
    def add_item(self, item):
        self.items.append(item)

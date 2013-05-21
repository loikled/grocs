class element:
    states = ['reseted','activated']
    def __init__(self, owner = 'everyone', name = 'item',  points = 0, zone = None):
        self.image_path = ""
        self.owner = owner
        self.state = 'reseted'
        self.moveable = True
        self.contains = []
        self.upper_in_stack = None
        self.base_points = points
        self.name = 'item'
        self.number = 0
        self.start_zone = zone
        self.current_zone = self.start_zone

    def condition(self):
        """Condition to gain the item's points based on its state or
        its current_zone at the end of the match"""
        return True
    
    def score(self):
        """return the actual score verifying the condition and managing a stack of elements"""
        score = 0
        if self.condition():
            score += self.base_points
            if self.upper_in_stack != None:
                score += self.upper_in_stack.score()
        return score


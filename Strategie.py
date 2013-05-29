class Strategie :
    idents = 1
    def __init__(self, genome) :
        self.genome = genome
        self.score = 0
        self.ident = Strategie.idents
        Strategie.idents += 1


    def do_strat(self) :
        self.score = 0
        for i in self.genome :
            self.score += int(i)
    def __repr__(self):
        return "< strat" + str(self.ident) + " | genome : " + self.genome + " | score : " + str(self.score) + " >"

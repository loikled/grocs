class Strategie :
    idents = 1
    genome_length = 9
    def __init__(self, genome) :
        self.genome = genome
        self.score = 0
        self.ident = Strategie.idents
        Strategie.idents += 1
        
    def __repr__(self):
        return "< strat" + str(self.ident) + " | genome : " + self.genome + " | score : " + str(self.score) + " >"

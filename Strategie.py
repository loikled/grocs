class Strategie :
    idents = 1
    def __init__(self, genome) :
        self.genome = genome
        self.score = 0
        self.ident = Strategie.idents
        Strategie.idents += 1
        self.parameters = []
        self.table = []

    def do_strat(self) :
        self.score = 0
        for i in self.genome :
            self.score += int(i)
    def __repr__(self):
        return "< strat" + str(self.ident)  + " | score : " + str(self.score) + " >"


    # variables other_x / other_y / x / y  must be between 0 and 3 (first try)
    def get_strat(self,other_x,other_y,x,y) :
        rank = other_y*6+other_y*6*4+x*6*16+y*6*64
        return int(self.genome[rank:rank+6],2)

    def strategie(self) :
        root = Edge(none)
        for i in range(180) :
            root.add_son(Edge(root))
    



    def create_table(self) :
        for i in range(30) :
            self.table.append([[[[1]]]])
        for i in range(30) :
            for j in range(19) :
                self.table[i].append([[[1]]])
        for i in range(30) :
            for j in range(20) :
                for k in range(29) :
                    self.table[i][j].append([[1]])
        for i in range(30) :
            for j in range(20) :
                for k in range(30) :
                    for l in range(19) :
                        self.table[i][j][k].append([1])
        for i in range(30) :
            for j in range(20) :
                for k in range(30) :
                    for l in range(20) :
                        for m in range(89) :
                            self.table[i][j][k][l].append(1)













                        

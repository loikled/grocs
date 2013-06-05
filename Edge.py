class Edge :

    def __init__(self, father) :
        self.son_list = []
        self.father = father
        self.state = 0
        self.strat_to_use = 0


    def __repr__(self) :
        print " < Edge number : " + edge_id + " >"


    def add_son(self, son) :
        son_list.append(son)

    def get_son(self) :
        if len(self.son_list) == 0 :
            return self.strat_to_use
        else :
            return self.son_list[self.son_list].get_son()
        
    def get_genome(self) :   
        if len(self.son_list) == 0 :
            return str(self.strat_to_use)
        else :
            list_of_strat = ""
            for son in self.son_list :
                list_of_strat += son.get_genome()
            return list_of_strat

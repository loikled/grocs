import random
from Strategie import *

class Reproduction :

    def __init__(self) :
        self.all_strats = []
        self.new_strats = []
        self.cross_over = 1
        self.mutation_rate = 20

    def start_generation(self) :
        self.sort()
        self.kill()
        self.birth()



    def add_strat(self, strategie) :
        self.all_strats.append(strategie);

    def sort(self) :
        for i in range(len(self.all_strats)-1) :
            for j in range(i+1, len(self.all_strats)) :
                if(self.all_strats[i].score<self.all_strats[j].score) :
                    self.all_strats[i],self.all_strats[j] = self.all_strats[j],self.all_strats[i]
    def kill(self) :
        self.all_strats = self.all_strats[0:len(self.all_strats)/2]
        
    def mutation(self, genome) :
        genome = list(genome)
        for count in range((len(genome)*self.mutation_rate)/100) :
            rank = random.randint(0,len(genome)-1)
            genome[rank] = str(1 - int(genome[rank]))
        genome = "".join(genome)
        return genome
    
    def birth(self) :
        random.shuffle(self.all_strats)
        for strat in range(0,len(self.all_strats),2) :
            genome_child_1 = ""
            genome_child_2 = ""
            offset = 0
            for i in range(self.cross_over) :
                new_offset = random.randint(offset+1,Strategie.genome_length-(self.cross_over-i))
                genome_child_1 += self.all_strats[strat+(i%2)].genome[offset:new_offset]
                genome_child_2 += self.all_strats[strat+((i+1)%2)].genome[offset:new_offset]
                offset = new_offset
            genome_child_1 += self.all_strats[strat+((i+1)%2)].genome[offset:]
            genome_child_2 += self.all_strats[strat+(i%2)].genome[offset:]
            self.add_strat(Strategie(self.mutation(genome_child_1)))
            self.add_strat(Strategie(self.mutation(genome_child_2)))
               
           
        
reproduction = Reproduction()

reproduction.add_strat(Strategie('111111111'))
reproduction.add_strat(Strategie('000000000'))
reproduction.add_strat(Strategie('101001110'))
reproduction.add_strat(Strategie('101000000'))
reproduction.all_strats[0].score = 3
reproduction.all_strats[1].score = 4
reproduction.all_strats[2].score = 2
reproduction.all_strats[3].score = 1
reproduction.sort()
print reproduction.all_strats
reproduction.start_generation()
print reproduction.all_strats
reproduction.start_generation()
print reproduction.all_strats
reproduction.start_generation()
print reproduction.all_strats
reproduction.start_generation()
print reproduction.all_strats

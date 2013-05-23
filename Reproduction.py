import random
from Strategie import *

class Reproduction :

    def __init__(self) :
        self.all_strats = []
        self.new_strats = []
        self.cross_over = 1

    def start_generation(self) :
        self.kill()
        self.birth()



    def add_strat(self, strategie) :
        self.all_strats.append(strategie);

   # def sort(self) :

    def kill(self) :
        self.all_strats = self.all_strats[0:len(self.all_strats)/2]
        

    def birth(self) :
        random.shuffle(self.all_strats)
        for strat in range(0,len(self.all_strats),2) :
            genome_child_1 = ""
            genome_child_2 = ""
            offset = 0
            for i in range(self.cross_over) :
                new_offset = random.randint(offset+1,Strategie.genome_length-(self.cross_over-i))
                print new_offset
                genome_child_1 += self.all_strats[strat+(i%2)].genome[offset:new_offset]
                genome_child_2 += self.all_strats[strat+((i+1)%2)].genome[offset:new_offset]
                offset = new_offset
            genome_child_1 += self.all_strats[strat+((i+1)%2)].genome[offset:]
            genome_child_2 += self.all_strats[strat+(i%2)].genome[offset:]
            self.add_strat(Strategie(genome_child_1))
            self.add_strat(Strategie(genome_child_2))
               
           
        
reproduction = Reproduction()

reproduction.add_strat(Strategie('111111111'))
reproduction.add_strat(Strategie('000000000'))
reproduction.add_strat(Strategie('101001110'))
reproduction.add_strat(Strategie('101000000'))


print reproduction.all_strats
reproduction.start_generation()
print reproduction.all_strats
reproduction.start_generation()
print reproduction.all_strats
reproduction.start_generation()
print reproduction.all_strats
reproduction.start_generation()
print reproduction.all_strats

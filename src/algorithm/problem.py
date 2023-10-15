from typing import Callable
from .chromosome import Chromosome

class Problem:
    
    def __init__(self, 
            gene_interval: (float, float), 
            gene_length: int, 
            population_length: int, 
            evaluation_function: Callable[[Chromosome], float]):
        self.gene_interval = gene_interval
        self.gene_length = gene_length
        self.population_length = population_length
        self.population = []
        self.evaluation_function = evaluation_function

    def do_cycle(self):
        # todo
        pass
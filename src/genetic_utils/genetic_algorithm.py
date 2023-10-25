from typing import Callable, Iterable, List
from .chromosome import Chromosome
from .gene import Gene
from .utils import custom_sorted, show_time, AbsoluteSolutionFoundException
from random import uniform, random, choices, binomialvariate

class GeneticAlgorithm:
    
    def __init__(
            self, 
            gene_interval: (int, int), 
            chromosome_length: int, 
            population_length: int, 
            mutation_probability: float,
            mutation_function: Callable[[Gene], Gene],
            not_mutated_count: int,
            crossover_probability: float,
            crossover_function: Callable[[Chromosome, Chromosome], [Chromosome, Chromosome]],
            evaluation_function: Callable[[Chromosome], float],
            get_probabilities: Callable[[List[Chromosome]], float],
            is_absolute_solution_found: Callable[[List[Chromosome]], bool]):
        self.gene_interval = gene_interval
        self.chromosome_length = chromosome_length
        self.population_length = population_length
        self.population = []
        self.mutation_probability = mutation_probability
        self.mutation_function = mutation_function
        self.not_mutated_count = not_mutated_count
        self.crossover_probability = crossover_probability
        self.crossover_function = crossover_function
        self.evaluation_function = evaluation_function
        self.get_probabilities = get_probabilities
        self.is_absolute_solution_found = is_absolute_solution_found

    @show_time
    def do_cycle(self):
        if self.is_absolute_solution_found(self.population):
            raise AbsoluteSolutionFoundException
        parents = self.do_selection()
        successors = self.do_crossover(parents)
        self.population = self.do_mutation(successors)
        print(f"best chromosome: {self.get_best()}")
        return self.get_best()

    # done
    def do_mutation(self, successors: Iterable[Chromosome]) -> List[Chromosome]:
        evaluation_function = self.evaluation_function
        mutation_probability = self.mutation_probability
        mutation_function = self.mutation_function
        not_mutated_count = self.not_mutated_count
        population_length = self.population_length
        chromosome_length = self.chromosome_length
        
        
        sorted_successors = custom_sorted( \
            successors, 
            lambda x, y: evaluation_function(x) > evaluation_function(y))
        
        not_mutated = [sorted_successors[i] for i in range(not_mutated_count)]
        mutated = []
        for i in range(not_mutated_count, population_length):
            chromosome = sorted_successors[i]
            new_gene_sequence = []
            for j in range(chromosome_length):
                gene = chromosome.get_gene(j)
                random_number = random()
                if random_number <= mutation_probability:
                    new_gene_sequence.append(mutation_function(gene))
                else: 
                    new_gene_sequence.append(gene)
                    
            mutated.append(Chromosome(new_gene_sequence))
            
        return not_mutated + mutated
    
    # done
    def do_crossover(self, parents: Iterable[Chromosome]) -> List[Chromosome]:
        crossover_probability = self.crossover_probability
        crossover_function = self.crossover_function
        
        successors = []
        prerequisites = []
        for p in parents:
            prerequisites.append(p)
            if len(prerequisites) == 2:
                random_number = random()
                if random_number <= crossover_probability:
                    crossovered = crossover_function(*prerequisites)
                    successors.extend(crossovered)
                else:
                    successors.extend(prerequisites)
                prerequisites = []
        successors.extend(prerequisites)
        
        return successors
    
    # done
    def do_selection(self) -> List[Chromosome]:
        population = self.population
        population_length = self.population_length
        evaluation_function = self.evaluation_function
        get_probabilities = self.get_probabilities
        
        probabilities = get_probabilities(population)
        
        try:
            parents = choices(population, probabilities, k=population_length)
            return parents
        except:
            pass

    # done
    def generate_population(self):
        new_gene_sequences = [ \
            [Gene(int(uniform(*self.gene_interval))) \
                for j in range(self.chromosome_length)] \
                    for i in range(self.population_length)]
        self.population = [Chromosome(x) for x in new_gene_sequences]

    # done
    @show_time
    def do_cycles(self, cycle_count):
        self.generate_population()
        for i in range(cycle_count):
            try:
                print(f"cycle {i + 1}: ")
                self.do_cycle()
            except AbsoluteSolutionFoundException:
                print(f"cycle halted: the absolute solution was found: {self.get_best()}")
                break
    
    # done
    def show_population(self):
        print('show_population: population contains:')
        for i, x in enumerate(self.population):
            print(f'index={i}: chromosome={x}')
        print('--------End--------')
    
    #  done
    def get_best(self):
        population = self.population
        evaluation_function = self.evaluation_function
        best = None
        best_value = 0
        for chromosome in population:
            value = evaluation_function(chromosome)
            best, best_value = (chromosome, value) \
                    if best is None or value > best_value \
                    else (best, best_value)
        return best
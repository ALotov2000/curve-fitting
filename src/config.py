from genetic_utils import Gene, Chromosome
from typing import List
from random import uniform
class Config:
    def __init__(
            self,
            gene_interval: (Gene, Gene),
            chromosome_length: int,
            examples: (int, int),
            population_length: int,
            mutation_probability: float,
            not_mutated_count: int,
            crossover_probability: float):
        self.population_length = population_length
        self.mutation_probability = mutation_probability
        self.not_mutated_count = not_mutated_count
        self.crossover_probability = crossover_probability
        def mutation_function(gene: Gene) -> Gene:
            return Gene(int(uniform(*gene_interval)))
        self.mutation_function = mutation_function
        def crossover_function(
                chromosome1: Chromosome, 
                chromosome2: Chromosome) -> [Chromosome, Chromosome]:
            gene_sequence1 = []
            gene_sequence2 = []
            choice_vector = [chromosome1, chromosome2]
            for i in range(chromosome_length):
                if i == int(chromosome_length / 2):
                    choice_vector = choice_vector[::-1]
                gene_sequence1.append(choice_vector[0].get_gene(i))
                gene_sequence2.append(choice_vector[1].get_gene(i))

            new_chromosome1 = Chromosome(gene_sequence1)
            new_chromosome2 = Chromosome(gene_sequence2)
            return [new_chromosome1, new_chromosome2]
        self.crossover_function = crossover_function
        def evaluation_function(chromosome: Chromosome) -> float:
            calculated_value = 0
            for example in examples:
                x, y = example
                f_x = 0
                for i in range(chromosome_length):
                    gene = chromosome.get_gene(i)
                    f_x += gene.value * (x ** i)
                calculated_value -= abs(y - f_x)
            return calculated_value
        self.evaluation_function = evaluation_function
        def get_probabilities(population: List[Chromosome]) -> List[float]:
            values = [evaluation_function(chromosome) \
                for chromosome in population]
            value_times_probabilities = 1 / sum([1 / x for x in values])
            probabilities = [value_times_probabilities / x for x in values]
            return probabilities
        self.get_probabilities = get_probabilities
        def is_absolute_solution_found(population: List[Chromosome]) -> bool:
            for chromosome in population:
                if evaluation_function(chromosome) == 0:
                    return True
            return False
        self.is_absolute_solution_found = is_absolute_solution_found
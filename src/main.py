from genetic_utils import GeneticAlgorithm
from config import Config

print("---problem description---")
chromosome_length = int(input("polynomial degree: ")) + 1
gene_interval = tuple(map(int, input("coefficients' interval: ").split()))
example_count = int(input("number of examples: "))
examples = []
for i in range(example_count):
    point = tuple(
            map(int, input(f"point corresponding example {i}: ").split())
            )
    examples.append(point)
    
print("---problem description saved---")

population_length = int(input("population_length: "))
mutation_probability = float(input("mutation_probability: "))
not_mutated_count = int(input("not_mutated_count: "))
crossover_probability = float(input("crossover_probability: "))
config = Config(
        gene_interval, 
        chromosome_length, 
        examples, 
        population_length,
        mutation_probability,
        not_mutated_count,
        crossover_probability)
print("---algorithm specification done---")

algorithm = GeneticAlgorithm(
        gene_interval,
        chromosome_length,
        config.population_length,
        config.mutation_probability,
        config.mutation_function,
        config.not_mutated_count,
        config.crossover_probability,
        config.crossover_function,
        config.evaluation_function,
        config.get_probabilities,
        config.is_absolute_solution_found)
print("---instantiating genetic algorithm done---")

print("---almost ready---")
cycle_count = int(input("number of cycles: "))
algorithm.generate_population()
algorithm.do_cycles(cycle_count)
algorithm.show_population()
print(algorithm.get_best())
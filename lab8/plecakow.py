import pygad
import numpy
from measure_time import measure_time
import math

LIMIT = 25
CHROM_POPULATION = 10
MATING_RATE = 0.5
GENERATIONS = 40
KEEP_PARENTS = 0.05
SELECTION_TYPE = "sss"
CROSSOVER_TYPE = "single_point"
MUTATION_TYPE = "random"
MUTATION_RATE = 0.05


@measure_time(rounding_precision=2)
def solve_knapsack(suppress_plot: bool = False) -> float:
    backpack = [(100, 7), (300, 7), (200, 6), (40, 2), (500, 5), (70, 6), (100, 1), (250, 3), (300, 10), (280, 3), (300, 15)]
    gene_space = [0, 1]
    genes = len(backpack)

    smallest_value = min([tup[0] for tup in backpack])
    def fitness(model: pygad.GA, solution: list[int], solution_index: int) -> float:
        weight = sum([backpack[i][1] if solution[i] == 1 else 0 for i in range(len(solution))])
        value = sum([backpack[i][0] if solution[i] == 1 else 0 for i in range(len(solution))])
        diff = weight - LIMIT
        if diff > 0:
            return math.log2(pow(value, 8)) - pow(diff, 2)
        else:
            diff = -diff
            return value - diff * smallest_value
        
    mating_parents = int(round(MATING_RATE * CHROM_POPULATION))
    keep_parents = int(round(KEEP_PARENTS * CHROM_POPULATION))

    ga = pygad.GA(
        gene_space=gene_space,
        num_generations=GENERATIONS,
        num_parents_mating=mating_parents,
        fitness_func=fitness,
        sol_per_pop=CHROM_POPULATION,
        num_genes=genes,
        parent_selection_type=SELECTION_TYPE,
        keep_parents=keep_parents,
        crossover_type=CROSSOVER_TYPE,
        mutation_type=MUTATION_TYPE,
        mutation_percent_genes=MUTATION_RATE
    )

    ga.run()
    solution, solution_fitness, _ = ga.best_solution()
    
    print(f"Best solution: {solution}")
    print(f"Best fitness score: {solution_fitness}")
    best_value = sum([backpack[i][0] if solution[i] == 1 else 0 for i in range(len(solution))])
    print(f"Output based on best solution: {best_value}")

    if not suppress_plot:
        ga.plot_fitness()





def main() -> None:
    # solve_knapsack() # pojedyncze wykonanie z wykresem fitness
    for i in range(10):
        print(f"---= Attempt {i+1}/10 =---")
        solve_knapsack(suppress_plot=True)
        print()


if __name__ == "__main__":
    main()

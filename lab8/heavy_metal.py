import pygad
from measure_time import measure_time
import math


CHROM_POPULATION = 10
MATING_RATE = 0.5
GENERATIONS = 60
KEEP_PARENTS = 0.05
SELECTION_TYPE = "sss"
CROSSOVER_TYPE = "single_point"
MUTATION_TYPE = "random"
MUTATION_RATE = 0.15


def mean(arr: list[float]) -> float:
    result = 0
    for elem in arr:
        result += elem
    return result / len(arr)


def endurance(x: float, y, z, u, v, w) -> float:
    return math.exp(-2*(y-math.sin(x))**2)+math.sin(z*u)+math.cos(v*w)


def fitness(model: pygad.GA, solution: list[float], solution_index: int) -> float:
    return endurance(*solution)


@measure_time(rounding_precision=2)
def solve_alloy(suppress_plot: bool = False) -> float:
    gene_space = {"low": 0, "high": 1}
    genes = 6

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
    print(f"Best endurance: {solution_fitness}")

    if not suppress_plot:
        ga.plot_fitness()



def main() -> None:
    # solve_alloy() # pojedyncze wykonanie z wykresem fitness

    times = []
    for i in range(20):
        print(f"---= Attempt {i+1}/10 =---")
        times.append(solve_alloy(suppress_plot=True))
        print()
    
    print(f"Average execution time: {round(mean(times), 2)}ms")



if __name__ == "__main__":
    main()
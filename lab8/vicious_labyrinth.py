import pygad
from measure_time import measure_time
import math


GRID_HEIGHT = 12
GRID_WIDTH = 12
LIMIT = 30
CHROM_POPULATION = 70
MATING_RATE = 0.5
GENERATIONS = 200
KEEP_PARENTS = 0.05
SELECTION_TYPE = "sss"
CROSSOVER_TYPE = "single_point"
MUTATION_TYPE = "random"
MUTATION_RATE = 0.15
TEST_SAMPLES = 20


def print_labyrinth(labyrinth, spaces, solution):
    for i in range(GRID_HEIGHT):
        for j in range(GRID_WIDTH):
            part_of_solution = False
            for k in range(len(spaces)):
                if spaces[k] == (i, j) and solution[k] == 1:
                    part_of_solution = True
                    print("▫", end=" ")
            if not part_of_solution:
                print("◼" if labyrinth[i][j] == 1 else " ", end=" ")
        print()
            


def mean(arr: list[float]) -> float:
    result = 0
    for elem in arr:
        result += elem
    return result / len(arr)


@measure_time(rounding_precision=2, return_solution=True)
def solve_labyrinth(spaces: list[tuple[int, int]], start: tuple[int, int], end: tuple[int, int], suppress_plot: bool = False) -> float:
    gene_space = [0, 1]
    genes = len(spaces)


    def has_neighbours(solution: list[int], coords: tuple[int, int]) -> int:
        neighbours = 0
        for i in range(len(spaces)):
            space = spaces[i]
            if ((abs(space[0] - coords[0]) == 1 and space[1] == coords[1]) or (space[0] == coords[0] and abs(space[1] - coords[1]) == 1)):
                if solution[i] == 1:
                    neighbours += 1
            if neighbours == 2:
                return 2
        return neighbours


    def fitness(model: pygad.GA, solution: list[int], solution_index: int) -> float:
        if sum(solution) > LIMIT: return 1 / (sum(solution) - LIMIT)
        hit_start = False
        hit_end = False
        modifier = 1
        zero_neighbours = 0
        one_neighbour = 0
        two_neighbours = 0

        for i in range(len(spaces)):
            space = spaces[i]
            if solution[i] == 1:
                neighbours = has_neighbours(solution, space)
                if space == start and solution[i] == 1:
                    hit_start = True
                elif space == end and solution[i] == 1:
                    hit_end = True

                if neighbours == 2:
                    two_neighbours += 1
                elif neighbours == 1:
                    one_neighbour += 1
                else:
                    zero_neighbours += 1
        
        if not hit_start: modifier *= 0.1
        if not hit_end: modifier *= 0.1
        elif hit_end and hit_start and one_neighbour < 2: modifier *= 0.1
        if hit_start and hit_end and zero_neighbours == 0 and one_neighbour == 2 and two_neighbours >= 2:
            return pow(LIMIT + 4 - two_neighbours, 2)
        else:
            result = modifier * (LIMIT*2 - (one_neighbour - 2) - zero_neighbours*2)
            return 1.5 if 1.5 > result else result
        

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
    print(f"Best fitness: {solution_fitness}")
    print(f"Route Length: {sum(solution)}")

    if not suppress_plot:
        ga.plot_fitness()
    
    return (solution, solution_fitness)



def main() -> None:
    labyrinth = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
                 [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
                 [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                 [1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
                 [1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
                 [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
                 [1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
                 [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1],
                 [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
                 [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    start = (1, 1); end = (10, 10)

    spaces = []
    for row in range(GRID_HEIGHT):
        for elem in range(GRID_WIDTH):
            if labyrinth[row][elem] == 0:
                spaces.append((row, elem))


    # solve_labyrinth(spaces, start, end) # pojedyncze wykonanie z wykresem fitness

    solutions = []
    for i in range(TEST_SAMPLES):
        print(f"---= Attempt {i+1}/{TEST_SAMPLES} =---")
        solutions.append(solve_labyrinth(spaces, start, end, suppress_plot=True))
    
    best_fitness = 0
    for solution in solutions:
        if solution[1] > best_fitness:
            best_fitness = solution[1]
    best_solution = []
    for solution in solutions:
        if solution[1] == best_fitness:
            best_solution = solution[0]

    print_labyrinth(labyrinth, spaces, best_solution)



if __name__ == "__main__":
    main()
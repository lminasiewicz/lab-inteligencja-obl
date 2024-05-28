import matplotlib.pyplot as plt
import random

from aco import AntColony


plt.style.use("dark_background")

random.seed(727)
COORDS = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(15)]


def plot_nodes(w=12, h=8):
    for x, y in COORDS:
        plt.plot(x, y, "g.", markersize=15)
    plt.axis("off")
    fig = plt.gcf()
    fig.set_size_inches([w, h])


plot_nodes()

colony = AntColony(COORDS, ant_count=100, alpha=1, beta=1, 
                    pheromone_evaporation_rate=0.40, pheromone_constant=1000.0,
                    iterations=10)

optimal_nodes = colony.get_path()

for i in range(len(optimal_nodes) - 1):
    plt.plot(
        (optimal_nodes[i][0], optimal_nodes[i + 1][0]),
        (optimal_nodes[i][1], optimal_nodes[i + 1][1]),
    )

# 25 nodes, random state 727, Beta = 4* alpha
# ~589.379 notably weird moves in a couple places

# 25 nodes, random state 727, Alpha = 4* beta
# ~589.379 notably weird moves in a couple places (nothing changed?)

# 25 nodes, random state 727, Beta = alpha
# ~589.379 notably weird moves in a couple places (again)

# 15 nodes, random state 727, Beta = 4* alpha
# ~445.415 notably weird moves in a couple places

# 15 nodes, random state 727, Alpha = 4* beta
# ~445.415 notably weird moves in a couple places (nothing changed)

# 25 nodes, random state 727, Beta = alpha + 0.2 pheromone evaporation
# ~445.415

# Chyba rozumiem jaki jest problem. Ale troszkę nie mam czasu puścić tego jeszcze te kilka razy.


plt.show()
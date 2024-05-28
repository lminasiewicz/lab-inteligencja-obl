import math
import numpy as np
from matplotlib import pyplot as plt
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import plot_cost_history

DIMENSIONS = 6
N_PARTICLES = 10
ITERATIONS = 100

options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}

def endurance_optimization(particles: np.ndarray):
    # particles: np.ndarray(shape=(N_PARTICLES, DIMENSIONS))
    def endurance(x, y, z, u, v, w):
        return -math.exp(-2*(y-math.sin(x))**2)+math.sin(z*u)+math.cos(v*w)
    
    results = np.ndarray(shape=(N_PARTICLES,), dtype=np.float32)
    for i in range(len(particles)):
        results[i] = endurance(*particles[i])
    
    return results

optimizer = ps.single.GlobalBestPSO(n_particles=N_PARTICLES, dimensions=DIMENSIONS, options=options)

cost, pos = optimizer.optimize(endurance_optimization, iters=ITERATIONS)
print(f"Best value: {-cost}")

cost_history = optimizer.cost_history
plot_cost_history(cost_history)
plt.show()
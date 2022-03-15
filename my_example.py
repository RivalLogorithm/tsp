import numpy as np
import tsp
from python_tsp.exact import solve_tsp_dynamic_programming
from python_tsp.heuristics import solve_tsp_simulated_annealing

import time
import random

def by_tsp(mat):
    start_time = time.time()
    r = range(len(mat))
    # Dictionary of distance
    dist = {(i, j): mat[i][j] for i in r for j in r}
    print(time.time()-start_time)
    print(tsp.tsp(r, dist))



def by_python_tsp_dynamic(distance_matrix):
    start_time = time.time()
    permutation, distance = solve_tsp_dynamic_programming(distance_matrix)
    print(time.time() - start_time)
    print(permutation, distance)


def by_python_tsp_metaheuristic(distance_matrix):
    start_time = time.time()
    permutation, distance = solve_tsp_simulated_annealing(distance_matrix)
    print(time.time() - start_time)
    print(permutation, distance)


distance_matrix = np.array([[0, 20, 18, 12, 8],
                   [5, 0, 14, 7, 11],
                   [12, 18, 0, 6, 11],
                   [11, 17, 11, 0, 12],
                   [5, 5, 5, 5, 0]])

N = 20
big_matrix = np.array([[random.randint(5, 30) for i in range(N)] for j in range(N)])
# distance_matrix = [[0, 20, 18, 12, 8],
#                    [5, 0, 14, 7, 11],
#                    [12, 18, 0, 6, 11],
#                    [11, 17, 11, 0, 12],
#                    [5, 5, 5, 5, 0]]

print("5 cities")
by_python_tsp_dynamic(distance_matrix)
by_python_tsp_metaheuristic(distance_matrix)

by_tsp(distance_matrix)

print("20 cities")
by_python_tsp_dynamic(big_matrix)
by_python_tsp_metaheuristic(big_matrix)

by_tsp(big_matrix)

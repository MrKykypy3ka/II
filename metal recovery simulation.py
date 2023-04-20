import random
import math


def f(x, y):
    return 1 / (1 + x ** 2 + y ** 2)


def simulated_annealing(f, x, y, T=1, T_min=0.00001, alpha=0.9, iterations=1000):
    best_x, best_y = x, y
    best_score = f(x, y)
    while T > T_min:
        for i in range(iterations):
            delta_x = random.uniform(-1, 1) * T
            delta_y = random.uniform(-1, 1) * T
            neighbor_x, neighbor_y = x + delta_x, y + delta_y
            neighbor_score = f(neighbor_x, neighbor_y)
            acceptance_prob = math.exp((neighbor_score - best_score) / T)
            if neighbor_score > best_score or random.random() < acceptance_prob:
                best_x, best_y = neighbor_x, neighbor_y
                best_score = neighbor_score
            T *= alpha
    return best_x, best_y, best_score


x, y, score = simulated_annealing(f, 0, 0)
print("Best x: ", x)
print("Best y: ", y)
print("Best score: ", score)
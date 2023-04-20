import random

POPULATION_SIZE = 20
NUM_GENERATIONS = 100
MUTATION_RATE = 0.1
ELITE_RATIO = 0.2
CROSSOVER_POINTS = 1

def fitness_function(x, y):
    return 1 / (1 + x**2 + y**2)

def generate_initial_population(population_size):
    population = []
    for i in range(population_size):
        x = random.uniform(-10, 10)
        y = random.uniform(-10, 10)
        population.append((x, y))
    return population

def select_parents(sorted_population, num_parents):
    fitness_scores = [fitness_function(x, y) for (x, y) in sorted_population]
    fitness_sum = sum(fitness_scores)
    fitness_probs = [score/fitness_sum for score in fitness_scores]
    parent1_index = random.choices(range(POPULATION_SIZE), weights=fitness_probs)[0]
    parent2_index = random.choices(range(POPULATION_SIZE), weights=fitness_probs)[0]
    return sorted_population[parent1_index], sorted_population[parent2_index]

def crossover(parent1, parent2):
    child = []
    for i in range(len(parent1)):
        if random.random() < 0.5:
            child.append(parent1[i])
        else:
            child.append(parent2[i])
    return tuple(child)

def mutate(individual):
    mutated = []
    for i in range(len(individual)):
        if random.random() < MUTATION_RATE:
            mutated.append(random.uniform(-10, 10))
        else:
            mutated.append(individual[i])
    return tuple(mutated)

def select_new_population(sorted_population, elite_fitness_scores):
    num_elite = int(ELITE_RATIO * POPULATION_SIZE)
    elite_population = sorted_population[:num_elite]
    new_population = elite_population
    while len(new_population) < POPULATION_SIZE:
        parent1, parent2 = select_parents(sorted_population, 2)
        child = crossover(parent1, parent2)
        child = mutate(child)
        new_population.append(child)
    return new_population

def run_genetic_algorithm():
    population = generate_initial_population(POPULATION_SIZE)
    for generation in range(NUM_GENERATIONS):
        sorted_population = sorted(population, key=lambda ind: fitness_function(ind[0], ind[1]), reverse=True)
        elite_population = sorted_population[:int(ELITE_RATIO * POPULATION_SIZE)]
        elite_fitness_scores = [fitness_function(x, y) for (x, y) in elite_population]
        best_individual = sorted_population[0]
        print(f"Generation {generation}: Best individual = {best_individual}, Fitness = {fitness_function(*best_individual)}")
        population = select_new_population(sorted_population, elite_fitness_scores)


if __name__ == '__main__':
    run_genetic_algorithm()
import numpy as np
import random

# Определение глобальных параметров
NUM_INPUTS = 2
POPULATION_SIZE = 100
NUM_GENERATIONS = 50
MUTATION_PROBABILITY = 0.05


# Определение функции активации (ступенчатая)
def step(x):
    return 1 if x > 0 else 0


# Определение класса перцептрона
class Perceptron:
    def __init__(self, weights):
        self.weights = weights

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        return step(summation)


# Определение функции для расчета приспособленности (fitness) каждой особи
def fitness_function(individual, X, y):
    perceptron = Perceptron(individual)
    predictions = np.array([perceptron.predict(x) for x in X])
    accuracy = np.mean(predictions == y)
    return accuracy


# Определение функции для создания случайной особи (весов перцептрона)
def generate_random_individual():
    return np.random.uniform(low=-1, high=1, size=NUM_INPUTS + 1)


# Определение функции для селекции родителей
def select_parent(population, fitness_scores):
    return random.choices(population, weights=fitness_scores)[0]


# Определение функции для операции кроссовера (одноточечный)
def crossover(parent_1, parent_2):
    split_point = random.randint(1, NUM_INPUTS + 1)
    child = np.concatenate((parent_1[:split_point], parent_2[split_point:]))
    return child


# Определение функции для операции мутации (замена веса случайным значением)
def mutation(individual):
    if random.random() < MUTATION_PROBABILITY:
        index = random.randint(0, NUM_INPUTS)
        individual[index] = np.random.uniform(low=-1, high=1)
    return individual


# Генетический алгоритм для обучения перцептрона
def genetic_algorithm(X, y):
    # Инициализация начальной популяции случайными весами перцептрона
    population = [generate_random_individual() for _ in range(POPULATION_SIZE)]

    for generation in range(NUM_GENERATIONS):
        # Вычисление приспособленности каждой особи в популяции
        fitness_scores = [fitness_function(individual, X, y) for individual in population]
        # Определение элитной особи (с наибольшей приспособленностью)
        elite_index = np.argmax(fitness_scores)
        elite = population[elite_index]
        # Создание новой популяции
        new_population = [elite]
        while len(new_population) < POPULATION_SIZE:
            # Селекция двух родителей
            parent_1 = select_parent(population, fitness_scores)
            parent_2 = select_parent(population, fitness_scores)
            while np.array_equal(parent_2, parent_1):
                parent_2 = select_parent(population, fitness_scores)
            # Кроссовер и мутация для создания потомка
            child = crossover(parent_1, parent_2)
            child = mutation(child)
            new_population.append(child)
            # Обновление популяции
        population = new_population

        # Вычисление приспособленности каждой особи в финальной популяции
        fitness_scores = [fitness_function(individual, X, y) for individual in population]
        # Определение лучшей особи (с наибольшей приспособленностью)
        best_index = np.argmax(fitness_scores)
        best_individual = population[best_index]
        best_accuracy = fitness_scores[best_index]

        return Perceptron(best_individual), best_accuracy


X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([0, 1, 1, 1])

perceptron, accuracy = genetic_algorithm(X, y)

print("Weights:", perceptron.weights)
print("Accuracy:", accuracy)
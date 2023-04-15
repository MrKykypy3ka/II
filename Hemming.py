def hamming_distance(x, y):
    """
    Функция расстояния Хемминга между двумя бинарными векторами
    """
    assert len(x) == len(y), "Длины векторов не совпадают"
    return sum(1 for a, b in zip(x, y) if a != b)


class HammingNetwork:
    def __init__(self, num_neurons, num_bits):
        """
        Конструктор сети.
        num_neurons - количество нейронов в сети.
        num_bits - количество бит во входном векторе.
        """
        self.num_neurons = num_neurons
        self.num_bits = num_bits
        self.weights = [[0] * num_bits for _ in range(num_neurons)]

    def train(self, patterns):
        """
        Метод обучения сети на наборе образов.
        patterns - список бинарных векторов, на которых будет обучаться сеть.
        """
        assert len(patterns) <= self.num_neurons, "Количество образов больше, чем количество нейронов"
        for i, p in enumerate(patterns):
            self.weights[i] = p

    def recognize(self, pattern):
        """
        Метод распознавания образа.
        pattern - бинарный вектор, который нужно распознать.
        """
        distances = [hamming_distance(pattern, w) for w in self.weights]
        print(f"Расстояния: {distances}")  # Добавленный вывод
        min_distance = min(distances)
        if distances.count(min_distance) == 1:
            return distances.index(min_distance)
        else:
            return None


network = HammingNetwork(num_neurons=4, num_bits=4)

# Обучаем сеть на некоторых образах
patterns = [[1, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 1, 1, 0],
            [1, 0, 0, 1]]

network.train(patterns)
new_pattern = [1, 0, 1, 0]
recognized_neuron = network.recognize(new_pattern)

if recognized_neuron is not None:
    print(f"Образ распознан как нейрон {recognized_neuron}")
else:
    print("Образ не распознан")
import numpy as np


class Cogitron:
    def __init__(self, input_shape, output_shape):
        self.input_shape = input_shape
        self.output_shape = output_shape
        self.weights = np.zeros((input_shape[0] * input_shape[1], output_shape))

    def forward(self, input):
        self.input = input.reshape(-1)
        self.net_input = np.dot(self.input, self.weights)
        self.output = np.where(self.net_input >= 0, 1, 0)
        return self.output.reshape(self.output_shape)

    def train(self, inputs, labels, epochs=10, learning_rate=0.1):
        for epoch in range(epochs):
            for input, label in zip(inputs, labels):
                output = self.forward(input)
                error = label - output
                delta_weights = learning_rate * np.outer(self.input, error)
                self.weights += delta_weights.reshape(self.weights.shape)


# создаем объект Cogitron с размерностью входного и выходного слоев 5x5 и 2 соответственно
cogitron = Cogitron((5, 5), 2)

# задаем обучающие примеры и соответствующие метки
inputs = np.array([
    [[0, 1, 1, 1, 0],
     [0, 0, 0, 0, 1],
     [0, 0, 0, 0, 1],
     [0, 0, 0, 1, 0],
     [0, 0, 1, 0, 0]],

    [[1, 1, 1, 1, 1],
     [1, 0, 0, 0, 0],
     [1, 1, 1, 1, 0],
     [0, 0, 0, 0, 1],
     [1, 1, 1, 1, 0]]
])

labels = np.array([
    [1, 0],
    [0, 1]
])

# обучаем сеть
cogitron.train(inputs, labels, epochs=100)


# тестируем сеть на новых образах
test_inputs = np.array([
    [[1, 0, 0, 0, 1],
     [0, 1, 0, 1, 0],
     [0, 0, 1, 0, 0],
     [0, 1, 0, 1, 0],
     [1, 0, 0, 0, 1]],

    [[0, 0, 1, 1, 0],
     [0, 1, 0, 0, 1],
     [1, 0, 0, 0, 1],
     [0, 1, 0, 0, 1],
     [0, 0, 1, 1, 0]]
])

for input in test_inputs:
    output = cogitron.forward(input)
    print(output)


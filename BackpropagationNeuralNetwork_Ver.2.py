import numpy as np
from sklearn.datasets import load_digits
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split

digits = load_digits()


X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)

encoder = LabelBinarizer()
y_train = encoder.fit_transform(y_train)
y_test = encoder.transform(y_test)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.weights1 = np.random.randn(input_size, hidden_size)
        self.weights2 = np.random.randn(hidden_size, output_size)
        self.bias1 = np.random.randn(hidden_size)
        self.bias2 = np.random.randn(output_size)

    def forward(self, inputs):
        self.hidden = sigmoid(np.dot(inputs, self.weights1) + self.bias1)
        self.output = sigmoid(np.dot(self.hidden, self.weights2) + self.bias2)

    def backward(self, inputs, targets, learning_rate):
        error = targets - self.output
        d_output = error * sigmoid_derivative(self.output)
        error_hidden = np.dot(d_output, self.weights2.T)
        d_hidden = error_hidden * sigmoid_derivative(self.hidden)

        self.weights2 += learning_rate * np.dot(self.hidden.T, d_output)
        self.bias2 += learning_rate * np.sum(d_output, axis=0)
        self.weights1 += learning_rate * np.dot(inputs.T, d_hidden)
        self.bias1 += learning_rate * np.sum(d_hidden, axis=0)

    def train(self, inputs, targets, learning_rate):
        self.forward(inputs)
        self.backward(inputs, targets, learning_rate)

    def predict(self, inputs):
        self.forward(inputs)
        return np.argmax(self.output, axis=1)



input_size = X_train.shape[1]
hidden_size = 16
output_size = len(digits.target_names)
nn = NeuralNetwork(input_size, hidden_size, output_size)


epochs = 1000
learning_rate = 0.1

for i in range(epochs):
    nn.train(X_train, y_train, learning_rate)


y_pred = nn.predict(X_test)


accuracy = np.mean(y_pred == y_test)
print("Accuracy:", accuracy)

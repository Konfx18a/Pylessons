import math

import numpy as np
def activatoin_function(x):
    return math.tan(x)

class Perceptron:

    def __init__(self, input_size, lening_rate=0.01, iters=0, hidden_layer_sizes=(100,), weights_func="adam"):
        self.biases = np.random.sample(hidden_layer_sizes+1)
        self.weights_func = weights_func
        self.h_layers = hidden_layer_sizes[0]
        self.neorons_number=hidden_layer_sizes[1]
        self.lening_rate = lening_rate
        self.weights = np.zeros(input_size)

    def feed_forward(self, x):

        return activatoin_function(np.dot(x, self.weights)+self.bias)


    def train(self, input_data, target):
        output_data = self.feed_forward(input_data)
        err = target - output_data
        self.weights += err * input_data * self.lening_rate
        self.bias += err * self.lening_rate

        print(f"Входы: {input_data} Выход: {int(output_data)} Ошибка: {err}")


X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])  # Операция XOR

pers = Perceptron(8)
pers.train(X,y)

from sklearn.neural_network import MLPClassifier
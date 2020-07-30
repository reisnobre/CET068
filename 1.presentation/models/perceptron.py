"""
File: perceptron.py
Author: Eduardo Reis Nobre
"""
import random
from numpy import sign


def actvator(_):
    """ Filter the outputs to 1 and -1 """
    return 1 if _ > 0 else -1


class Perceptron:
    """
    Type: Class
    Name: Perceptron
    Description: file with the
    """
    def __init__(self):
        """."""
        self.weights = [random.choice([1, -1]) for _ in range(2)]
        self.learning_rate = 0.1

    def guess(self, inputs):
        """."""
        sums = 0
        pair = list(zip(inputs, self.weights))

        for i_iterator, w_iterator in pair:
            sums += i_iterator * w_iterator

        output = sign(sums)
        return output

    def train(self, inputs, target):
        """."""
        guess = self.guess(inputs)
        error = target - guess

        pair = list(zip(inputs, self.weights))

        for i_iterator, w_iterator in pair:
            w_iterator += error * i_iterator * self.learning_rate

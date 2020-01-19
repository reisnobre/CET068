"""."""
from models.perceptron import Perceptron
from models.point import Point

INPUTS = [-1, 0.5]

PERCEPTRON = Perceptron()

POINTS = [Point() for _ in range(200)]

training_index = 0

for point in POINTS:
    inputs = [point.x, point.y]
    PERCEPTRON.train(inputs, point.label)
    guess = PERCEPTRON.guess(inputs)
    if guess == point.label:
        print('found')
    else:
        print(guess, point.label)

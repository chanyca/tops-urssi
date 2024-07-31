import numpy as np


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def mean(numbers):
    return np.mean(numbers)

numbers = [1, 2, 3]
print(mean(numbers))

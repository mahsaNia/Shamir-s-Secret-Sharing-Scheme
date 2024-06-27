import random
from functools import reduce


def generate(S, t, n, p):
    coefficients = [S] + [random.randint(0, p - 1) for _ in range(t - 1)]

    def random_polynomial(x):
        return sum([coefficients[i] * (x ** i) for i in range(t)]) % p

    shares = [(i, random_polynomial(i)) for i in range(1, n + 1)]
    return shares

import random
from functools import reduce


def generate(S, t, n, p):
    coefficients = [S] + [random.randint(0, p - 1) for _ in range(t - 1)]

    def random_polynomial(x):
        return sum([coefficients[i] * (x ** i) for i in range(t)]) % p

    shares = [(i, random_polynomial(i)) for i in range(1, n + 1)]
    return shares


def reconstruct_secret(shares, p):

    def lagrange_interpolate(x, x_s, y_s, p):
        def product(vals):
            return reduce(lambda x, y: x * y, vals)

        def numerator(i):
            return product(x - x_s[m] for m in range(len(x_s)) if m != i)

        def denominator(i):
            return product(x_s[i] - x_s[m] for m in range(len(x_s)) if m != i)


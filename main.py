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

        k = len(x_s)
        secret = 0
        for i in range(k):
            num = numerator(i)
            den = denominator(i)
            lagrange_basis = (num * pow(den, -1, p)) % p
            secret = (secret + y_s[i] * lagrange_basis) % p

        return secret

    x_s, y_s = zip(*shares)
    return lagrange_interpolate(0, x_s, y_s, p)


# example
S = 9
t = 3
n = 5
p = 13


shares = generate(S, t, n, p)
print("Shares:", shares)

t_shares = shares[:t]
reconstructed_secret = reconstruct_secret(t_shares, p)
print("Reconstructed Secret:", reconstructed_secret)
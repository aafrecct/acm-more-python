"""
Los generadores son objetos que devuelven valores según
se van pidiendo. Son "lazily evaluated", es decir, solo calculan
el valor una vez se pide, en vez de tener todos los valores
calculados de una.

Hay dos formas de crear generadores:
    1. Con funciones y la palabra ``yield``
    2. Con expresiones por comprensión. (Igual que las listas)
"""

# Generador Infinito
def count_fun(start = 0, step = 1):
    while True:
        yield start
        start += step


def get_prime_numbers_fun():
    primes = []
    i = 2
    while i < 100000:
        if all([i % j for j in primes]):
            primes.append(i)
        i += 1
    return primes


def get_prime_numbers_gen():
    primes = []
    i = 2
    while i < 100000:
        if all([i % j for j in primes]):
            primes.append(i)
            yield i
        i += 1


def get_prime_numbers_faster():
    primes = []
    i = 2
    while i < 100000:
        if all((i % j for j in primes)):
            primes.append(i)
            yield i
        i += 1


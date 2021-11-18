"""
Los generadores son objetos que devuelven valores según
se van pidiendo. Son "lazily evaluated", es decir, solo calculan
el valor una vez se pide, en vez de tener todos los valores
calculados de una.

Hay dos formas de crear generadores:
    1. Con funciones y la palabra ``yield``
    2. Con expresiones por comprensión. (Igual que las listas)
"""
from time import time


def count_fun(start = 0, step = 1):
    """
    Veamos primero un generador infinito que cuente
    de forma ascendente.

    Esta funcion recíbe dos argumentos y no tiene la
    palabra return. En su vez, aparece la palabra ``yield``.

    Args:
        start (int): Primer número de la secuencia.
        step (int): Intervalo entre dos números de la
        secuencia.
    """
    while True:
        yield start
        start += step


"""
Al hacer generadores por comprensión, no podemos hacer 
generadores infinitos.
"""
count_100000 = (i for i in range(100000))


def get_prime_numbers_fun():
    """
    Vamos a comparar la velocidad con la que diferentes metodos
    generan los primeros 100000 números primos.
    Primero, vamos a crear una función normal.
    """
    primes = []
    i = 2
    while i < 50000:
        if all([i % j for j in primes]):
            primes.append(i)
        i += 1
    return primes


def get_prime_numbers_gen():
    """
    Ahora vamos a ver que ocurre si hacemos la función un
    generador.
    """
    primes = []
    i = 2
    while i < 50000:
        if all([i % j for j in primes]):
            primes.append(i)
            yield i
        i += 1


def get_prime_numbers_fast():
    """
    Por último veamos que ocurre si en vez de una lista, usamos
    un objeto generador dentro de la función.
    """
    primes = []
    i = 2
    while i < 50000:
        if all((i % j for j in primes)):
            primes.append(i)
            yield i
        i += 1


if __name__ == '__main__':
    print("Numeros Primos:")
    print("Test 1:")
    t = time()
    for i in get_prime_numbers_fun():
        ...
    print("  Total time:", time() - t)

    input("Comenzar segundo test...")

    print("Test 2:")
    t = time()
    for i in get_prime_numbers_gen():
        ...
    print("  Total time:", time() - t)

    input("Comenzar último test...")

    print("Test 3:")
    t = time()
    for i in get_prime_numbers_fast():
        ...
    print("  Total time:", time() - t)

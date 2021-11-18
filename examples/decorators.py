"""
Una vez has programado en Python durante algún tiempo
puedes econtrarte con una anotación con @ antes de la
declaración de una función::

    @do_twice
    def say_hi():
        print("hi")

Esto son decoradores de funciones. ¿Pero que son los
decoradores?
"""


def gimme_function():
    """
    Lo primero que debemos saber es que podemos declarar
    funciones dentro de otras funciones. No solo eso,
    sino que podemos devolver el propio objecto función.
    """    
    def inside_function():
        print("Hola soy la función interna")
    return inside_function


def double_up(function):
    """
    Supongamos que queremos una función que dada otra,
    la devuelva una que haga lo mismo, dos veces.
    Sabiendo lo que sabemos, no debería ser muy dificil.
    """
    def function_but_twice():
        function()
        function()
    return function_but_twice


@double_up
def say_cheers():
    """
    Ahora podemos ver qué es lo que hacen los decoradores.
    Esta función es el equivalente a double_up(say_cheers),
    por lo que imprimirá "Cheers" 2 veces.
    """
    print("Cheers")


class ExecCounter:
    """
    Un decorador tambien puede ser una clase, ya que una 
    clase es "llamable", esto nos permite hacer cosas distintas
    ya que el comportamiento es distinto la primera vez que se 
    llama que el resto.
    """
    def __init__(self, fun):
        self.counter = 0
        self.fun = fun

    def __call__(self):
        self.counter += 1
        print(f"Function has been called {self.counter} times")
        self.fun()

@ExecCounter
def say_hi():
    print("hi")


class ClaseEjemplo:
    """
    Python implementa por defecto dos decoradores para crear
    métodos estaticos y métodos de clase.
    """

    @staticmethod
    def method_one():
        """
        Los métodos estaticos no tienen un argumento 'self'.

        Example::
            
            ClaseEjemplo.method_one()
        """
        ...

    @classmethod
    def method_two(cls):
        """ 
        Los métodos de clase no tienen un argumento 'self',
        en su vez, tienen un argumento 'cls' que se refiere
        a la clase.
        """
        ...


if __name__ == "__main__":
    input("Llamando a 'gimme_function()'")
    print(gimme_function())
    gimme_function()()

    input("Llamando a 'say_cheers()'")
    say_cheers()
    
    input("Llamando a 'say_hi()'")
    say_hi()
    say_hi()
    say_hi()
    say_hi()
    say_hi()


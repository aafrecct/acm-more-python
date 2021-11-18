"""
En Python una clase puede heredar de más de una 
otra clase. Esto se llama herencia múltiple y es útil
para enteder como funcionan algunas librerías.

Aquí vamos a ver en que orden se miran los métodos de una
clase que hereda de muchas otras y como funciona super()
cuando se hereda de otra clase.
"""

class A:
    def __init__(self):
        print("Init de clase A")
        self.dec_order = 1
        self.a = None


class B:
    def __init__(self):
        print("Init de clase B")
        self.dec_order = 2
        self.b = None

    def method_example(self):
        return "Soy una instancia de B"


class C:
    def __init__(self):
        print("Init de clase C")
        self.dec_order = 3
        self.c = None


    def method_example(self):
        return "Soy una instancia de C"


class D(A, B):
    def __init__(self):
        print("Init de clase D")
        super().__init__()
        self.dec_order = 4
        self.d = None



class E(C):
    def __init__(self):
        print("Init de clase E")
        super().__init__()
        self.dec_order = 5
        self.e = None


class F(D, E):
    def __init__(self):
        print("Init de clase F")
        super().__init__()

        print("La función super() devuelve:")
        print(super())
        print("Que tiene las variables:")
        print(vars(super()))
        self.dec_order = 6
        self.f = None


if __name__ == "__main__":
    f = F()
    print(dir(f))
    print(F.e)

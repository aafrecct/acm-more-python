"""
Python tiene la capacidad de 'preguntar' a una clase o una 
instancia qué metodos y atributos tiene. Para esto hay dos metodos:
    dir()
    vars()
"""

class ExampleClass():
    def __init__(self):
        self.atributo_a = "atributo_a"
    
    def metodo_1(self):
        print("Metodo 1")

if __name__ == "__main__":
    example = ExampleClass()
    input("Estos son los atributos de 'example':")
    print(vars(example), "\n")
    input("Estos son todos los metodos y atrubutos de 'example':")
    print(dir(example), "\n")
    input("Estos son los metodos y atrubutos publicos de 'example':")
    print([member for member in dir(example) if member[:2] != "__"], "\n")
    input("Llamada a dir() sin argumentos:")
    print(dir())

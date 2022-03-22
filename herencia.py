
#Ejemnplo de herencia de una super clase(Rectangulo)
#A una subclase(Cuadrado)
class Rectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


class Cuadrado(Rectangulo):
    def __init__(self,lado):
        super().__init__(lado,lado)

if __name__ == '__main__':
    rectangulo = Rectangulo(10,15)
    print(rectangulo.area())
    print("\n")
    cuadrado = Cuadrado(5)
    print(cuadrado.area())


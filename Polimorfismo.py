class Persona:
    def __init__(self,nombre):
        self.nombre = nombre

    def avanza(self):
        print("Estoy avanzando a pie")


class Ciclista(Persona):
    def __init__(self,nombre):
        super().__init__(nombre)

    def avanza(self):
        print("Estoy avanzando en bicicleta")

def main():
    persona = Persona("Santiago")
    persona.avanza()
    ciclista = Ciclista("Montse")
    ciclista.avanza()


if __name__ == "__main__":
    main()
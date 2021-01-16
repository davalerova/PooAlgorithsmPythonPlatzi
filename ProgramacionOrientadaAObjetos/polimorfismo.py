class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print("Ando caminando")
    

class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)
    
    def avanza(self):
        print("Ando moviéndome en mi bicicleta")

def main():
    ciclista = Ciclista("Daniela")
    ciclista.avanza()
    persona = Persona("David")
    persona.avanza()

if __name__ == '__main__':

    main()
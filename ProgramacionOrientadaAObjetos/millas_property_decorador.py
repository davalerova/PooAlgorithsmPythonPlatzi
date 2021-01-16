class Millas:
    def __init__(self) -> None:
        self._distancia = 0

    #Función para obtener el valor de _distancia
    #Usando el decorador property

    @property
    def obtener_distancia(self):
        print("Llamada al método get")
        return self._distancia
    
    #Función para definir el valor de distancia

    @obtener_distancia.setter
    def definir_distancia(self, valor):
        if valor < 0:
            raise ValueError("No es posible convertir distancias menores a 0.")
        print("Llamada al método setter")
        self._distancia = valor

avion = Millas()

avion.distancia = 200

print(avion.distancia)
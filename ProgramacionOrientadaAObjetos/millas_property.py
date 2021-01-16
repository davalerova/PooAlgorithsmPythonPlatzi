
class Millas_property:
    def __init__(self):
        self._distancia = 0

    #Función para obtener el valor de la distancia:
    def obtener_distancia(self):
        print("Llamada al método get:")
        return self._distancia
    
    #Función para definir el valor de distancia
    def definir_distancia(self, valor):
        print("Llamada al método set:")
        self._distancia = valor
    
    #Función para eliminar el atributo distancia:
    def eliminar_distancia(self):
        del self._distancia
    
    distancia = property(obtener_distancia, definir_distancia, eliminar_distancia)

#Creamos un nuevo objeto
avion3 = Millas_property

#Indicamos la distancia
avion3.distancia = 200

#Obtenemos su atributo distancia
print(avion3.distancia)
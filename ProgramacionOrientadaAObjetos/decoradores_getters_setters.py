def funcion_decoradora(funcion):
    def wrapper():
        print("Este es el último mensaje...")
        funcion()
        print("Este es el primer mensaje...")
    return wrapper

def zumbido():
    print("Buzzzzzzzzz")

zumbido = funcion_decoradora(zumbido)
zumbido()



print("Mejorando la sintaxis")

@funcion_decoradora
def zumbido():
    print("Buzzzzz")

zumbido()

print("\nGetters y Setters\n")
print("    Clases sin Getters y Setters\n")

class Millas:
    def __init__(self, distancia = 0) -> None:
        self.distancia = distancia

    def convertir_a_kilometros(self):
        return self.distancia * 1.609344

#se crea un nuevo objeto
avion = Millas()

#indicamos la distancia
avion.distancia = 200

"Obtenemos el atributo distancia"
print(avion.distancia)

"Obtenemos el método convertir_a_kilometros"
print(avion.convertir_a_kilometros())


print("\nUtilizando Getters y Setters:")

class Millas_getters_setters:
    def __init__(self, distancia = 0) -> None:
        self._distancia = distancia
    
    def convertir_a_kilometros(self):
        return self._distancia * 1.609344
    
    #Método getter
    def obtener_distancia(self):
        return self._distancia
    
    #Método setter
    def definir_distancia(self, valor):
        if valor < 0:
            raise ValueError("No es posible convertir distancias menores a o.")
        self._distancia = valor

#se crea un nuevo objeto
avion2 = Millas_getters_setters()

#indicamos la distancia
avion2.definir_distancia(200)

"Obtenemos el atributo distancia"
print(avion2.obtener_distancia())

"Obtenemos el método convertir_a_kilometros"
print(avion2.convertir_a_kilometros())

print("\nFunción property:\n")

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
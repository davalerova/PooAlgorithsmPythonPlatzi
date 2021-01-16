def elevar_cubo(numero):
    return numero ** 3

print(elevar_cubo(3))

def presentarse(nombre):
    return f"Me llamo {nombre}"

def estudiemos_juntos(nombre):
    return f"¡Hey {nombre}, aprendamos Python!"

def consume_funciones(funcion_entrante):
    return funcion_entrante("David")

print(consume_funciones(presentarse))
print(consume_funciones(estudiemos_juntos))

def funcion_mayor():
    print("Esta es una función mayor y su mensaje de salida")

    def librerias():
        print("Algunas librerías de Python son: Scikit-learn, Numpy y TensorFlow.")
    
    def frameworks():
        print("Algunos frameworks de Python son: Django, Dash, Flask.")

    frameworks()
    librerias()

funcion_mayor()
import random
def busqueda_binaria(lista, inicio, final, objetivo):
    match = False
    print(f'Buscando {objetivo} entre {lista[inicio]} y {lista[final - 1]}')
    if inicio > final:
        return False

    medio = (inicio + final) // 2
    if lista[medio] == objetivo:
        return True
    
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        return busqueda_binaria(lista, inicio, medio - 1, objetivo)

    return match

if __name__ == '__main__':
    tamano_lista = int(input('De qué tamaño es la lista'))
    objetivo = int(input('Qué número quieres encontrar'))

    lista = sorted([random.randint(0,100) for i in range(tamano_lista)])
    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"está" if encontrado else "no está"} en la lista')
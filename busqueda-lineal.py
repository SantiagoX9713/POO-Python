import random

def busqueda_lineal(lista, objetivo):
    match = False
    for i in lista:
       if i == objetivo:
           match = True
           break
    return match
# O(n)


if __name__ == '__main__':
    tamano_de_lista = int(input('¿De que tamaño será la lista?'))
    objetivo = int(input('¿Que número quieres encontrar?'))
    lista = [random.randint(0,100) for i in range(tamano_de_lista)]
    print(lista)
    encontrado = busqueda_lineal(lista,objetivo)
    print(f'El elemento {objetivo} {"está" if encontrado else "no está"} en la lista')
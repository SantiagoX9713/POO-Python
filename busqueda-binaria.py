import random

def busqueda_binaria(lista, start, end, objetivo):
    print(f'Buscando {objetivo} entre {lista[start]} y {lista[end - 1]}.')
    if start  > end:
        return False
    
    middle = (start + end) // 2

    if lista[middle] == objetivo:
        return True
    elif lista[middle] < objetivo:
        return busqueda_binaria(lista, middle + 1, end, objetivo)
    else:
        return busqueda_binaria(lista, start, middle - 1, objetivo)
# O(log n)
    
if __name__ == '__main__':
    tamano_de_lista = int(input('¿De que tamaño será la lista?'))
    objetivo = int(input('¿Que número quieres encontrar?'))
    lista = sorted([random.randint(0,100) for i in range(tamano_de_lista)])
    # print(lista)
    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
    print(f'El elemento {objetivo} {"está" if encontrado else "no está"} en la lista')
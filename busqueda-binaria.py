import random

def busqueda_binaria(lista, start, end, objetivo,iter_bin=0):
    iter_bin += 1
    print(f'Buscando {objetivo} entre {lista[start]} y {lista[end - 1]}.')
    if start  > end:
        return (False,iter_bin)
    
    middle = (start + end) // 2

    if lista[middle] == objetivo:
        return (True,iter_bin)
    elif lista[middle] < objetivo:
        return busqueda_binaria(lista, middle + 1, end, objetivo,iter_bin=iter_bin)
    else:
        return busqueda_binaria(lista, start, middle - 1, objetivo,iter_bin=iter_bin)
# O(log n)
    
if __name__ == '__main__':
    tamano_de_lista = int(input('¿De que tamaño será la lista?'))
    objetivo = int(input('¿Que número quieres encontrar?'))
    lista = sorted([random.randint(0,100) for i in range(tamano_de_lista)])
    # print(lista)
    (encontrado,iter_bin) = busqueda_binaria(lista, 0, len(lista), objetivo)
    print(f'El elemento {objetivo} {"está" if encontrado else "no está"} en la lista')
    print(f'Pasos para encontralo: {iter_bin}')
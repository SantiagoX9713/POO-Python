import random

def bubble_sort(lista):
    l = len(lista)
    for i in range(l):
        for j in range(0,l - i -1):
            if lista[j] > lista[j + 1]:
                lista[j],lista[j + 1] = lista[j + 1], lista[j]
    return lista
# O(n) * O(n) = O(n * n) = O(n**n)


if __name__ == '__main__':
    tamano_de_lista = int(input('¿De que tamaño será la lista?'))
    lista = [random.randint(0,100) for i in range(tamano_de_lista)]
    print(lista)
    sorted_list = bubble_sort(lista)
    print(sorted_list)
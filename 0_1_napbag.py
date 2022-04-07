def napbag(size, weigth, values, n):
    if n == 0 or size == 0:
        return 0

    if weigth[n - 1] > size:
        return napbag(size, weigth, values,n - 1)

    return max(values[n - 1] + napbag(size - weigth [n -1], weigth, values, n - 1),
                napbag(size, weigth, values, n - 1))

if __name__ == '__main__':
    values = [60, 100, 120]
    weigth = [10, 20, 30]
    size = 50
    n = len(values)
    resultado = napbag(size, weigth, values, n)
    print(resultado)
def operaciones_lista(numeros):
    """
    (num[]) -> num[]

    reciba como parámetro una lista de números y retorne una lista
    con la suma, resta, multiplicación y división de todos.

    >>> operaciones_lista([1,1,1,1,1])
    [5, -5, 1, 1]

    >>> operaciones_lista([1,1,1,1,1,1,1,1,1])
    [9, -9, 1, 1]

    :param numeros: Lista con 5 numeros
    :return: lista con suma resta...
    """

    suma = 0
    resta = 0
    producto = 1
    division = 1
    for elemento in numeros:
        suma += elemento
        resta -= elemento
        producto *= elemento
        division /= elemento

    return [suma, resta, producto, round(division)]

print(operaciones_lista([1,2,3,4,5,7,9,6,8,2,5]))

def media(lista):
    """
    (list of num) -> num

    Calcula la media de los elementos de la lista

    >>> media([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
    1.0

    >>> media([1,2,3])
    2.0

    >>> media([3,4,7,6])
    5.0

    :param lista: la lista de elementos a evaluar
    :return: la media de los elementos
    """
    resultado = 0
    for numero in lista:
        resultado += numero
    return resultado / len(lista)

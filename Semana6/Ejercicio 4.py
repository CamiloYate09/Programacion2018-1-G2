def producto_escalar_2(lista):
    """
    (list of num) -> List of num

    >>> producto_escalar_2([1,2,3,4,5])
    [2, 4, 6, 8, 10]

    >>> producto_escalar_2([5,4,3,2,1])
    [10, 8, 6, 4, 2]

    Precondition: len(lista) == 5

    :param lista: la lista a evaluar
    :return: una lista con todos los numeros * 2
    """
    return [lista[0] * 2, lista[1] * 2, lista[2] * 2, lista[3] * 2, lista[4] * 2]
    # return lista *2 Ojo esto no funciona

def unir_listas(lista_1, lista_2):
    """
    (List of num, list of num) -> list of num

    Une las dos listas

    >>> unir_listas([0,1,2,3,4],[5,6,7,8,9])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    >>> unir_listas([5,6,7,8,9], [0,1,2,3,4])
    [5, 6, 7, 8, 9, 0, 1, 2, 3, 4]

    :param lista_1: La primera lista
    :param lista_2: La segunda lista
    :return: Una lista con todos los elementos
    """
    return lista_1 + lista_2

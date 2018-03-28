def los_primeros_5(lista):
    """
    (list) -> (list)

    Recibe como parámetro una lista con 10 elementos, y retorne una lista nueva con solo
    los primeros 5 números de la lista original.

    >>> los_primeros_5([1,2,3,4,5,6,7,8,9,10])
    [1, 2, 3, 4, 5]

    :param lista: la lista de 10 elementos
    :return: lista con los primeros 5 elementos
    """
    lista_resultante = []
    for i in range(0, 5):
        lista_resultante.append(lista[i])
    return lista_resultante

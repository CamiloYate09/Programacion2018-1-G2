def multiplicar_por_2(lista):
    """
    (list of num) -> list of num

    >>> multiplicar_por_2([1,1,1,1,1])
    [2, 2, 2, 2, 2]

    >>> multiplicar_por_2([])
    []

    >>> multiplicar_por_2([9,7,0,-3])
    [18, 14, 0, -6]

    Retorna una lista con los elementos de la orginal
    multiplicados por 2

    :param lista: la lista a evaluar
    :return: lista con los elementos multiplicados por 2
    """
    resultante = []
    for numero in lista:
        resultante.append(numero*2)
    return resultante

def reemplazar_numeros(numeros):
    """
    (list of num) -> (list)
    Recibe como parámetro una lista de números, reemplaza los múltiplos de 3 por una “x”.

    >>> reemplazar_numeros([1,2,3,4,5,6])
    [1, 2, 'x', 4, 5, 'x']

    >>> reemplazar_numeros([3,6,9,12,15])
    ['x', 'x', 'x', 'x', 'x']

    :param numeros: lista con los numeros a evaluar
    :return: la lista modificada
    """
    lista_resultante = []
    for numero in numeros:
        if numero % 3 == 0:
            lista_resultante.append('x')
        else:
            lista_resultante.append(numero)
    return lista_resultante

def operaciones_lista(numeros):
    """
    (num[]) -> num[]

    reciba como parámetro una lista de 5 números y retorne una lista
    con la suma, resta, multiplicación y división de todos.

    >>> operaciones_lista([1,1,1,1,1])
    [5, -3, 1, 1]

    :param numeros: Lista con 5 numeros
    :return: lista con suma resta...
    """
    resultados = []
    resultados.append(numeros[0] + numeros[1]
                      + numeros[2] + numeros[3]
                      + numeros[4])
    resultados.append(numeros[0] - numeros[1]
                      - numeros[2] - numeros[3]
                      - numeros[4])
    resultados.append(numeros[0] * numeros[1]
                      * numeros[2] * numeros[3]
                      * numeros[4])
    resultados.append(numeros[0] // numeros[1]
                      // numeros[2] // numeros[3]
                      // numeros[4])
    return resultados

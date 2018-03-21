"""
En este documento incluiremos los ejercicios de operaciones basicas de vectores

"""
_author_ = "Jose Cordoba"


def producto_escalar(escalar, vector):
    """
    (num, list of num) -> list of num

    Calcula el producto escalar

    >>> producto_escalar(7,[1,2,3])
    [7, 14, 21]

    >>> producto_escalar(5,[3,8,3])
    [15, 40, 15]

    :param escalar: el escalar a multiplicar
    :param vector: el vector a evaluar
    :return: el vector resultante
    """
    vector_resultante = []
    for numero in vector:
        vector_resultante.append(numero * escalar)
    return vector_resultante


def suma_vectores(v_1, v_2):
    """
    (list of num, list of num) -> list of num

    Suma los dos vectores

    >>> suma_vectores([1,2,3],[3,2,1])
    [4, 4, 4]

    >>> suma_vectores([2,3],[2,1])
    [4, 4]

    >>> suma_vectores([],[1])
    Traceback (most recent call last):
      ...
    ValueError: Los vectores tienen diferente dimension

    :param v_1: el primer vector
    :param v_2: el segundo vector
    :return: el vector resultante de la suma de v_1 + v_2
    """
    if len(v_1) == len(v_2):
        vector_resultante = []
        for i in range(0, len(v_1)):
            vector_resultante.append(v_1[i] + v_2[i])
        return vector_resultante
    else:
        raise ValueError("Los vectores tienen diferente dimension")

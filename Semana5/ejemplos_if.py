"""
En este archivo subiremos nuestros ejemplos de la estructura de
decisión if
"""


def es_negativo(num):
    """
    (num) -> str

    Escribe el mensaje 'El numero es negativo' cuando el numero es
    menor que cero

    >>> es_negativo(0.0)
    ''
    >>> es_negativo(-20.0)
    'El numero es negativo'
    >>> es_negativo(1.0)
    ''

    :param num: el numero a evaluar
    :return: el mensaje resultante
    """
    salida = ''
    if num < 0:
        salida = 'El numero es negativo'
    return salida


def es_positivo(num):
    """
    (num) -> str

    Escribe el mensaje 'El numero es positivo' cuando el numero es
    mayor o igual que cero

    >>> es_positivo(0)
    'El numero es positivo'
    >>> es_positivo(-20)
    ''
    >>> es_positivo(10)
    'El numero es positivo'

    :param num: el numero a evaluar
    :return: el mensaje resultante
    """
    salida = ''
    if num >= 0:
        salida = 'El numero es positivo'
    return salida


def el_mayor(edad_1, edad_2):
    """
    (num,num) -> str

    retorna quien es el mayor de las dos edades

    >>> el_mayor(10,10)
    'los dos son igual de jovenes'

    >>> el_mayor(5,10)
    'El primero es el mas joven'

    >>> el_mayor(10,5)
    'El segundo es el mas joven'

    :param edad_1: la edad de la primera persona
    :param edad_2: la edad de la segunda persona
    :return: mensaje con el dato del mas joven
    """
    salida = ''
    if edad_1 > edad_2:
        salida = 'El segundo es el mas joven'
    elif edad_1 < edad_2:
        salida = 'El primero es el mas joven'
    else:
        salida = 'los dos son igual de jovenes'
    return salida

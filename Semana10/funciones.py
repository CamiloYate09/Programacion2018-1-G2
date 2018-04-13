# Podemos reutilizar nuestras funciones
def sumatoria(desde, hasta, funcion):
    """
    (int, int, function) -> float

    Calcula la sumatoria de todos los numeros
    en el rango dado

    >>> sumatoria(1, 3, lambda x : x)
    6

    >>> sumatoria(0, 100, lambda x : x)
    5050

    :param desde: desde donde hago la sumatoria
    :param hasta: hasta donde hago la sumatoria
    :return: el resultado de la sumatoria
    """
    resultado = 0
    for i in range(desde, hasta + 1):
        resultado += funcion(i)
    return resultado


def cuadrado(base):
    """
    (num) -> num

    Eleva la base al cuadrado

    >>> cuadrado(3)
    9

    >>> cuadrado(7)
    49

    :param base: la base para calcular
    :return: el cuadrado de la base
    """
    return base ** 2


# Todo hacer la función Raiz cuadrada
def raiz_cuadrada(base):
    """
    (num) -> float

    Obtiene la raiz cuadrada de un número

    >>> raiz_cuadrada(4)
    2.0

    >>> raiz_cuadrada(9)
    3.0

    >>> raiz_cuadrada(25)
    5.0

    :param base: la base de la operación
    :return: el resultado de calcular la raiz cuadrada
    """
    return base ** (1 / 2)

import Semana10.funciones as fun


def sumatoria_cuadrados(desde, hasta):
    """
    (int, int) -> int
    Calcula la sumataoria de los numeros al cuadrado en el
    rango seleccionado

    >>> sumatoria_cuadrados(1, 3)
    14

    >>> sumatoria_cuadrados(3, 4)
    25

    :param desde: el rango inicial de nuestra función
    :param hasta: el rango final de nuesta funcion
    :return: la sumatoria de todos los numeros en el rango elevados
    al cuadrado
    """
    return fun.sumatoria(desde, hasta, fun.cuadrado)


def sumatoria_raices(desde, hasta):
    """
    (int, int) -> float

    Calcula la sumatoria de las raices cuadradas en un rango determinado

    >>> sumatoria_raices(1, 4)
    6.146264369941973
    >>> sumatoria_raices(2, 10)
    21.468278186204095

    :param desde: el rango inicial
    :param hasta: el limite superior
    :return: la sumatoria de las raices cuadradas en el rango
    """
    return fun.sumatoria(desde, hasta, fun.raiz_cuadrada)

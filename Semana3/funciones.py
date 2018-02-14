import math

def area_circulo(radio):
    """
    (num) -> float

    Calcula el area de un circulo dado su radio

    >>> area_circulo(1)
    3.141592653589793
    >>> area_circulo(2)
    12.566370614359172

    :param radio: el radio del circulo
    :return: el area del circulo
    """
    return math.pi * radio *radio

def kelvin_a_centigrados(kelvin):
    """
    (num) -> num

    Convierte una cantidad en grados kelvin a grados centigrados

    >>> kelvin_a_centigrados(273)
    0
    >>> kelvin_a_centigrados(500)
    227

    :param kelvin: la cantidad en grados kelvin
    :return: La cantidad en grados centigrados
    """
    return kelvin - 273


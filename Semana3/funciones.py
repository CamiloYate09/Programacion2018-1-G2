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

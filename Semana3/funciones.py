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

def calcular_propina(cuenta, porcentaje_propina):
    """(num,num) -> float

    Calcula la propina dado una cuenta y un porcentaje de propina

    Precondición: La propina es un valor entre 0 y 100

    >>> calcular_propina(100,10)
    10.0
    >>> calcular_propina(2000,5)
    100.0

    :param cuenta: El valor consumido en el restaurante
    :param porcentaje_propina: El porcentaje de propina (entre 0 y 100)
    :return: El valor de la propina calculado
    """
    propina = cuenta * porcentaje_propina
    propina = propina / 100
    return propina

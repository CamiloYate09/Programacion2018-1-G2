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

def perimetro_del_triangulo(lado_1, lado_2, lado_3):
    '''
    (num,num,num) ->  num

    Calcula el perimetro de un triangulo

    Precondición: los lados entre (0, infinito)

    >>> perimetro_del_triangulo(1,2,3)
    6
    >>> perimetro_del_triangulo(2,2,2)
    6
    >>> perimetro_del_triangulo(3,2,7)
    12

    :param lado_1: El primer lado del triangulo
    :param lado_2: El segundo lado del triangulo
    :param lado_3: El tercer lado del triangulo
    :return: El perimetro del triangulo
    '''
    return lado_1 + lado_2 + lado_3

def semiperimetro_del_triangulo(lado_1, lado_2, lado_3):
    '''
    (num,num,num) ->  num

    Calcula el semiperimetro de un triangulo

    Precondición: los lados entre (0, infinito)

    >>> semiperimetro_del_triangulo(1,2,3)
    3.0
    >>> semiperimetro_del_triangulo(2,2,2)
    3.0
    >>> semiperimetro_del_triangulo(3,2,7)
    6.0

    :param lado_1: El primer lado del triangulo
    :param lado_2: El segundo lado del triangulo
    :param lado_3: El tercer lado del triangulo
    :return: El perimetro del triangulo
    '''
    return perimetro_del_triangulo(lado_1,lado_2,lado_3)/2

def area_triangulo(lado_1,lado_2,lado_3):
    '''
    (num,num,num) -> num

    Calcula el area de un triangulo dado sus lados

    >>> area_triangulo(3,25,26)
    36.0

    :param lado_1: El primer lado del triangulo
    :param lado_2: El segundo lado del triangulo
    :param lado_3: El tercer lado del triangulo
    :return: El perimetro del triangulo
    '''
    semiperimetro = semiperimetro_del_triangulo(lado_1,lado_2,lado_3)
    s_a = semiperimetro - lado_1
    s_b = semiperimetro - lado_2
    s_c = semiperimetro - lado_3
    return math.sqrt(semiperimetro*s_a*s_b*s_c)

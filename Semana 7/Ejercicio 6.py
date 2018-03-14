def es_vocal(letra):
    """
    (str) -> Boolean

    Decide si una letra es vocal

    Precondition: len(letra) == 1

    >>> es_vocal('a')
    True

    >>> es_vocal('b')
    False

    :param letra: la letra a evaluar
    :return: True si es vocal, False de lo contrario
    """
    return letra in "aeiouAEIOU"


def num_vocales(cadena):
    """
    (str) -> int

    Cuenta el numero de vocales en la cadena

    Precondition: len(cadena) == 10

    >>> num_vocales("Hola Mundo")
    4
    >>> num_vocales('JoseCordob')
    4

    :param cadena: la cadena a evaluar
    :return: el numero de vocales en la cadena
    """
    cuenta = 0
    for letra in cadena:
        if es_vocal(letra):
            cuenta += 1
    #
    #
    # if es_vocal(cadena[0]):
    #     cuenta +=1
    # if es_vocal(cadena[1]):
    #     cuenta +=1
    # if es_vocal(cadena[2]):
    #     cuenta +=1
    # if es_vocal(cadena[3]):
    #     cuenta +=1
    # if es_vocal(cadena[4]):
    #     cuenta +=1
    # if es_vocal(cadena[5]):
    #     cuenta +=1
    # if es_vocal(cadena[6]):
    #     cuenta +=1
    # if es_vocal(cadena[7]):
    #     cuenta +=1
    # if es_vocal(cadena[8]):
    #     cuenta +=1
    # if es_vocal(cadena[9]):
    #     cuenta +=1
    return cuenta

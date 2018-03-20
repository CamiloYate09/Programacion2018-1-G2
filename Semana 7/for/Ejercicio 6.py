def es_vocal(letra):
    """
    (str) -> boolean

    Decide si una letra es vocal

    Precondition len(letra) == 1

    >>> es_vocal('a')
    True

    >>> es_vocal('b')
    False

    :param letra: la letra a evaluar
    :return: True si es una vocal, False de lo contrario
    """
    return letra in "aeiouAEIOU"

def contar_vocales(cadena):
    """

    Cuenta el numero de vocales en la cadena

    >>> contar_vocales('Hola mundo')
    4

    >>> contar_vocales('Jose manuel Cordoba Castillo')
    11

    >>> contar_vocales('')
    0

    :param cadena: la cadena a evaluar
    :return: int el numero de vocales en la cadena
    """
    resultado = 0
    for letra in cadena:
        if es_vocal(letra):
            resultado +=1

    return resultado

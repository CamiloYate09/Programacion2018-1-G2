"""
Una cadena de ADN esta formada por bases de Adenina, Guanina, Citocina y
Tiamina 'A, T, C, G', adicionalmente las cadenas de ADN se organizan en
pares enlazados los cuales deben ser complementados de la siguiente
forma A <-> T y C <-> G.

El objetivo de esta aplicación es evaluar si dos cadenas de ADN son
Correspondientes y adicionalmente obtener la cadena complementaria.

Finalmente se desea evaluar el nivel de correspondecia entre una cadena y una
no valida.
"""


def obtener_complemento(base):
    """
    (str) -> str

    Obtiene un complemento dada una base
    Precondicion: La base es valida

    >>> obtener_complemento('A')
    'T'
    >>> obtener_complemento('T')
    'A'
    >>> obtener_complemento('Z')
    Traceback (most recent call last):
    ...
    ValueError: Z no es una base valida

    :param base: la base a evaluar
    :return: la base complementaria
    """
    if base == 'A':
        return 'T'
    elif base == 'T':
        return 'A'
    elif base == 'G':
        return 'C'
    elif base == 'C':
        return 'G'
    else:
        raise ValueError(base + ' no es una base valida')


def generar_cadena_complementaria(ADN):
    """
    (str) -> str
    Genera la cadena de ADN complementaria
    Precondicion ADN es una cadena valida

    >>> generar_cadena_complementaria('ATA')
    'TAT'
    >>> generar_cadena_complementaria('ATGC')
    'TACG'
    >>> generar_cadena_complementaria('ATGD')
    Traceback (most recent call last):
    ...
    ValueError: ATGD no es una cadena de ADN valida

    :param ADN: La cadena de ADN a validar
    :return: La cadena complementaria
    """
    complemento = ''
    for base in ADN:
        if es_base(base):
            complemento += obtener_complemento(base)
        else:
            raise ValueError(ADN + ' no es una cadena de ADN valida')
    return complemento


def se_complementan_bases(base, complemento):
    """
    (str, str) -> boolean
    Verifica si una base y un complemento son correspondientes

    >>> se_complementan_bases('A', 'T')
    True
    >>> se_complementan_bases('A', "G")
    False

    :param base: la base a verificar
    :param complemento: el complemento a verificar
    :return: True si son correspondientes
    """
    return complemento == obtener_complemento(base)

# TODO la funcion para calcular el porcentaje de correspondencia de una cadena y otra

def es_cadena_complementaria(ADN_1, ADN_2):
    """
    (str, str) -> Boolean
    Valida si una cadena de ADN es el complemento de la otra

    >>> es_cadena_complementaria('ATGC', "TACG")
    True

    >>> es_cadena_complementaria('ATGC', "TACC")
    False

    :param ADN_1: la secuencia a validar
    :param ADN_2: la secuencia complementaria
    :return: True si es el complemento, false de lo contrario
    """
    return ADN_2 == generar_cadena_complementaria(ADN_1)


def es_cadena_valida(ADN):
    """
    (str) -> boolean
    Valida si toda la secuencia de ADN es valida

    >>> es_cadena_valida('ATCG')
    True
    >>> es_cadena_valida("AZDFG")
    False

    :param ADN: La cadena de ADN a evaluar
    :return: True si la cadena de ADN es valida, False de lo contrario
    """
    for base in ADN:
        if not es_base(base):
            return False
    return True


def es_base(base):
    """
    (str) -> bool

    Decide si una cadena es una base

    >>> es_base('A')
    True
    >>> es_base('T')
    True
    >>> es_base('Z')
    False
    >>> es_base('AT')
    False

    :param base: la cadena a evaluar
    :return: True si es una base, False de lo contrario
    """
    return len(base) == 1 and base in 'ATCG'

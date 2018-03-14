def a_ascii(cadena):
    """
    (str) -> list of int

    Transforma una cadena de 10 elementos en una
    lista de sus codigos ascii

    >>> a_ascii("Hola mundo")
    [72, 111, 108, 97, 32, 109, 117, 110, 100, 111]

    :param cadena: La cadena a convertir
    :return: lista con los caracteres en ascii
    """
    lista_ascii = []
    lista_ascii.append(ord(cadena[0]))
    lista_ascii.append(ord(cadena[1]))
    lista_ascii.append(ord(cadena[2]))
    lista_ascii.append(ord(cadena[3]))
    lista_ascii.append(ord(cadena[4]))
    lista_ascii.append(ord(cadena[5]))
    lista_ascii.append(ord(cadena[6]))
    lista_ascii.append(ord(cadena[7]))
    lista_ascii.append(ord(cadena[8]))
    lista_ascii.append(ord(cadena[9]))
    # for letra in cadena:
    #     lista_ascii.append(ord(letra))
    return lista_ascii

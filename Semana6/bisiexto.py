def es_bisiexto(ano):
    """
    (int) -> boolean

    Decide si un año es bisiexto

    >>> es_bisiexto(4)
    True
    >>> es_bisiexto(100)
    False
    >>> es_bisiexto(400)
    True

    :param ano: el año a evaluar
    :return: True si el año e bisiexto False de lo contrario
    """
    p = ano % 4 == 0
    q = ano % 100 == 0
    r = ano % 400 == 0
    return p and (not q or r)


ano_usuario = int(input("Ingrese su año\n"))

if 0:
    print("Su año es bisiexto\n")
else:
    print("Su año no es bisiexto\n")

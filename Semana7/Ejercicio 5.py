def media(lista):
    """
    (list of num) -> float

    Retorna la media de los numeros en la lista

    Precondition: len(lista) == 5

    >>> media([1,2,3,4,5])
    3.0

    >>> media([2,2,2,2,2])
    2.0

    :param lista: con numeros a evaluar
    :return: la media de los numeros en la lista
    """
    return (lista[0] + lista[1] + lista[2] + lista[3] + lista[4]) / 5

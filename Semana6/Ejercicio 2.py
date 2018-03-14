def ordenar_lista(num_1, num_2, num_3, num_4, num_5):
    """
    (num,num,num,num,num) -> num[]

    Organiza los numeros de forma ascendente en una lista

    >>> ordenar_lista(5, 4, 3, 2, 1)
    [1, 2, 3, 4, 5]

    >>> ordenar_lista(50, -4, 30, 12, 15)
    [-4, 12, 15, 30, 50]

    :param num_1: el primer numero
    :param num_2: el Segundo numero
    :param num_3: el tercer numero
    :param num_4: el cuarto numero
    :param num_5: el quinto numero
    :return: una lista con los numeros de manera ascendente
    """
    return sorted([num_1, num_2, num_3, num_4, num_5])

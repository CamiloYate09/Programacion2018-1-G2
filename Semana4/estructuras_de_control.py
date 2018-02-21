def es_par(numero):
    '''
    (int) -> boolean

    Valida si un numero es par

    >>> es_par(2)
    true
    >>> es_par(9)
    false

    :param numero: el numero a verificar
    :return: true si el numero es par false de lo contrario
    '''
    return numero%2==0

numero = int(input("Digite su numero:\n"))

#if nos permite tomar una decision
if(es_par(numero)):
    print("El número "+ str(numero) + " es par")
#else nos permite evaluar el caso contrario
else:
    print("El número "+ str(numero) + " no es par")

def saludar_hora(hora):
    '''
    (num) -> str

    Saluda de acuerdo a la hora dada
    Precondicion: hora 0 - 23


    >>> saludar_hora(10)
    "Buenos días"

    >>> saludar_hora(16)
    "Buenas tardes"

    >>> saludar_hora(21)
    "Buenas noches"

    :param hora: la hora actual
    :return: un saludo
    '''
    if hora<13:
        return "Buenos Días"
    elif hora < 17:
        return "Buenas tardes"
    else:
        return "Buenas Noches"

print(saludar_hora(int(input("Que hora es?\n"))))

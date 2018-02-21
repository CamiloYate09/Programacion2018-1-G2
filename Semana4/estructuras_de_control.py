def esPar(numero):
    '''
    (int) -> boolean

    Valida si un numero es par

    >>> esPar(2)
    true
    >>> esPar(9)
    false

    :param numero: el numero a verificar
    :return: true si el numero es par false de lo contrario
    '''
    return numero%2==0

def saludarHora(hora):
    '''

    :param hora:
    :return:
    '''


numero = int(input("Digite su numero:\n"))

print(numero)


#if nos permite tomar una decision
if(esPar(numero)):
    print("El número "+ str(numero) + " es par")
#else nos permite evaluar el caso contrario
else:
    print("El número "+ str(numero) + " no es par")



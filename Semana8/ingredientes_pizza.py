def ingredientes_pizza():
    """
    -> list of str

    Solicita al usuario los ingredientes de una pizza y retorna una lista
    con ellos

    :return: lista con los ingredientes de la pizza
    """
    pizza = []
    while True:
        ingrediente = input("Ingrese un ingrediente o 'salir' para terminar\n")
        if ingrediente.lower() == 'salir':
            break
        else:
            pizza.append(ingrediente.lower())
    return pizza


# Probamos nuestra función
print('Su pizza tendrá', ingredientes_pizza())

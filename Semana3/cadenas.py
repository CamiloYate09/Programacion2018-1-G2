def saludar():
    """
    (none) -> str
    Saluda al usuario luego de preguntar el nombre

    :return: el nombre ingresado por el usuario
    """
    return input("¿Cual es tu nombre?\n")


#Tres formas de definir str
# comillas simples fugan automaticamente las comillas dobles
cadena_1 = 'Hola "comillas dobles" '
#comillas dobles fugan automaticamente las comillas simples
cadena_2 = "Hola 'comillas simples' "
#comillas triples fugan automaticamente los saltos de linea
cadena_3 = '''Hola
mundo'''#las comillas triples permiten escribir multiples lineas

#note la diferencia en lo que se imprime
print(cadena_1, cadena_2, cadena_3)

#Podemos concatenar cadenas usando el operador +
cadena_concatenada = cadena_1 + cadena_2
print("La cadena concatenada es:",cadena_concatenada)

#Podemos multiplicar nuestras cadenas utilizando el operador *
cadena_multiplicada = cadena_1 * 3
print("la cadena multiplicada es:",cadena_multiplicada)

#Podemos averiguar la longitud de una cadena utlizando la función
#len(str)
longitud = len(cadena_multiplicada)
print("La longitud de la cadena es",longitud)

#Podemos fugar usando \
cadena_de_fugas = "\n\t\"\'\\"
print("La cadena de fugas es:",cadena_de_fugas)

#Podemos preguntar si algo esta en la cadena
esta_h = "h" in cadena_1
print("Esta \"h\" en cadena_1:",esta_h)

esta_Ho = "Ho" in cadena_1
print("Esta \"Ho\" en cadena_1:",esta_Ho)

def saludar_2():
    '''
    (none) -> str

    Solicita el nombre, luego el apellido y retorna una cadena con
    los dos separados por un espacio

    :return: el nombre completo
    '''
    nombre = input("¿Cual es su Nombre?\n")
    apellido = input("¿Cual es su Apellido\n")
    return nombre + " " + apellido

#probamos nuestra función saludar
print("Hola" , saludar())

#probamos nuestra función saludar 2
print("Hola" , saludar_2())

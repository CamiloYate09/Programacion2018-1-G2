# Asi declaramos un diccionario
dias_en_ingles = {'Lunes': 'Monday',
                  'Martes': 'Tuesday',
                  'Miercoles': 'Wednesday',
                  'Jueves': 'Thursday',
                  'Viernes': 'Friday',
                  'Sabado': 'Saturday',
                  'Domingo': 'Sunday'}

# Podemos acceder a un elemento del diccionario por su clave
primer_dia = dias_en_ingles['Lunes']

# Podemos iterar por las claves de un diccionario igual que
# con una lista
for clave in dias_en_ingles:
    print(clave, 'en ingles es', dias_en_ingles[clave])

# Las operaciones que hacemos en una lista, tambien aplican para los
# Diccionarios
print(len(dias_en_ingles))

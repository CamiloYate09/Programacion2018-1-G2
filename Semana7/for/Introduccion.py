"""
En este archivo trabajaremos nuestra introcucción a
estructuras de repetición

"""
cigarrillos = ['belmont', 'lucky', 'malboro', 'mustang', 'piel roja',
               'jet', 'apanado']

# print('me fumo un',cigarrillos[0])
# print('me fumo un',cigarrillos[1])
# print('me fumo un',cigarrillos[2])
# print('me fumo un',cigarrillos[3])
# print('me fumo un',cigarrillos[4])
# print('me fumo un',cigarrillos[5])
# print('me fumo un',cigarrillos[6])
# print('me fumo un',cigarrillos[7])

# Mejor recorrer las listas con una estructura de repeticion
for cigarrillo in cigarrillos:
    print("me fumo un",cigarrillo)


# Podemos usar For en cualquier estructura iterable
for c in "me gustan las paletas":
    print(c)

# Podemos iterar usando for en un rango de numeros
for numero in range(1,10):
    print(numero)

# Podemos decrementar usando for en un rango de numeros
for numero in range(10,0,-1):
    print(numero)

# Podemos aumentar de 2 en dos
for numero in range(2,21,2):
    print(numero)

# Podemos decrementar tambien de 2 en dos
for numero in range(29,14,-2):
    print(numero)

# Podemos recorrer una lista por sus indices
for i in range(0, len(cigarrillos)):
    print(cigarrillos[i])

# Podemos recorrer una lista por sus indices
# También del ultimo al primero
for i in range(-1, -1*len(cigarrillos)-1, -1):
    print(cigarrillos[i])

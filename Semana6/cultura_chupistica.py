# Podemos declarar listas utilizando [] y separando los elementos por ,
tequilas = ['Jose Cuervo', 'Olmeca', 'Herradura', 'Agave azul', 'Gusano rojo']

# Podemos imprimir nuestras listas
print(tequilas)

# Podemos obtener los elementos en nuestras listas dado su indice
# Mi cuarto tequila favorito es
print(tequilas[3])

# Podemos obtener la longitud de una lista utilizando la funcion len
print('mis tequilas favoritos son', len(tequilas))

# Podemos leer la lista de derecha a izquierda
print('El tequila que menos me gusta es', tequilas[-1])

# El jose cuervo realmente no me gusta, mejor el cabrito
tequilas[0] = 'Cabrito'

print(tequilas)

# Podemos crecer nuestra lista usando append
tequilas.append('Maestro tequilero')

# Agregamos como el ultimo elemento de la lista
print(tequilas)

# Mi tequila favorito es el 1800 añadamoslo
tequilas.insert(3, '1800')

print(tequilas)

# Podemos sacar el ultimo elemento de la lista
ultimo_tequila = tequilas.pop()

print(tequilas, ' ', ultimo_tequila)

# Podemos sacar un elemento dado su indice
tercer_tequila = tequilas.pop(2)

print(tequilas, ' ', tercer_tequila)

# Podemos remover un elemento conocido
tequilas.remove('Olmeca')

print(tequilas)

# Podemos organizar una lista
# tequilas.sort()
# Pero es mejor no dañarla
tequilas_ordenados = sorted(tequilas)

print(tequilas_ordenados)
print(tequilas)

# Podemos revertir una lista
tequilas_ordenados.reverse()

print(tequilas_ordenados)

from Semana11.OOP import Gato as Cat
from Semana11.OOP import Guarderia as Housing

# Podemos definir objetos del tipo Gato llamando a
# la funcion constructura y pasando los atributos
# A esto se le llama instanciar un objeto
fidel = Cat.Gato('Fidel', 'blanco', 10)
chavez = Cat.Gato('Hugo', 'negro', 5)

print(fidel)  # intentamos imprimir nuestro objeto

# Podemos acceder a los metodos de nuestra instancia
# con notacion de punto
print(fidel.ronnorear())

# Podemos crear nuevas instancias del objeto
raul = Cat.Gato('Raul Reyes', 'mono', 0)
print(raul)

# Podemos acceder a los atributos de un objeto usando
# Notación de punto
print('La edad de', chavez.nombre + ' es ', chavez.edad)

# Podemos almacenar objetos en objetos
casa_isabel = Housing.Guarderia('Casa de mi abuela',
                                'Oscar Cordoba')
casa_isabel.mascotas.append(fidel)
casa_isabel.mascotas.append(chavez)
casa_isabel.mascotas.append(raul)

print(casa_isabel)

# Podemos imprimir nuestras mascotas
print('Las mascotas de', casa_isabel.nombre, 'son:')
for gato in casa_isabel.mascotas:
    print(gato)

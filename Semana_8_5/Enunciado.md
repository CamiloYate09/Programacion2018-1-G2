# El Robot Parlachin

Desde tiempos inmmemoriables hemos soñado con máquinas,
que nos ayuden a responder nuestras preguntas. Esta es
su oportunidad de construir una. Diseñe una aplicacion
en python que permita responder a las preguntas dadas
por el usuario, en caso de no conocer la respuesta,
su robot debe estar en capacidad de preguntar la
respuesta correcta y de esa forma aprender a solucionar
futuras inquietudes. Su programa debe continuar chateando
con el usuario hasta que este decida despedirse.

![Robot](robot.png)

* Utilice funciones para reutilizar su código y priorice la
legibilidad del mismo usando nombres de variables que tengan
sentido.
* Cargue una serie de respuestas por defecto para que su
robot funcione en el escenario inicial

Recuerde que se evaluará:
1. Estructuras de control (if, try, for, while).
2. Listas.
3. Funciones.
4. Documentacion.
5. Tipos de datos.
6. Patrón contador.
7. Patrón Acumulador.

**Sugerencia 1**
Ulitice diccionarios para apoyarse en la solución de su
problema. Asi mismo almacene los datos limpios y en minuscula
para evitar problemas.

**Sugerencia 2**
Revise los ejerccios y contenidos adicionales en el
repositorio del refuerzo de programación en https://github.com/JoseCordobaEAN/refuerzo_programacion_2018_1


## Diccionarios en Python
En python un diccionario es una estructura de datos muy similar
a una lista, su principal diferencia radica en que los indices
del diccionario son ‘claves’ en cadenas de texto. Por ejemplo:

```python
# Asi declaramos un diccionario
dias_en_ingles = { 'Lunes' : 'Monday',
                   'Martes' : 'Tuesday',
                   'Miercoles'  : 'Wednesday',
                   'Jueves'  : 'Thursday',
                   'Viernes'  : 'Friday',
                   'Sabado'  : 'Saturday',
                   'Domingo'  : 'Sunday' }

# Podemos acceder a un elemento del diccionario por su clave
primer_dia = dias_en_ingles['Lunes']

# Podemos iterar por las claves de un diccionario igual que
# con una lista
for clave in dias_en_ingles:
    print(clave, 'en ingles es',dias_en_ingles[clave])

# Las operaciones que hacemos en una lista, tambien aplican para los
# Diccionarios
print(len(dias_en_ingles))
```

Muchos exitos y en caso de dudas no olvide consultar tanto con
el docente del curso como con el monitor asignado

**Pasos a futuro** Extienda su proyecto a futuro agregando
soporte a archivos para conservar el estado de aprendizaje de
su robot.

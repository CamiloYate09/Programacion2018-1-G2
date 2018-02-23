"""
El Juego de adivinar


A todos nos gustan las adivinanzas y los ingenieros amamos
los números, desarrolle un juego en python que genere un
numero secreto (entre 0 y 100) y le de la oportunidad al
usuario de adivinar cual es durante cinco intentos.
Cuando el usuario acierte el juego debe anunciar el
nombre del usuario y su victoria, en cambio cuando el usuario
diga un número erróneo debe decirle si el numero es mas grande o
mas pequeño finalmente en el caso de presentarse un quinto intento
fallido debe anunciar la derrota del usuario.

:author Jose Cordoba
"""

# Importamos la funcion randint para generar el numero secreto
from random import randint

print("Bienvenido al juego")

jugador = input("¿Como es tu nombre?: ")

# Generamos nuestro numero al azar
secreto = randint(0, 100)

print("Estoy Pensando un numero entre 1 y 100\n "
      "Tienes 5 intentos\n"
      "¿adivina cual es?")


def turno(numero, numero_turno):
    """
    (int) -> int

    Pregunta un numero al usuario y evalua si adivino, si es menor o si es mayor

    :param numero: el número secreto del juego
    :param numero_turno: El turno en el que vamos
    :return: 1 si el usuario adivina, dos si el usuario piensa que es
    mayor y 3 si es menor
    """
    print("Es el turno " + str(numero_turno))
    guess = int(input("¿Que número crees que es?: "))
    if guess == numero:
        return 1
    elif guess < numero:
        return 2
    return 3


# primer intento
intento = turno(secreto, 1)
if intento == 1:
    print("Felicidades " + jugador + " Adivinaste!")
else:
    if intento == 2:
        print("Mi número es mas grande")
    else:
        print("Mi número es mas pequeño")
    # Segundo intento
    intento = turno(secreto, 2)
    if intento == 1:
        print("Felicidades " + jugador + " Adivinaste!")
    else:
        if intento == 2:
            print("Mi número es mas grande")
        else:
            print("Mi número es mas pequeño")
        # Tercer intento
        intento = turno(secreto, 3)
        if intento == 1:
            print("Felicidades " + jugador + " Adivinaste!")
        else:
            if intento == 2:
                print("Mi número es mas grande")
            else:
                print("Mi número es mas pequeño")
            # Cuarto intento
            intento = turno(secreto, 4)
            if intento == 1:
                print("Felicidades " + jugador + " Adivinaste!")
            else:
                if intento == 2:
                    print("Mi número es mas grande")
                else:
                    print("Mi número es mas pequeño")
                # Ultimo intento
                intento = turno(secreto, 5)
                if intento == 1:
                    print("Felicidades " + jugador + " Adivinaste!")
                else:
                    print("Lo siento " + jugador + " el número era " + str(secreto))

"""
La aplicación de apuestas

> Solución de:

Se ha identificado una oportunidad en relación a las apuestas deportivas,
desarrolle una aplicación en python la cual deberá cumplir con las
siguientes funciones:

    1. El sistema debe indicar el nombre de un encuentro deportivo
    (Ej. Caracoles Veloces Vs Plumas Pesadas).

    2. La aplicación deberá leer el resultado de cada equipo para
    los dos jugadores.

    3. La aplicación deberá generar aleatoria-mente el resultado
    real del encuentro (entre 0 y 5 puntos por equipo).

    4. La aplicación deberá determinar el puntaje de cada jugador
    basándose en el siguiente sistema de puntos:

        1. Un punto por acertar el equipo ganador.
        2. Dos puntos por acertar el puntaje del equipo local.
        3. Dos puntos por acertar el puntaje del equipo visitante.
        4. Cinco puntos por acertar el resultado total.

    5. La aplicación deberá indicar el nombre del jugador ganador
    o empate si se obtiene la misma cantidad de puntos.
"""
from random import randint

__author__ = 'Jose Cordoba'

print("--- Bienvenido a Appuestas ---")
local = "Caracoles"
visitante = "Plumas"

# Imprimir encuentro deportivo
print("El encuentro de hoy es", local, "vs", visitante)

# Lea los nombres de sus jugadores
jugador_1 = input("Jugador 1 Ingrese su nombre: ")
jugador_2 = input("Jugador 2 Ingrese su nombre: ")


# Complete la función leer resultado
def leer_resultado(nombre_jugador, nombre_equipo):
    """
    (str,str) -> int

    Lee el resultado esperado por un jugador para un equipo y valida
    que este entre 0 y 5


    :param nombre_jugador: El nombre del jugador
    :param nombre_equipo: El nombre del equipo
    :return: int el resultado esperado por el jugador para el equipo
    """
    resultado = input(nombre_jugador + " ¿Que resultado espera para? " + nombre_equipo + ": ")

    try:
        resultado = int(resultado)
    except ValueError:
        print("El resultado debe ser un numero entre 0 y 5")
        resultado = leer_resultado(nombre_jugador, nombre_equipo)

    if 0 <= resultado <= 5:
        return resultado
    else:
        print("El resultado debe ser un numero entre 0 y 5")
        return leer_resultado(nombre_jugador, nombre_equipo)


# Lea los 4 resultados
resultado_local_jugador_1 = leer_resultado(jugador_1, local)
resultado_visitante_jugador_1 = leer_resultado(jugador_1, visitante)
resultado_local_jugador_2 = leer_resultado(jugador_2, local)
resultado_visitante_jugador_2 = leer_resultado(jugador_2, visitante)

# Genere los resultados de cada equipo
resultado_local = randint(0, 5)
resultado_visitante = randint(0, 5)


# Complete la función puntaje_jugador
def puntaje_jugador(resultado_local_real,
                    resultado_visitante_real,
                    resultado_local_jugador,
                    resultado_visitante_jugador):
    """
    (int, int, int, int) -> int

    Calcula el puntaje del jugador siguiendo el sistema de puntos:
        1. Un punto por acertar el equipo ganador.
        2. Dos puntos por acertar el puntaje del equipo local.
        3. Dos puntos por acertar el puntaje del equipo visitante.
        4. Cinco puntos por acertar el resultado total.

    >>> puntaje_jugador(0,0,0,0)
    10
    >>> puntaje_jugador(1,0,2,0)
    3
    >>> puntaje_jugador(3,2,3,4)
    2
    >>> puntaje_jugador(3,0,3,1)
    3

    :param resultado_local_real: el resultado del equipo local
    :param resultado_visitante_real: el resultado del equipo visitante
    :param resultado_local_jugador: el resultado del equipo local esperado
    por el jugador
    :param resultado_visitante_jugador: el resultado del equipo visitante
    esperado por el jugador
    :return: El puntaje obtenido por el jugador
    """

    puntaje = 0

    atino_1 = resultado_local_real > resultado_visitante_real and resultado_local_jugador > resultado_visitante_jugador
    atino_1 = atino_1 or (
            resultado_local_real < resultado_visitante_real and resultado_local_jugador < resultado_visitante_jugador)
    atino_1 = atino_1 or (
            resultado_local_real == resultado_visitante_real and resultado_local_jugador == resultado_visitante_jugador)

    if atino_1:
        puntaje += 1
    if resultado_local_real == resultado_local_jugador:
        puntaje += 2

    if resultado_visitante_real == resultado_visitante_jugador:
        puntaje += 2

    if puntaje == 5:
        puntaje *= 2

    return puntaje


# Calcule el puntaje de cada jugador
puntaje_jugador_1 = puntaje_jugador(resultado_local, resultado_visitante, resultado_local_jugador_1,
                                    resultado_visitante_jugador_1)
puntaje_jugador_2 = puntaje_jugador(resultado_local, resultado_visitante, resultado_local_jugador_2,
                                    resultado_visitante_jugador_2)

# Indique el resultado de la apuesta
print("El partido finalizó con un marcador de", str(resultado_local), "para", local,
      "y", str(resultado_visitante), "para", visitante)
if puntaje_jugador_1 > puntaje_jugador_2:
    print("El ganador es", jugador_1, "con", str(puntaje_jugador_1), "puntos\n")
elif puntaje_jugador_1 < puntaje_jugador_2:
    print("El ganador es", jugador_2, "con", str(puntaje_jugador_2), "puntos\n")
else:
    print("Es un empate entre"
          "", jugador_1, "y", jugador_2,
          "\nDe", puntaje_jugador_1, "puntos\n")

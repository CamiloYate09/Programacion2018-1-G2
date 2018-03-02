"""
La aplicación de apuestas

> Solución de: Jose Cordoba

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
__author__ = 'Jose Cordoba - Manuel Castillo'

print("--- Bienvenido a Appuestas ---")
# local = Cree los nombres de sus equipos
# visitante =
local = 'Patacones'
visitante = 'Empanadas'

# Imprimir encuentro deportivo
print('--- Hoy Juegan', local, "vs", visitante, '---')

# Lea los nombres de sus jugadores
jugador_1 = input("Ingrese el nombre del Jugador 1")
jugador_2 = input("Ingrese el nombre del Jugador 2")


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
    resultado_esperado = input(nombre_jugador + " Ingrese el resultado esperado para " + nombre_equipo)
    try:
        resultado_esperado = int(resultado_esperado)
    except ValueError:
        print(nombre_jugador, "El resultado debe ser un numero entre 0 y 5")
        resultado_esperado = leer_resultado(nombre_jugador, nombre_equipo)
    if resultado_esperado < 0 or resultado_esperado > 5:
        print(nombre_jugador, "El resultado debe ser un numero entre 0 y 5")
        resultado_esperado = leer_resultado(nombre_jugador, nombre_equipo)
    return resultado_esperado


# Lea los 4 resultados
resultado_jugador_1_local = leer_resultado(jugador_1, local)
resultado_jugador_1_visitante = leer_resultado(jugador_1, visitante)
resultado_jugador_2_local = leer_resultado(jugador_2, local)
resultado_jugador_2_visitante = leer_resultado(jugador_2, visitante)

# Genere los resultados de cada equipo
from random import randint

resultado_local = randint(0, 5)
resultado_visitante = randint(0, 5)


# Complete la función puntaje_jugador
def puntaje_jugador(resultado_local,
                    resultado_visitante,
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

    :param resultado_local: el resultado del equipo local
    :param resultado_visitante: el resultado del equipo visitante
    :param resultado_local_jugador: el resultado del equipo local esperado
    por el jugador
    :param resultado_visitante_jugador: el resultado del equipo visitante
    esperado por el jugador
    :return: El puntaje obtenido por el jugador
    """
    puntaje = 0
    equipo_ganador = resultado_local > resultado_visitante and resultado_local_jugador > resultado_visitante_jugador
    equipo_ganador = equipo_ganador or (
            resultado_local < resultado_visitante and resultado_local_jugador < resultado_visitante_jugador)
    equipo_ganador = equipo_ganador or (
            resultado_local == resultado_visitante and resultado_local_jugador == resultado_visitante_jugador)

    if equipo_ganador:
        puntaje += 1

    if resultado_local == resultado_local_jugador:
        puntaje += 2

    if resultado_visitante == resultado_visitante_jugador:
        puntaje += 2

    if puntaje == 5:
        puntaje *= 2

    return puntaje


# Calcule el puntaje de cada jugador
puntaje_jugador_1 = puntaje_jugador(resultado_local,
                                    resultado_visitante,
                                    resultado_jugador_1_local,
                                    resultado_jugador_1_visitante)
puntaje_jugador_2 = puntaje_jugador(resultado_local,
                                    resultado_visitante,
                                    resultado_jugador_2_local,
                                    resultado_jugador_2_visitante)

# Indique el resultado de la apuesta
print("El partido entre", local, "vs", visitante, "terminó con un puntaje de:")
print(str(resultado_local), " para ", local)
print(str(resultado_visitante), " para ", visitante)

if puntaje_jugador_1 > puntaje_jugador_2:
    print("El ganador es", jugador_1, "con", str(puntaje_jugador_1))
elif puntaje_jugador_1 > puntaje_jugador_2:
    print("El ganador es", jugador_2, "con", str(puntaje_jugador_2))
else:
    print("Es un empate entre", jugador_1, 'y', jugador_2, "con", puntaje_jugador_1, "puntos")

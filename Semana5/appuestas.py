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
__author__ = 'Jose Cordoba'

print("--- Bienvenido a Appuestas ---")
# local = Cree los nombres de sus equipos
# visitante =


# Imprimir encuentro deportivo


# Lea los nombres de sus jugadores
jugador_1 = "Jugador 1"
jugador_2 = "Jugador 2"


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


# Lea los 4 resultados

# Genere los resultados de cada equipo
resultado_local = 0
resultado_visitante = 0


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

# Calcule el puntaje de cada jugador

# Indique el resultado de la apuesta

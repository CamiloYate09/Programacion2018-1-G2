"""
Esta aplicación es un robot de chat

Desde tiempos inmmemoriables hemos soñado con máquinas,
que nos ayuden a responder nuestras preguntas. Esta es
su oportunidad de construir una. Diseñe una aplicacion
en python que permita responder a las preguntas dadas
por el usuario, en caso de no conocer la respuesta,
su robot debe estar en capacidad de preguntar la
respuesta correcta y de esa forma aprender a solucionar
futuras inquietudes. Su programa debe continuar chateando
con el usuario hasta que este decida despedirse.
"""

# Trabajamos expresiones regulares y nos apoyamos en
# numpy para salvar nuestro diccionario
import re
from random import randint as rn

import numpy as np

_author_ = 'José Córdoba'
preguntas = ['¿Que necesitas?',
             'Es interesante, pregunta algo mas',
             '¿Que mas quieres saber?',
             'Seguire aprendiendo entre mas preguntes',
             'Me gustaría poder pregrntar cosas com tu',
             '¿Como puedo ayudar?']


def limpiar_cadena(cadena):
    """
    (str) -> str

    >>> limpiar_cadena(" hola mundo ")
    'hola mundo'

    >>> limpiar_cadena(" Hola MundO ")
    'hola mundo'

    >>> limpiar_cadena('Hola$ mundo')
    'hola mundo'

    >>> limpiar_cadena('!@#%$&%#%')
    ''

    Limpia una cadena de caracteres especiales

    :param cadena: La cadena trabajar
    :return: la cadena en minusculas sin caracteres especiales
    """
    return re.sub('\W+', ' ', cadena).strip().lower();


def agregar_al_chat(pregunta, respuesta, chat):
    """
    (str,str) -> None

    Agrega una pregunta y respuesta al chat, dandole formato de minnusculas
    y eliminando signos de puntuación y validando que no exista previamente

    :param pregunta: str la pregunta al chat
    :param respuesta: str la respuesta adecuada
    :param chat: dic of str donde almacenaremos las respuestas
    :return: None
    """
    if not (limpiar_cadena(pregunta) in chat):
        chat[limpiar_cadena(pregunta)] = limpiar_cadena(respuesta)
    else:
        raise ValueError(pregunta + ' ya existe en el robot')


def main():
    """
    Funcion Principal de nuestra app
    :return: None
    """

    # Soporte para guardar nuestro bot
    try:
        chat = np.load('chat.npy').item()
    except:
        chat = {'hola': 'hola',
                'como estas': 'bien muchas gracias',
                'de que color es el cielo': 'El cielo es azul',
                'cual es tu pelicula favorita': 'Mi pelicula favorita es V de venganza'}

    print('Hola, soy un bot que responde a tus preguntas, preguntame algo o di adios'
          ' para salir')

    while True:

        # Preguntamos con una de nuestras frases predeterminadas
        n_pregunta = rn(0, len(preguntas) - 1)
        pregunta = limpiar_cadena(input(preguntas[n_pregunta] + ' '))

        # Validamos que el usuario quiera continuar
        if pregunta == 'adios':
            print('Fue divertido\n')
            # Salvamos nuestro diccionario
            np.save('chat.npy', chat)
            break

        # Si sabemos la respuesta respondemos
        elif pregunta in chat:
            print(chat[pregunta])

        # Si no sabemos preguntamos para aprender
        else:
            respuesta = limpiar_cadena(input('No se como responder eso.\n '
                                             '¿Que debería decir?\n'))
            agregar_al_chat(pregunta, respuesta, chat)


# Corremos nuestra función principal, esto no es necesario pero ayuda a organizar
main()

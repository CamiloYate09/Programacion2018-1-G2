"""
Esta aplicación nos permitirá jugar al ahorcado
"""
from random import randint as ri

_author_ = 'Jose Cordoba'

# Palabras de nuestro juego
palabras = ['casa', 'perro', 'gato', 'pulpo', 'pato', 'leon']

# Intentos de nuestro juego
intentos_restantes = 5

# Generamos la palabra para jugar
palabra_secreta = palabras[ri(0,len(palabras)-1)]

# Generamos las letras disponibles
letras_disponibles = 'qwertyuiopasdfghjklzxcvbnm'

# Generamos las letras adivinadas
letras_adivinadas = ''

# Todo Hacer una función para validar la entrada de una letra
def solicitar_letra():
    """
    (none)->str
    :return: la letra ingresada por el usuario
    """
    letra = input('Ingrese su letra\n').lower()
    if len(letra) != 1:
        print('Ingrese una sola letra')
        letra = solicitar_letra()
    elif not (letra in 'qwertyuiopasdfghjklzxcvbnm'):
        print('Ingrese una letra del alfabeto')
        letra = solicitar_letra()
    return letra


# Todo Hacer una función para crear la cadena de letras adivinadas
def generar_estado_palabra(palabra, letras_adivinadas):
    """
    (str, str) -> str
    Genera la cadena a partir de las letras usadas
    :param palabra: la palabra secreta del usuario
    :param letras_adivinadas: las letras que ha usado el usuario
    :return: la cadena con el mensaje a mostrar
    """
    resultado = ''
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra
        else:
            resultado += ' _ '
    return resultado



print('Bienvenido a ahorcado')
# Todo Recorrer por los turnos
while intentos_restantes > 0:
    print('Le quedan',intentos_restantes,'intentos')
    letra = solicitar_letra()
    if letra in palabra_secreta:
        letras_adivinadas += letra
        print('la letra',letra,'esta en la palabra')
    else:
        print('Opsss la letra',letra, 'no esta en la palabra')
        intentos_restantes -= 1
    letras_disponibles = letras_disponibles.replace(letra,"")
    estado_actual = generar_estado_palabra(palabra_secreta,letras_adivinadas)
    print(estado_actual)
    print('las letras disponibles son',letras_disponibles)
    if estado_actual == palabra_secreta:
        print('Ganaste')
        break

if intentos_restantes == 0:
    print('la palabra era',palabra_secreta, 'lo siento')


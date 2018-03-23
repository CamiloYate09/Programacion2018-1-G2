"""
Version mejorada de la aplicación de lorito
"""
seguimos = True
while seguimos:
    mensaje = input("Soy un loro, paramos?\n")

    if mensaje.lower() == 'si':
        seguimos = False
        print("Suerte")
    else:
        print(mensaje)

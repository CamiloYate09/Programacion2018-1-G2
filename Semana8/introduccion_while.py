# El ciclo while nos permite iterar mientras que una condición sea verdadera
numero = 1
while numero <= 5:
    print(numero)
    numero += 1

# Podemos usar while con cualquier desicion logica
mensaje = ''
while mensaje != 'pare':
    mensaje = input("Soy un loro, diga su mensaje o pare para terminar\n")
    print(mensaje)

# A veces no sabemos cuando queremos parar en un ciclo
# Lo podemos romper con la palabra clave break
while True:
    mensaje = input("Paramos? s/n:\n")
    if mensaje.lower() == 's':
        break
    else:
        print(mensaje)

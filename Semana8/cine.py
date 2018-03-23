"""
Hacer un programa que calcule el precio de una visita al cine con
una cantidad indeterminada de asistentes y siguiendo las siguientes
reglas segun la edad del visitante:
    $0 si es menor de 2 años
    $3 si es menor de 10 años
    $7 si es menor de 20 años
    $10 si es menor de 60 años
    $7 si es mayor o igual que 60
"""

# Creamos la factura
valor_factura = 0

# Preguntamos hasta que se canse el usuario
while True:
    edad = input("Ingrese la edad del visitante\n")

    # Intentamos convertir la edad
    try:
        edad = int(edad)
        if edad < 2:
            valor_factura += 0
        elif edad < 10:
            valor_factura += 3
        elif edad < 20:
            valor_factura += 7
        elif edad < 60:
            valor_factura += 10
        else:
            valor_factura += 7
        if 'n' == input("Desea agregar otro visitante? s/n\n").lower():
            break
    except ValueError:
        print('La edad debe ser un número')

print('El total de su factura es', valor_factura)

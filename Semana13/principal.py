from Semana13.Clases.Hotel import Hotel
from Semana13.Clases.Habitacion import Habitacion
from Semana13.Clases.Reserva import Reserva
from Semana13.create import crear_reservas
from Semana13.read import ver_reservas
from datetime import *
from Semana13.db_handler import *

# cargar los hoteles
hoteles = cargar_hoteles('bd/Hoteles.txt')

# Cargar las habitaciones
# Cargar las reservas
for hotel in hoteles:
    hotel.habitaciones = cargar_habitaciones(
        'bd/habitaciones/'+hotel.nombre+'.txt')
    for habitacion in hotel.habitaciones:
        archivo = 'bd/reservas/' + \
                  hotel.nombre + \
                  habitacion.numero + '.txt'
        try:
            habitacion.reservas = cargar_reservas(archivo)
        except FileNotFoundError:
            f = open(archivo, "w+")

while True:
    print('Bienvenido a el vago')
    print('Seleccione una opción')
    print('1. Crear reserva')
    print('2. Consultar reservas')
    seleccion = input('Para salir use cualquier otra tecla\n')
    if seleccion == '1':
        crear_reservas(hoteles)
    elif seleccion == '2':
        ver_reservas(hoteles)
    else:
        print('Hasta luego')
        break


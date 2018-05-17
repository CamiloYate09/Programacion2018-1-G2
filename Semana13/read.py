from Semana13.Clases.Hotel import Hotel
from Semana13.Clases.Habitacion import Habitacion
from Semana13.Clases.Reserva import Reserva
from datetime import *
from Semana13.db_handler import *

def ver_reservas(hoteles):
    while True:
        print('Los hoteles disponibles son')
        for i in range(0, len(hoteles)):
            print(i, '. ', hoteles[i])

        # Preguntar el hotel
        hotel_seleccionado = int(input('Seleccione el '
                                        'numero del hotel\n'))
        print('Seleccionó', hoteles[hotel_seleccionado])
        print('Las habitaciones disponibles son')

        # Mostrar las habitaciones disponibles
        hotel_seleccionado = hoteles[hotel_seleccionado]
        for i in range(0, len(hotel_seleccionado.habitaciones)):
            print(i, '. ', hotel_seleccionado.habitaciones[i])

        # Preguntar la habitación
        habitacion_seleccionada = int(input('Seleccione el '
                                            'numero de la habitación\n'))

        habitacion_seleccionada = \
            hotel_seleccionado.habitaciones[habitacion_seleccionada]
        print('Seleccionó', habitacion_seleccionada)

        print('Las reservas para la habitación son')

        for reserva in habitacion_seleccionada.reservas:
            print(reserva)

        seleccion = input('¿Desea ver otra reserva? S/N\n')
        if seleccion.upper() == 'N':
            break

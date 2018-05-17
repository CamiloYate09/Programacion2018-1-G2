from Semana13.Clases.Hotel import Hotel
from Semana13.Clases.Habitacion import Habitacion
from Semana13.Clases.Reserva import Reserva
from datetime import *
from Semana13.db_handler import *

def crear_reservas(hoteles):
    while True:

        # Mostrar los hoteles disponibles
        for i in range(0, len(hoteles)):
            print(i, '. ', hoteles[i])

        # Preguntar el hotel
        while True:
            try:
                hotel_seleccionado = int(input('Seleccione el '
                                           'numero del hotel\n'))
                break
            except:
                print('No seleccionó un hotel valido')

        print('Seleccionó', hoteles[hotel_seleccionado])
        print('Las habitaciones disponibles son')

        # Mostrar las habitaciones disponibles
        hotel_seleccionado = hoteles[hotel_seleccionado]
        for i in range(0, len(hotel_seleccionado.habitaciones)):
            print(i, '. ', hotel_seleccionado.habitaciones[i])

        # Preguntar la habitación
        while True:
            try:
                habitacion_seleccionada = int(input('Seleccione el '
                                            'numero de la habitación\n'))
                break
            except:
                print('Seleccione una habitación valida')
        habitacion_seleccionada = \
            hotel_seleccionado.habitaciones[habitacion_seleccionada]
        print('Seleccionó', habitacion_seleccionada)

        # Preguntar la fecha deseada
        nombre_cliente = input('Ingrese su nombre\n')
        cedula_cliente = input('Ingrese su cedula\n')
        while True:
            try:
                fecha_inicio_reserva = datetime.strptime(
                    input('Ingrese la fecha inicial en formato dd/mm/yyyy\n'),
                    '%d/%m/%Y').date()
                fecha_fin_reserva = datetime.strptime(
                    input('Ingrese la fecha final en formato dd/mm/yyyy\n'),
                    '%d/%m/%Y').date()

                # Generar la reserva
                reserva = Reserva(nombre_cliente,
                                  cedula_cliente,
                                  fecha_inicio_reserva,
                                  fecha_fin_reserva)
                habitacion_seleccionada.reservar(reserva)
                break
            except ValueError:
                print('No hay disponibilidad para las fechas seleccionadas')

        # Guardar la reserva
        guardar_reserva(hotel_seleccionado,
                        habitacion_seleccionada,
                        reserva)

        continuar = input('Desea agregar otra reserva? S/N\n')

        if (continuar.upper() == 'N'):
            break
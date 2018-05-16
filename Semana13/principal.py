from Semana13.Clases.Hotel import Hotel
from Semana13.Clases.Habitacion import Habitacion
from Semana13.Clases.Reserva import Reserva
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

    # Mostrar los hoteles disponibles
    for i in range(0,len(hoteles)):
        print(i,'. ', hoteles[i])

    # Preguntar el hotel
    hotel_seleccionado = int(input('Seleccione el '
                                   'numero del hotel\n'))
    print('Seleccionó',hoteles[hotel_seleccionado])
    print('Las habitaciones disponibles son')

    # Mostrar las habitaciones disponibles
    hotel_seleccionado = hoteles[hotel_seleccionado]
    for i in range(0,len(hotel_seleccionado.habitaciones)):
        print(i,'. ',hotel_seleccionado.habitaciones[i])


    # Preguntar la habitación
    habitacion_seleccionada = int(input('Seleccione el '
                                   'numero de la habitación\n'))
    habitacion_seleccionada = \
        hotel_seleccionado.habitaciones[habitacion_seleccionada]
    print('Seleccionó',habitacion_seleccionada)

    # Preguntar la fecha deseada
    nombre_cliente = input('Ingrese su nombre\n')
    cedula_cliente = input('Ingrese su cedula\n')
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


    # Guardar la reserva
    f = open('bd/reservas/'+
             hotel_seleccionado.nombre+
             habitacion_seleccionada.numero+
             '.txt','a')
    f.write(reserva.cliente+','
            +reserva.cedula+','+
            str(reserva.fecha_inicio)+','
            +str(reserva.fecha_fin)+'\n')
    f.close()

    continuar = input('Desea agregar otra reserva?S/N\n')

    if(continuar.upper() == 'N'):
        break
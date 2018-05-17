from Semana13.Clases.Hotel import Hotel
from Semana13.Clases.Habitacion import Habitacion
from Semana13.Clases.Reserva import Reserva
from datetime import *

def cargar_hoteles(file):
    """

    :param file:
    :return:
    """
    hoteles_resultante = []
    with open(file) as bd_Hoteles:
        lineas = bd_Hoteles.readlines()
        for linea in lineas:
            variables = linea.strip().split(',')
            hoteles_resultante.append(Hotel(variables[0],
                                 variables[1],
                                 variables[2:]))
        bd_Hoteles.close()
    return hoteles_resultante


def cargar_habitaciones(file):
    habitaciones_resultantes = []
    with open(file) as bd_Habitcion:
        lineas = bd_Habitcion.readlines()
        for linea in lineas:
            variables = linea.strip().split(',')
            habitaciones_resultantes.append(Habitacion(variables[0],
                                                       variables[1]))
        bd_Habitcion.close()
    return habitaciones_resultantes

def cargar_reservas(file):
    reservas_resultantes = []
    with open(file) as bd_reservas:
        lineas = bd_reservas.readlines()
        for linea in lineas:
            variables = linea.strip().split(',')
            fecha_inicio = datetime.strptime(
                variables[2],'%Y-%m-%d').date()
            fecha_fin = datetime.strptime(
                variables[3], '%Y-%m-%d').date()
            reservas_resultantes.append(Reserva(
                variables[0],
                variables[1],
                fecha_inicio,
                fecha_fin
            ))
        bd_reservas.close()
    return reservas_resultantes


def guardar_reserva(hotel, habitacion, reserva):
    f = open('bd/reservas/' +
             hotel.nombre +
             habitacion.numero +
             '.txt', 'a')
    f.write(reserva.cliente + ','
            + reserva.cedula + ',' +
            str(reserva.fecha_inicio) + ','
            + str(reserva.fecha_fin) + '\n')
    f.close()
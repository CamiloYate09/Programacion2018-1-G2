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
    return hoteles_resultante


def cargar_habitaciones(file):
    habitaciones_resultantes = []
    with open(file) as bd_Habitcion:
        lineas = bd_Habitcion.readlines()
        for linea in lineas:
            variables = linea.strip().split(',')
            habitaciones_resultantes.append(Habitacion(variables[0],
                                                       variables[1]))
    return habitaciones_resultantes

def cargar_reservas(file):
    reservas_resultantes = []
    with open(file) as bd_reservas:
        lineas = bd_reservas.readlines()
        for linea in lineas:
            variables = linea.strip().split(',')
            fecha_inicio = datetime.strptime(
                variables[2],'%Y-%d-%m').date()
            fecha_fin = datetime.strptime(
                variables[3], '%Y-%d-%m').date()
            reservas_resultantes.append(Reserva(
                variables[0],
                variables[1],
                fecha_inicio,
                fecha_fin
            ))
    return reservas_resultantes
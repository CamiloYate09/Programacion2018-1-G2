from Semana13.Clases.Reserva import Reserva

class Habitacion:

    reservas = []

    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo


    def reservar(self, nueva_reserva):
        for reserva in self.reservas:
            if(reserva.coliciona(nueva_reserva)):
                raise ValueError('La habitación no se'
                                 ' encuentra disponible '
                                 'para esa fecha')
        self.reservas.append(nueva_reserva)


    def __repr__(self):
        return 'Habitación # '+self.numero\
               + ' de tipo '+self.tipo+' Tiene '\
               + str(len(self.reservas))+ ' reservas'
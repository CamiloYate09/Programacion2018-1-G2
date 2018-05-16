from datetime import *

class Reserva:
    """
    Representa una reserva de una habitación
    """

    def __init__(self, cliente, cedula, fecha_inicio, fecha_fin):
        """

        Crea una nueva instancia de reserva

        :param cliente:
        :param cedula:
        :param fecha_inicio:
        :param fecha_fin:
        """
        if fecha_inicio > datetime.now().date() and \
                fecha_inicio < fecha_fin:
            self.cliente = cliente
            self.cedula = cedula
            self.fecha_inicio = fecha_inicio
            self.fecha_fin = fecha_fin
        else:
            raise ValueError('La fecha reserva debe ser mayor a '
                             'hoy y la fecha inicial mayor a la '
                             'fecha final')

    def coliciona(self, other):
        """
        :param other:
        :return:
        """
        if isinstance(other, Reserva):
            return (other.fecha_inicio >= self.fecha_inicio and \
                   other.fecha_inicio <=self.fecha_fin) or \
                   (other.fecha_fin >= self.fecha_inicio and \
                   other.fecha_fin <=self.fecha_fin)
        raise ValueError('No puedo comprar reservas con '
                         +type(other).__name__)

    def __repr__(self):
        return 'Reserva de '+self.cliente\
               +' cedula '+self.cedula+ \
               ' desde '+str(self.fecha_inicio)+ \
               ' hasta '+ str(self.fecha_fin)
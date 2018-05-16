from Semana13.Clases.Habitacion import Habitacion

class Hotel:

    habitaciones = []

    def __init__(self, nombre, estrellas, servicios):
        self.nombre = nombre
        self.estrellas = estrellas
        self.servicios = servicios

    def __repr__(self):
        return 'Hotel '+ self.nombre +' de '+ \
               self.estrellas + ' presta los servicios de '\
               + str(self.servicios)

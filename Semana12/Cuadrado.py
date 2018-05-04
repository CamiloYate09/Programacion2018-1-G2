from Semana12.Figura import Figura

class Cuadrado(Figura):
    """
    Representa un cuadrado
    """
    tamano = 'small'
    color = 'blanco'
    lado = 4

    def __init__(self, tamano, color, lado):
        """
        Crea una nueva instancia de cuadrado

        :param tamano: el tamaño del Cuadrado
        :param color: el color del cuadrado
        :param lado: la longitud del lado del cuadrado
        """
        Figura.__init__(self,4)
        self.tamano = tamano
        self.color = color
        self.lado = lado

    def __repr__(self):
        return 'Cuadrado de tamaño '+ self.tamano \
               + ' de color ' + self.color \
               + ' sus lados miden ' + str(self.lado) + ' unidades'

    def area(self):
        """
        Calcula el area del cuadrado
        :return: num El area del cuadrado
        """
        return self.lado ** 2
from Semana12.Figura import Figura

class Triangulo(Figura):
    """
    Representa un cuadrado
    """
    tamano = 'small'
    color = 'blanco'
    lados = []

    def __init__(self, tamano, color, lado_1 , lado_2, lado_3):
        """
        Crea una nueva instancia de Triangulo

        :param tamano: el tamaño del triangulo
        :param color: el color del triangulo
        :param lado_1: la longitud del primer lado
        :param lado_2: la longitud del segundo lado
        :param lado_3: la longitud del tercer lado
        """
        Figura.__init__(self,4)
        self.tamano = tamano
        self.color = color
        self.lados.append(lado_1)
        self.lados.append(lado_2)
        self.lados.append(lado_3)

    def __repr__(self):
        return 'Triangulo de tamaño '+ self.tamano \
               + ' de color ' + self.color \
               + ' sus lados ' + str(self.lados) + ' unidades'

    def area(self):
        """
        Calcula el area del cuadrado
        :return: num El area del cuadrado
        """
        s_p = (self.lados[0] + self.lados[1] + self.lados[2]) / 2
        return (s_p*(s_p-self.lados[0])*(s_p-self.lados[1])*(s_p-self.lados[2]))**(1/2)
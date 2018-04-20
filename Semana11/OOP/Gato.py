class Gato:
    """
    Representa un gato
    """

    def __init__(self, nombre, color, edad):
        """
        Inicializa un gato con su color y edad

        :param color: el color del gato
        :param edad: la edad del gato
        """
        self.nombre = nombre
        self.color = color
        self.edad = edad

    def ronnorear(self):
        """
        simula el ronroneo de un gato
        :return: el sonido del gato
        """
        return 'prrrrr'

    def __repr__(self):
        """
        Retorna una cadena con la representación en texto
        de nuestro gato
        :return: str
        """
        return self.nombre + ' un gato de color ' + \
               self.color + ' y tiene ' + \
               str(self.edad) + ' años de vida'

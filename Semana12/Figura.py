class Figura:
    """
    Representa una figura geométrica
    """

    numero_lados = 0

    def __init__(self, numero_lados):
        """
        Crea una nueva figura

        :param numero_lados: el numero de lados de la figura
        """
        self.numero_lados = numero_lados

    def dibujar(self, pos_x, pos_y):
        """
        Dibuja la figura

        :param pos_x: la posicion en x de la figura
        :param pos_y: la posicion en y de la figura
        :return: str representa el dibujo de la figura
        """
        pass

    def __repr__(self):
        """
        Genera la representación en forma de cadena de la
        figura
        :return: str con el numero de lados de la figura
        """
        return 'Esta figura tiene '+str(self.numero_lados) \
               + ' lados'



class Guarderia:
    """
    Representa una guarderia de Gatos
    """

    def __init__(self, nombre, veterinario):
        """
        Construye una nueva guardería

        :param nombre: str El nombre de nuestra guardería
        :param veterinario: str El nombre del vetrinario a cargo
        """
        self.nombre = nombre
        self.veterinario = veterinario
        self.mascotas = []

    def __repr__(self):
        """
        :return: str, Retorna una representacion de nuestra guarderia
        """
        return "Guarderia " + self.nombre + \
               '. ' + self.veterinario + ' esta a cargo. ' \
               + 'Contamos con ' + str(len(self.mascotas)) \
               + ' Huespedes'

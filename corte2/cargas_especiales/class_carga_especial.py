from pasajeros.class_pasajero import Pasajero


class Carga_Especial:

    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo
    @property
    def peso(self):
        return self._peso
    @peso.setter
    def peso(self, peso):
        self._peso = peso

    def __init__(self, tipo, peso):

        self._tipo = tipo
        self._peso = peso

    def calcular_costo(self):
        if self.tipo == "bicicleta":
            return self.peso * 10000
        elif self.tipo == "perro":
            return self.peso * 20000
        elif self.tipo == "gato":
            return self.peso * 15000
        else:
            return 0
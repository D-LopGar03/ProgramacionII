from abc import ABC, abstractmethod

class Carga_Especial:

    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo
    @property
    def peso(self):
        return self.__peso
    @peso.setter
    def peso(self, peso):
        self.__peso = peso

    @property
    def costo_base(self):
        return self.__costo_base
    @costo_base.setter
    def costo_base(self, costo_base):
        self.__costo_base = costo_base

    def __init__(self, tipo, peso, costo_base):

        if tipo not in self.tipo_permitido:
            raise ValueError(f"Tipo de carga especial '{tipo}' no permitido.")
        if peso <= 0:
            raise ValueError("El peso debe ser mayor a cero.")

        self.__tipo = tipo
        self.__peso = peso
        self.__costo_base = costo_base



    @abstractmethod
    def calcular_costo_carga_especial(self):
        pass
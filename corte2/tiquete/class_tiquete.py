from abc import ABC, abstractmethod
from pasajeros.class_pasajero import Pasajero


class Tiquete(ABC):
    def __init__(self, pasajero: Pasajero, costo_base: float, embarazada: bool = False):
        self.__pasajero = pasajero
        self.__costo_base = costo_base
        self.__embarazada = embarazada

    @property
    def pasajero(self):
        return self.__pasajero
    @pasajero.setter
    def pasajero(self, value: Pasajero):
        if not isinstance(value, Pasajero):
            raise ValueError("El pasajero debe ser una instancia de la clase Pasajero")
        self.__pasajero = value


    @property
    def embarazada(self):
        return self.__embarazada

    @embarazada.setter
    def embarazada(self, value: bool):
        if value and self.__pasajero.sexo != 'F':
            raise ValueError(
                "Solo pasajeras femeninas pueden estar embarazadas")
        self.__embarazada = value

    def aplicar_descuentos(self, subtotal: float):

        descuento = 0.0

        if self.__pasajero.es_infante():
            
            print("Infante detectado")
            descuento += 0.07

        if self.__pasajero.es_adulto_mayor():
            descuento += 0.05

        if self.__embarazada:
            print("Pasajera embarazada detectada")
            descuento += 0.10

        return subtotal * descuento


    def calcular_total(self):
        costo_equipaje = self.calcular_costo_equipaje()
        subtotal = self.__costo_base + costo_equipaje
        print("Subtotal:", subtotal)
        print("Costo equipaje:", costo_equipaje)
        print("Descuento:", self.aplicar_descuentos(subtotal))
        total = subtotal - self.aplicar_descuentos(subtotal)
        return total

    @abstractmethod
    def calcular_costo_equipaje(self):
        pass
from abc import ABC, abstractmethod
from pasajeros.class_pasajero import Pasajero
from cargas_especiales.class_carga_especial import Carga_Especial


class Tiquete(ABC):
    def __init__(self, pasajero: Pasajero, costo_base: float, embarazada: bool = False):

        if costo_base <= 0:
            raise ValueError("El costo base debe ser mayor a cero")
    
        self._pasajero = pasajero
        self._costo_base = costo_base
        self._embarazada = embarazada
        self._carga_especial = []

    @property
    def pasajero(self):
        return self._pasajero
    @pasajero.setter
    def pasajero(self, value: Pasajero):
        if not isinstance(value, Pasajero):
            raise ValueError("El pasajero debe ser una instancia de la clase Pasajero")
        self._pasajero = value


    @property
    def embarazada(self):
        return self._embarazada

    @embarazada.setter
    def embarazada(self, value: bool):
        if value and self._pasajero.sexo != 'F':
            raise ValueError(
                "Solo pasajeras femeninas pueden estar embarazadas")
        self._embarazada = value

    def aplicar_descuentos(self, subtotal: float):

        descuento = 0.0

        if self._pasajero.es_infante():
            
            descuento += 0.07

        if self._pasajero.es_adulto_mayor():
            descuento += 0.05

        if self._embarazada:
            descuento += 0.10

        return subtotal * descuento


    def calcular_total(self):
        costo_equipaje = self.calcular_costo_equipaje()
        costo_carga_especial = self.calcular_costo_carga_especial()
        subtotal = self._costo_base + costo_equipaje + costo_carga_especial
        
        print(f"\nDetalle de cálculo:")
        print(f"- Costo base: ${self._costo_base:,.2f}")
        print(f"- Costo equipaje: ${costo_equipaje:,.2f}")
        print(f"- Costo carga especial: ${costo_carga_especial:,.2f}")
        print(f"- Subtotal: ${subtotal:,.2f}")
        
        descuento = self.aplicar_descuentos(subtotal)
        total = subtotal - descuento
        
        print(f"- Descuentos aplicados: ${descuento:,.2f}")
        print(f"- TOTAL A PAGAR: ${total:,.2f}")
        
        return total

    @abstractmethod
    def calcular_costo_equipaje(self):
        pass
    @abstractmethod
    def calcular_costo_carga_especial(self):
        pass
    
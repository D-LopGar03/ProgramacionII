from tiquete.class_tiquete import Tiquete
from pasajeros.class_pasajero import Pasajero

class TiqueteEconomico(Tiquete):
    KILOS_GRATIS = 10
    COSTO_POR_KILO = 5000
    
    def __init__(self, pasajero: Pasajero, costo_base: float, kilos_equipaje: float):
        super().__init__(pasajero, costo_base)
        self.__kilos_equipaje = kilos_equipaje

    @property
    def kilos_equipaje(self):
        return self.__kilos_equipaje
    
    @kilos_equipaje.setter
    def kilos_equipaje(self, value: float):
        if value < 0:
            raise ValueError("Los kilos de equipaje no pueden ser negativos")
        self.__kilos_equipaje = value
    
    def calcular_costo_equipaje(self):
        exceso = self.__kilos_equipaje - self.KILOS_GRATIS
        return exceso * self.COSTO_POR_KILO
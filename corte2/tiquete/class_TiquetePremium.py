from tiquete.class_tiquete import Tiquete
from pasajeros.class_pasajero import Pasajero
from cargas_especiales.class_carga_especial import Carga_Especial
from cargas_especiales.class_bicicleta import Bicicleta
from cargas_especiales.class_perro import Perro
from cargas_especiales.class_gato import Gato
from cargas_especiales.class_otro import Otro

class TiquetePremium(Tiquete):
    KILOS_GRATIS = 30
    COSTO_POR_KILO = 0.01

    def __init__(self, pasajero: Pasajero, costo_base: float, kilos_equipaje: float, carga_especial: Carga_Especial = None):
        super().__init__(pasajero, costo_base)
        self.__kilos_equipaje = kilos_equipaje
        self.__costo_base = costo_base
        self.__carga_especial = carga_especial
    
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
        return exceso * (self.__costo_base * self.COSTO_POR_KILO)
    
    def calcular_costo_carga_especial(self):
        if self.__carga_especial:
            return self.__carga_especial.calcular_costo_carga_especial()
        return 0
        
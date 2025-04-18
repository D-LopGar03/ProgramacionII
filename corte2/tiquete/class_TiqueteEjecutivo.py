from tiquete.class_tiquete import Tiquete
from pasajeros.class_pasajero import Pasajero
from cargas_especiales.class_carga_especial import Carga_Especial
from cargas_especiales.class_bicicleta import Bicicleta
from cargas_especiales.class_perro import Perro
from cargas_especiales.class_gato import Gato
from cargas_especiales.class_otro import Otro

class TiqueteEjecutivo(Tiquete):
    KILOS_GRATIS = 20
    COSTO_POR_KILO = 10000
    
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
    
    def calcular_costo_carga_especial(self):
        return sum(carga.calcular_costo_carga_especial() for carga in self._carga_especial)

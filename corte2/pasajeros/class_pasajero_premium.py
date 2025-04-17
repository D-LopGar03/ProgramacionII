from pasajeros.class_pasajero import Pasajero


class Pasajero_Premium(Pasajero):

    KILOS_GRATIS = 30
    COSTO_KILO_EXTRA = 0.01

    def calcular_costo_equipaje_extra(self):
        if self.kilo_equipaje > self.KILOS_GRATIS:
            return (self.kilo_equipaje - self.KILOS_GRATIS) * (self.costo_tiquete * self.COSTO_KILO_EXTRA)
        return 0


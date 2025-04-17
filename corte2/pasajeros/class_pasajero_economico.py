from pasajeros.class_pasajero import Pasajero


class Pasajero_Economico(Pasajero):

    KILOS_GRATIS = 10
    COSTO_KILO_EXTRA = 5000

    def calcular_costo_equipaje_extra(self):
        if self.kilo_equipaje > self.KILOS_GRATIS:
            return (self.kilo_equipaje - self.KILOS_GRATIS) * self.COSTO_KILO_EXTRA
        return 0


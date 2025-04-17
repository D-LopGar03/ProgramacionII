from pasajeros.class_pasajero import Pasajero


class Pasajero_Ejecutivo(Pasajero):

    KILOS_GRATIS = 20
    COSTO_KILO_EXTRA = 10000

    def calcular_costo_equipaje_extra(self):
        if self.kilo_equipaje > self.KILOS_GRATIS:
            return (self.kilo_equipaje - self.KILOS_GRATIS) * self.COSTO_KILO_EXTRA
        return 0





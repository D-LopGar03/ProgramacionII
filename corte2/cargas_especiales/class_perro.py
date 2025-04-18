from cargas_especiales.class_carga_especial import Carga_Especial 

class Perro(Carga_Especial):
    
    VALOR_MASCOTA = 0.05

    @property
    def costo_base(self):
        return self._costo_base
    @costo_base.setter
    def costo_base(self, costo_base):
        self._costo_base = costo_base
    
    def __init__(self, costo_base):
        self._costo_base = costo_base
    
    def calcular_costo_carga_especial(self):
        return self._costo_base + (self._costo_base * self.VALOR_MASCOTA)
    
    def __str__(self):
        return f"Perro: {self._costo_base} kg"

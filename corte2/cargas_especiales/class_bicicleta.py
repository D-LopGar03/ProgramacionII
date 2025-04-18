from cargas_especiales.class_carga_especial import Carga_Especial 

class Bicicleta(Carga_Especial):
    
    VALOR_KILO = 15000
    
    def __init__(self, peso):
        self._peso = peso
    
    def calcular_costo_carga_especial(self):
        return self._peso * self.VALOR_KILO
    
    def __str__(self):
        return f"Bicicleta: {self._peso} kg"

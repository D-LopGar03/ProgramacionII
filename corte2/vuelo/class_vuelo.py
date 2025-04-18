from ciudad.class_ciudad import Ciudad
from tiquete.class_tiquete import Tiquete

class Vuelo:
    def __init__(self, origen: Ciudad, destino: Ciudad, fecha: str, codigo: str):


        if origen.nombre == destino.nombre:
            raise ValueError("La ciudad de origen y destino no pueden ser la misma.")
        if not fecha or len(fecha) == 0:
            raise ValueError("La fecha no puede estar vacía.")
        
        if len(self.tiquetes) == 0:
            raise ValueError("El vuelo no tiene tiquetes asignados.")

        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.codigo = codigo
        self.tiquetes = []

    def agregar_tiquete(self, tiquete: Tiquete):
        self.tiquetes += (tiquete,)

    @property
    def tiquetes(self):
        return self.tiquetes
    
    def __str__(self):
        return f"Vuelo {self.codigo}: {self.origen} -> {self.destino} ({self.fecha})"

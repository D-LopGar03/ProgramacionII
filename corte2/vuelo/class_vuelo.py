from ciudad.class_ciudad import Ciudad
from tiquete.class_tiquete import Tiquete

class Vuelo:
    MAX_TIQUETES = 200

    def __init__(self, origen: Ciudad, destino: Ciudad, fecha: str, codigo: str, tiquetes: list):

        if origen.nombre == destino.nombre:
            raise ValueError("La ciudad de origen y destino no pueden ser la misma.")
        if not fecha:
            raise ValueError("La fecha no puede estar vacía.")
        if not tiquetes or len(tiquetes) == 0:
            raise ValueError("El vuelo debe tener al menos un tiquete asignado.")
        if len(tiquetes) > Vuelo.MAX_TIQUETES:
            raise ValueError("No se pueden asignar más de 200 tiquetes al vuelo.")

        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.codigo = codigo
        self._tiquetes = tiquetes

    def agregar_tiquete(self, tiquete: Tiquete):
        if len(self._tiquetes) >= Vuelo.MAX_TIQUETES:
            raise ValueError("Este vuelo ya tiene el máximo de 200 tiquetes.")
        self._tiquetes.append(tiquete)

    @property
    def tiquetes(self):
        return self._tiquetes

    def __str__(self):
        return f"Vuelo {self.codigo}: {self.origen} -> {self.destino} ({self.fecha})"
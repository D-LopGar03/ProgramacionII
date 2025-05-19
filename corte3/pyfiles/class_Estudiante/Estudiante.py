class Estudiante:

    def __init__(self, nombre, genero, edad, estrato):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        self.estrato = estrato

    @property
    def estrato(self):
        return self._estrato

    @estrato.setter
    def estrato(self, value):
        if value in {1, 2, 3, 4, 5, 6}:
            self._estrato = value
        else:
            raise ValueError("Estrato debe ser estar entre 1 y 6.")

    def __str__(self):
        return f"Estudiante: {self.nombre}, {self.genero}, {self.edad} años, Estrato {self.estrato}"
    

    
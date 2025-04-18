class Ciudad:
    def __init__(self, nombre: str, pais: str):
        self.nombre = nombre.title()
        self.pais = pais.title()
    
    def __str__(self):
        return f"{self.nombre}, {self.pais}"
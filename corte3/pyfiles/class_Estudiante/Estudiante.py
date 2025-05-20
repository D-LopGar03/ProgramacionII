class Estudiante:

    def __init__(self, nombre, genero, edad, estrato, asignatura, valor_pagar):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        self.estrato = estrato
        self.asignatura = asignatura

        if estrato == 1:
            self.valor_pagar = valor_pagar * 0.5
        elif estrato == 2:
            self.valor_pagar = valor_pagar * 0.3
        elif estrato == 3:
            self.valor_pagar = valor_pagar * 0.2
        else: 
            self.valor_pagar = valor_pagar

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
        return f"Estudiante: {self.nombre},\nGénero{self.genero},\nEdad: {self.edad} años,\nEstrato: {self.estrato}, \nAsignatura: {self.asignatura},\nValor a pagar: {self.valor_pagar}\n"
    
    

    
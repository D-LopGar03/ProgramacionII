class Estudiante:

    GENEROS_VALIDOS = {'M': 'Masculino', 'F': 'Femenino'}

    def __init__(self, nombre, genero, edad, estrato, asignatura, valor_pagar):
        self.nombre = nombre
        self.genero = genero 
        self.edad = edad
        self.estrato = estrato  
        self.asignatura = asignatura

        
        if estrato == 1:
            self.valor_pagar = round(valor_pagar * 0.5, 2)
        elif estrato == 2:
            self.valor_pagar = round(valor_pagar * 0.3, 2)
        elif estrato == 3:
            self.valor_pagar = round(valor_pagar * 0.2, 2)
        else:
            self.valor_pagar = round(valor_pagar, 2)

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, value):
        if value in Estudiante.GENEROS_VALIDOS:
            self._genero = value
        else:
            raise ValueError("Género inválido. Debe ser 'M' o 'F'.")

    @property
    def estrato(self):
        return self._estrato

    @estrato.setter
    def estrato(self, value):
        if value in {1, 2, 3, 4, 5, 6}:
            self._estrato = value
        else:
            raise ValueError("Estrato debe estar entre 1 y 6.")

    def __str__(self):
        genero_completo = Estudiante.GENEROS_VALIDOS[self.genero]
        return (
            f"[Estudiante: {self.nombre},\n"
            f"Género: {genero_completo},\n"
            f"Edad: {self.edad} años,\n"
            f"Estrato: {self.estrato},\n"
            f"Asignatura: {self.asignatura},\n"
            f"Valor a pagar: ${self.valor_pagar}\n]"
        )

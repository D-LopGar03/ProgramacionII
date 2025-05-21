from unidecode import unidecode

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
    def nombre(self):
        return self._nombre
    

    @nombre.setter
    def nombre(self, nombre):
        if len(nombre) == 0:
            raise ValueError("El nombre no puede ser nulo")
        self._nombre = nombre
    

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
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, value):
        if value < 13:
            raise ValueError("El estudiante debe de tener como mínimo 13 años.")
        self._edad = value


    @property
    def estrato(self):
        return self._estrato

    @estrato.setter
    def estrato(self, value):
        if value in {1, 2, 3, 4, 5, 6}:
            self._estrato = value
        else:
            raise ValueError("Estrato debe estar entre 1 y 6.")
        

    @property
    def asignatura(self):
        return self._asignatura

    @asignatura.setter
    def asignatura(self, value):
        if isinstance(value, str):
            value = unidecode(value).upper()
            value = value.replace('1', 'I').replace('2', 'II').replace('3', 'III') \
                         .replace('4', 'IV').replace('5', 'V')
            self._asignatura = value
        else:
            raise TypeError("El nombre de la asignatura debe ser una cadena de texto.")

    

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

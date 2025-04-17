class Pasajero:
    def __init__(self, identificacion: str, nombre: str, edad: int, sexo: str, embarazada: bool = False):
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__embarazada = embarazada
    
    @property
    def identificacion(self):
        return self.__identificacion
    
    @identificacion.setter
    def identificacion(self, value: str):
        if not value or value.strip() == "":
            raise ValueError("La identificación no puede estar vacía")
        self.__identificacion = value.strip()
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, value: str):
        value = value.strip().title()
        if not value:
            raise ValueError("El nombre no puede estar vacío")
        self.__nombre = value
    
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, value: int):
        if not (0 <= value <= 120):
            raise ValueError("La edad debe estar entre 0 y 120 años")
        self.__edad = value
    
    @property
    def sexo(self):
        return self.__sexo
    
    @sexo.setter
    def sexo(self, value: str):
        value = value.upper()
        if value not in ['M', 'F']:
            raise ValueError("Sexo debe ser 'M' o 'F'")
        self.__sexo = value
    
    @property
    def embarazada(self):
        return self.__embarazada
    
    @embarazada.setter
    def embarazada(self, value: bool):
        if value and self.sexo != 'F':
            raise ValueError("Solo pasajeras femeninas pueden estar embarazadas")
        self.__embarazada = value
    
    def es_infante(self):
        return 0 <= self.edad <= 13
    
    def es_adulto_mayor(self):
        return self.edad >= 65
    
from abc import ABC, abstractmethod


class Pasajero(ABC):

    @property
    def identificacion(self):
        return self.__identificacion

    @identificacion.setter
    def identificacion(self, identificacion):
        self.__identificacion = identificacion

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    @property
    def kilo_equipaje(self):
        return self.__kilo_equipaje

    @kilo_equipaje.setter
    def kilo_equipaje(self, kilo_equipaje):
        self.__kilo_equipaje = kilo_equipaje

    @property
    def costo_tiquete(self):
        return self.__costo_tiquete

    @costo_tiquete.setter
    def costo_tiquete(self, costo_tiquete):
        self.__costo_tiquete = costo_tiquete

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, sexo):
        self.__sexo = sexo

    @property
    def embarazada(self):
        return self.__embarazada

    @embarazada.setter
    def embarazada(self, embarazada):
        self.__embarazada = embarazada

    def __init__(self, identificacion, nombre, edad, kilo_equipaje, costo_tiquete, sexo, embarazada=False):

        self.__identificacion = self.__validar_identificacion(identificacion)
        self.__nombre = self.__validar_nombre(nombre)
        self.__edad = self.__validar_edad(edad)
        self.__kilo_equipaje = self.__validar_kilos(kilo_equipaje)
        self.__costo_tiquete = self.__validar_costo(costo_tiquete)
        self.__sexo = self.__validar_sexo(sexo)
        self.__embarazada = self.__validar_embarazo(embarazada, self.__sexo)

    def __validar_identificacion(self, identificacion):

        if identificacion <= 0:
            raise ValueError("La identificación debe de ser mayor a cero.")
        return identificacion

    def __validar_nombre(self, nombre):
        nombre = nombre.strip().title()
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        return nombre

    def __validar_edad(self, edad):
        if not (0 <= edad <= 120):
            raise ValueError("La edad debe estar entre 0 y 120 años.")
        return edad

    def __validar_kilos(self, kilos):
        if kilos < 0 or kilos > 100:
            raise ValueError("El equipaje debe estar entre 0 y 70 kg.")
        return kilos

    def __validar_costo(self, costo):
        if costo < 0:
            raise ValueError("El costo del tiquete no puede ser negativo.")
        return costo

    def __validar_sexo(self, sexo):
        sexo = sexo.upper()
        if sexo not in ['M', 'F']:
            raise ValueError("Sexo no válido. Debe ser 'M' o 'F'.")
        return sexo

    def __validar_embarazo(self, embarazada, sexo):
        if sexo == 'M' and embarazada:
            raise ValueError(
                "Un pasajero masculino no puede estar embarazado.")
        return embarazada

    def aplicar_descuentos(self, costo_base):
        costo_final = costo_base

        if 0 <= self.edad <= 13:
            costo_final -= costo_final * 0.07

        if self.edad >= 65:
            costo_final -= costo_final * 0.05

        if self.__sexo == "F" and self.embarazada:
            costo_final -= costo_final * 0.10

        return costo_final

    def calcular_total_tiquete(self):
        costo_parcial = float(self.__costo_tiquete)
        costo_equipaje_extra = self.calcular_costo_equipaje_extra()
        costo_base = costo_parcial + costo_equipaje_extra
        costo_con_descuentos = self.aplicar_descuentos(costo_base)
        costo_final = costo_con_descuentos
        return costo_final

    @abstractmethod
    def calcular_costo_equipaje_extra(self):
        pass

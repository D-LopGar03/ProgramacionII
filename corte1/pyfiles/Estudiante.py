""" from pyfiles import Gestor_Json

import Asignatura


class Estudiante:

    DESCUENTOS = {1:0.50, 2:0.30, 3:0.20}



    def __init__(self):
        self.nom_est = ""
        self.edad = 0
        self.estrato = 0
        self.genero = ""
        self.asignaturas = []

    def registrar_estudiante(self):
        while True:
            try:
                self.nom_est = input("Ingrese el nombre del estudiante: ")
                if not self.nom_est.isalpha():
                    raise ValueError(
                        "Nombre del estudiante debe ser una cadena de texto")
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                self.edad = int(
                    input("Ingrese la edad del estudiante: "))
                if self.edad <= 11:
                    raise ValueError(
                        "El estudiante debe de tener como mínimo 12 años")
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                self.estrato = int(
                    input("Ingrese el estrato del estudiante: "))
                if self.estrato <= 0 or self.estrato > 6:
                    raise ValueError(
                        "El estrato del estudiante debe ser un número entero positivo entre 1 y 6")
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                self.genero = input("Ingrese el género del estudiante (M/F): ")
                if self.genero.lower() not in ["m", "f"]:
                    raise ValueError(
                        "El género del estudiante debe ser 'M' o 'F'")
                break
            except ValueError as e:
                print(e)

        def calcular_descuento(estrato):
            if estrato in self.DESCUENTOS:
                return self.DESCUENTOS[estrato]
            return 0



    """
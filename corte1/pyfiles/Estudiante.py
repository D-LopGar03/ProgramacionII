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
                if self.edad <= 0:
                    raise ValueError(
                        "La edad del estudiante debe ser un número entero positivo mayor de cero")
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                self.estrato = int(
                    input("Ingrese el estrato del estudiante: "))
                if self.estrato <= 0:
                    raise ValueError(
                        "El estrato del estudiante debe ser un número entero positivo mayor de cero")
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

        while True:
            asignatura = Asignatura.Asignatura()
            asignatura.registrar_asignatura()
            self.asignaturas.append(asignatura)
            continuar = input("Desea registrar otra asignatura? (s/n): ")
            if continuar.lower() != "s":
                break


   
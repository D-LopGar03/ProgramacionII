from pyfiles import Interact_Json_Asig as asignatura_json


class Asignatura:

    def __init__(self):
        self.nom_asign = ""
        self.cant_cred = 0
        self.cost_cred = 0

    def registrar_asignatura(self):
        while True:
            try:
                self.nom_asign = input("Ingrese el nombre de la asignatura: ")
                if not self.nom_asign.isalpha():
                    raise ValueError(
                        "Nombre de la asignatura debe ser una cadena de texto")

                break
            except ValueError as e:
                print(e)
        while True:
            try:
                self.cant_cred = int(
                    input("Ingrese la cantidad de créditos de la asignatura: "))
                if self.cant_cred <= 0:
                    raise ValueError(
                        "La cantidad de créditos debe ser un número entero positivo mayor de cero")
                break
            except ValueError as e:
                print(e)
        while True:
            try:
                self.cost_cred = float(
                    input("Ingrese el costo de cada crédito: "))
                if self.cost_cred <= 0:
                    raise ValueError(
                        "El costo de cada crédito debe ser un número positivo mayor de cero")
                break
            except ValueError as e:
                print(e)

        nueva_asignatura = {
            "nombre": self.nom_asign,
            "creditos": self.cant_cred,
            "costo_credito": self.cost_cred
        }

        asignaturas = asignatura_json.cargar_asignaturas()
        asignaturas.append(nueva_asignatura)
        asignatura_json.guardar_asignaturas(asignaturas)
        print("Asignatura registrada exitosamente")

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
                self.cost_cred = float(
                    input("Ingrese el costo de cada crédito: "))

                if self.cant_cred <= 0 or self.cant_cred <= 0:
                    raise ValueError(
                        "La cantidad de créditos o el costo de cada uno debe ser un número entero positivo mayor de cero")
                break
            except ValueError as e:
                print("Ingrese un dato válido para este campo")

        nueva_asignatura = {
            "nombre": self.nom_asign,
            "creditos": self.cant_cred,
            "costo_credito": self.cost_cred,
            "valor_total": self.cant_cred*self.cost_cred
        }

        asignaturas = asignatura_json.cargar_asignaturas()
        asignaturas.append(nueva_asignatura)
        asignatura_json.guardar_asignaturas(asignaturas)
        print("Asignatura registrada exitosamente")

from pyfiles.Gestor_Json import Gestor_Json
import unidecode

path_asignaturas = "JSON/asignaturas.json"


class Asignatura:

    def __init__(self):
        self.nom_asign = ""
        self.cant_cred = 0
        self.cost_cred = 0

    def normalizar_nombre(self, nombre):
        nombre = unidecode.unidecode(nombre)
        return nombre.lower()
    
    def check_asignatura(self, nombre):
        gestor_asignaturas = Gestor_Json(path_asignaturas)
        asignaturas = gestor_asignaturas.load_file()
        for asignatura in asignaturas:
            if self.normalizar_nombre(asignatura["nombre"]) == nombre:
                return True
        return False


    def registrar_asignatura(self):
        while True:
            try:
                self.nom_asign = input("Ingrese el nombre de la asignatura: ")
                self.nom_asign = self.normalizar_nombre(self.nom_asign)
                if not self.nom_asign.isalpha():
                    raise ValueError(
                        "Nombre de la asignatura debe ser una cadena de texto")
                if self.check_asignatura(self.nom_asign):
                    raise ValueError(
                        "La asignatura ya se encuentra registrada")

                break
            except ValueError as e:
                print(e)

        while True:
            try:
                self.cant_cred = int(
                    input("Ingrese la cantidad de créditos de la asignatura: "))
                self.cost_cred = float(
                    input("Ingrese el costo de cada crédito: "))

                if self.cant_cred <= 0 or self.cost_cred <= 0:
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

        gestor_asignaturas = Gestor_Json(path_asignaturas)
        asignaturas = gestor_asignaturas.load_file()
        asignaturas.append(nueva_asignatura)
        gestor_asignaturas.save_file(asignaturas)

        print("Asignatura registrada exitosamente")

        return self.nom_asign

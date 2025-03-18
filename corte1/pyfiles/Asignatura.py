from pyfiles.Gestor_Json import Gestor_Json
import unidecode

path_asignaturas = "JSON/asignaturas.json"
path_estudiantes = "JSON/estudiantes.json"


class Asignatura:

    def __init__(self):
        self.nom_asign = ""
        self.cant_cred = 0
        self.cost_cred = 0

    def normalizar_nombre(self, nombre):
        nombre = unidecode.unidecode(nombre)
        return nombre.lower()

    def generar_informe_asignaturas():
        gestor_estudiantes = Gestor_Json(path_estudiantes)
        estudiantes = gestor_estudiantes.load_file()

        conteo_asignaturas = {}

        for estudiante in estudiantes:
            if estudiante["asignatura"] not in conteo_asignaturas:
                conteo_asignaturas[estudiante["asignatura"]] = 1
            else:
                conteo_asignaturas[estudiante["asignatura"]] += 1

        print("Informe de asignaturas:")
        for asignatura, cantidad in conteo_asignaturas.items():
            print(f"{asignatura}: {cantidad}")

    def check_asignatura(self, nombre):

        gestor_asignaturas = Gestor_Json(path_asignaturas)
        asignaturas = gestor_asignaturas.load_file()
        for asignatura in asignaturas:
            if self.normalizar_nombre(asignatura["nombre"]) == nombre:
                return True
        return False

    def mayor_valor_asignatura():
        gestor_estudiantes = Gestor_Json(path_estudiantes)
        estudiantes = gestor_estudiantes.load_file()

        conteo_asignaturas = {}

        for estudiante in estudiantes:
            if estudiante["asignatura"] not in conteo_asignaturas:
                conteo_asignaturas[estudiante["asignatura"]] = 1
                conteo_asignaturas[estudiante["asignatura"]
                                   ] = estudiante["valor_pagar"]
            else:
                conteo_asignaturas[estudiante["asignatura"]
                                   ] += estudiante["valor_pagar"]

        mayor_valor = 0
        asignatura_mayor = ""
        for asignatura, cantidad in conteo_asignaturas.items():
            if cantidad > mayor_valor:
                mayor_valor = cantidad
                asignatura_mayor = asignatura
        print(
            f"La asignatura con mayor valor recaudado es {asignatura_mayor} con un total de {mayor_valor}")

    def registrar_asignatura(self):
        while True:
            try:
                self.nom_asign = input(
                    "Ingrese el nombre de la asignatura o 'Q' para regresar al menú principal: ")
                self.nom_asign = self.normalizar_nombre(self.nom_asign)

                if self.nom_asign.lower() == "q":
                    return

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

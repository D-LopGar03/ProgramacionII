from pyfiles.Gestor_Json import Gestor_Json
import unidecode
from colorama import Fore, Style

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

    def cantidad_estudiantes_asignaturas(self):
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

    def valor_promedio_cred(self):

        gestor_asignaturas = Gestor_Json(path_asignaturas)
        asignaturas = gestor_asignaturas.load_file()

        cantidad_asign = 0
        valor_credito = 0

        for asignatura in asignaturas:
            if asignatura["nombre"]:
                cantidad_asign += 1
                valor_credito += asignatura["costo_credito"]

        print(
            f"El valor promedio por crédito es: {valor_credito/cantidad_asign}")

    def descuento_estrato(self):

        while True:
            try:
                self.estrato = int(
                    input("Ingrese el estrato a consultar (1, 2 o 3): "))

                if self.estrato < 1 or self.estrato > 3:
                    raise ValueError(
                        "El rango del estrato debe de estar entre 1 y 3")

                estudiante = Gestor_Json(path_estudiantes)

                valor_total_descuento = 0

                for estrato in estudiante:

                    if estrato["estrato"] == self.estrato:

                        valor_total_descuento += estrato["valor_pagar"]
                print(
                    f"El valor total de todos los decuntos para el estrato {self.estrato} es: {valor_total_descuento}")
                break
            except ValueError as e:
                print("Ingrese un dato válido para este campo")

    def cantidad_estudiantes_estrato1(self):
        gestor_estudiantes = Gestor_Json(path_estudiantes)
        estudiantes = gestor_estudiantes.load_file()

        cantidad_estudiantes = 0

        for estudiante in estudiantes:
            if estudiante["estrato"] == 1:
                cantidad_estudiantes += 1

        print(
            f"La cantidad de estudiantes con estrato 1 es: {cantidad_estudiantes}")

    def total_ingresos(self):
        gestor_estudiantes = Gestor_Json(path_estudiantes)
        estudiantes = gestor_estudiantes.load_file()

        valor_total = 0

        for estudiante in estudiantes:
            valor_total += estudiante["valor_pagar"]
        print(f"El valor total recaudado es: {valor_total}")

    def mayor_valor_asignatura(self):
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

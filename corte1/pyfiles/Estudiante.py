from pyfiles.Gestor_Json import Gestor_Json
from pyfiles.Asignatura import Asignatura
from colorama import Fore, Style

path_estudiantes = "JSON/estudiantes.json"
path_asignaturas = "JSON/asignaturas.json"


class Estudiante:

    def __init__(self):
        self.doc = 0
        self.nom_est = ""
        self.edad = 0
        self.estrato = 0
        self.genero = ""
        self.asignaturas = ""

    def check_estudiante(self, documento):
        gestor_estudiantes = Gestor_Json(path_estudiantes)
        estudiantes = gestor_estudiantes.load_file()
        for estudiante in estudiantes:
            if estudiante["documento"] == documento:
                return True
        return False

    def aplicar_descuento(self, estrato):

        gestor_descuento = Gestor_Json(path_asignaturas)
        descuento = gestor_descuento.load_file()
        for desc in descuento:
            if estrato == 1:
                valor_pagar = desc["valor_total"] * 0.50

            elif estrato == 2:
                valor_pagar = desc["valor_total"] * 0.30

            elif estrato == 3:
                valor_pagar = desc["valor_total"] * 0.20
            else:
                valor_pagar = desc["valor_total"]
        return valor_pagar

    def registrar_estudiante(self):
        while True:
            try:
                self.doc = input("Ingrese el documento del estudiante: ")
                if not self.doc.isdigit():
                    raise ValueError(
                       Fore.RED + "Documento del estudiante debe ser un número" + Style.RESET_ALL)
                if self.check_estudiante(self.doc):
                    raise ValueError(
                        "El estudiante ya se encuentra registrado")
                break
            except ValueError as e:
                print(e)
        while True:
            try:
                self.nom_est = input("Ingrese el nombre del estudiante: ")
                if not self.nom_est.isalpha():
                    raise ValueError(
                        Fore.RED + "Nombre del estudiante debe ser una cadena de texto" + Style.RESET_ALL)
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                self.edad = int(
                    input("Ingrese la edad del estudiante: "))
                if self.edad <= 11:
                    raise ValueError(
                       Fore.RED + "El estudiante debe de tener como mínimo 12 años" + Style.RESET_ALL)
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                self.estrato = int(
                    input("Ingrese el estrato del estudiante: "))
                if self.estrato <= 0 or self.estrato > 6:
                    raise ValueError(
                       Fore.RED + "El estrato del estudiante debe ser un número entero positivo entre 1 y 6" + Style.RESET_ALL)
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                self.genero = input("Ingrese el género del estudiante (M/F): ")
                if self.genero.lower() not in ["m", "f"]:
                    raise ValueError(
                       Fore.RED + "El género del estudiante debe ser 'M' o 'F'" + Style.RESET_ALL)
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                obj_asignatura = Asignatura()
                asignatura = input("Ingrese el nombre de la asignatura: ")
                asignatura = obj_asignatura.normalizar_nombre(asignatura)
                self.asignaturas = asignatura
                if not obj_asignatura.check_asignatura(asignatura):
                    print(Fore.RED + "La asignatura no se encuentra registrada, regístrela ahora" + Style.RESET_ALL)
                    obj_asignatura.registrar_asignatura()

                break

            except ValueError as e:
                print(e)

        nuevo_estudiante = {
            "documento": self.doc,
            "nombre": self.nom_est,
            "edad": self.edad,
            "estrato": self.estrato,
            "genero": self.genero,
            "asignatura": self.asignaturas,
            "valor_pagar": self.aplicar_descuento(self.estrato)
        }

        gestor_estudiantes = Gestor_Json(path_estudiantes)
        estudiantes = gestor_estudiantes.load_file()
        estudiantes.append(nuevo_estudiante)
        gestor_estudiantes.save_file(estudiantes)
        print(Fore.GREEN + "Estudiante registrado exitosamente" + Style.RESET_ALL)

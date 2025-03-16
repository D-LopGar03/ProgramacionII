from Asignatura import Asignatura
from Estudiante import Estudiante

class Asignatura:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.estudiantes = []

    def registrar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print(f"Estudiante {estudiante.nombre} registrado en {self.nombre}")

class Estudiante:
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula

signatura = Asignatura("Programacion 2", "PRG202")
estudiante = Estudiante("Juan Perez", "20210001")

def mostrar_menu():
    print("1. Crear Asignatura")
    print("2. Registrar Estudiante en Asignatura")
    print("3. Salir")

asignaturas = {}

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre de la asignatura: ")
        codigo = input("Ingrese el código de la asignatura: ")
        asignaturas[codigo] = Asignatura(nombre, codigo)
        print(f"Asignatura {nombre} creada con éxito.")
    elif opcion == "2":
        codigo = input("Ingrese el código de la asignatura: ")
        if codigo in asignaturas:
            nombre_estudiante = input("Ingrese el nombre del estudiante: ")
            matricula = input("Ingrese la matrícula del estudiante: ")
            estudiante = Estudiante(nombre_estudiante, matricula)
            asignaturas[codigo].registrar_estudiante(estudiante)
        else:
            print("Asignatura no encontrada.")
    elif opcion == "3":
        break
    else:
        print("Opción no válida. Intente de nuevo.")
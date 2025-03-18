#!/usr/bin/env python3
from pyfiles.Asignatura import Asignatura
from pyfiles.Estudiante import Estudiante


def main():
    while True:
        print("Menú de opciones")
        print("1. Registrar asignatura")
        print("2. Registrar estudiante")
        print("3. Mostrar estudiantes por asignatura")
        print("4. Valor promedio de créditos por asignatura")
        print("5. Valor total de descuento por estrato (1, 2 o 3)")
        print("6. Cantidad de estudiantes por estrato 1")
        print("7. Cantidad de dinero recaudado en total")
        print("8. Salir")

        try:
            opcion = int(input("Ingrese la opción deseada: "))
            if opcion == 1:
                asignatura = Asignatura()
                asignatura.registrar_asignatura()
            elif opcion == 2:
                estudiante = Estudiante()
                estudiante.registrar_estudiante()
            elif opcion == 3:

                Asignatura.generar_informe_asignaturas()
            elif opcion == 4:
                pass
            elif opcion == 5:
                pass
            elif opcion == 6:
                pass
            elif opcion == 7:
                pass
            elif opcion == 8:
                break
            else:
                raise ValueError("Opción no válida")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSaliendo del programa...")
        exit()

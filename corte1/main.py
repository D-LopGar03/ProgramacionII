#!/usr/bin/env python3
from pyfiles.Asignatura import Asignatura
from pyfiles.Estudiante import Estudiante
from colorama import Fore, Style


print(Fore.GREEN + "Bienvenido al sistema de registro de estudiantes" + Style.RESET_ALL)


def main():
    asignatura = Asignatura()
    estudiante = Estudiante()

    while True:
        print("Menú de opciones")
        print("1. Registrar asignatura")
        print("2. Registrar estudiante")
        print("3. Mostrar estudiantes por asignatura")
        print("4. Valor promedio de créditos por asignatura")
        print("5. Asignatura con mayor dinero recaudado")
        print("6. Valor total de descuento por estrato (1, 2 o 3)")
        print("7. Cantidad de estudiantes por estrato 1")
        print("8. Cantidad de dinero recaudado en total")
        print("9. Salir")

        try:
            opcion = int(
                input(Fore.GREEN + "Ingrese la opción deseada: " + Style.RESET_ALL))
            if opcion == 1:

                asignatura.registrar_asignatura()
            elif opcion == 2:

                estudiante.registrar_estudiante()
            elif opcion == 3:
                asignatura = Asignatura()
                asignatura.cantidad_estudiantes_asignaturas()
            elif opcion == 4:
                asignatura = Asignatura()
                asignatura.valor_promedio_cred()
            elif opcion == 5:
                asignatura = Asignatura()
                asignatura.mayor_valor_asignatura()
            elif opcion == 6:
                asignatura = Asignatura()
                asignatura.descuento_estrato()
            elif opcion == 7:
                asignatura = Asignatura()
                asignatura.cantidad_estudiantes_estrato1()
            elif opcion == 8:
                asignatura = Asignatura()
                asignatura.total_ingresos()
            elif opcion == 9:
                break
            else:
                raise ValueError("Opción no válida")
        except ValueError:
            print(Fore.RED + "Ingrese un valor entre 1 y 9..." + Style.RESET_ALL)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSaliendo del programa...")
        exit()

#!/usr/bin/env python3

import sys
sys.dont_write_bytecode = True

from pyfiles.class_Asignatura.Asigantura import Asignatura
from pyfiles.class_Asignatura.class_Lista_Asignatura import ListaAsignatura
from pyfiles.class_Estudiante.Estudiante import Estudiante
from pyfiles.class_Estudiante.class_Lista_Estudiante import ListaEstudiante

lista_asignaturas = ListaAsignatura()
lista_estudiantes = ListaEstudiante()

def limpiar_pantalla():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def gestion_asignaturas():
    while True:
        try:
            print("1. Agregar asignatura")
            print("2. Mostrar asignaturas")
            print("3. Buscar asignatura por nombre")
            print("4. Eliminar asignatura por nombre")
            print("5. Buscar asignatura por posición")
            print("6. Eliminar asignatura por posición")
            
            print("x. Menú principal")
            print("ctrl + c. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                limpiar_pantalla()
                nombre = input("Ingrese el nombre de la asignatura: ")
                creditos = int(input("Ingrese los créditos de la asignatura: "))
                costo_credito = float(input("Ingrese el costo de los créditos: "))
                semestre = int(input("Ingrese el semestre de la asignatura: "))
                asignatura = Asignatura(nombre, creditos, costo_credito, semestre)
                lista_asignaturas.agregar(asignatura)
                limpiar_pantalla()
                print(f"Asignatura '{nombre}' agregada.")

            elif opcion == "2":

                limpiar_pantalla()
                if lista_asignaturas._head is None:
                    print("No hay asignaturas registradas.")
                    continue
                print("Lista de asignaturas:\n")
                
                lista_asignaturas.mostrar()

            elif opcion == "3":
                limpiar_pantalla()
                nombre = input("Ingrese el nombre de la asignatura a buscar: ").upper()
                resultado = lista_asignaturas.buscar_por_nombre(nombre)
                if resultado is not None:
                    print(f"Asignatura encontrada: {resultado.dato}")
                else:
                    print(f"Asignatura '{nombre}' no encontrada.")
                
            elif opcion == "4":
                nombre = input("Ingrese el nombre de la asignatura a eliminar: ").upper()

                

                if not lista_asignaturas.eliminar_asignatura_nombre(nombre):
                    limpiar_pantalla()
                    print(f"Asignatura '{nombre}' no encontrada para eliminar.")
                else:
                    limpiar_pantalla()
                    print(f"Asignatura '{nombre}' eliminada.")

            elif opcion == "5":
                limpiar_pantalla()
                posicion = int(input("Ingrese la posición de la asignatura a buscar: "))
                resultado = lista_asignaturas.buscar_por_posicion(posicion)
                if resultado is not None:
                    print(f"Asignatura en posición {posicion}: {resultado}")
                else:
                    print(f"No hay asignatura en la posición {posicion}.")


            elif opcion == "6":
                limpiar_pantalla()
                try:
                    posicion_usuario = int(input("Ingrese la posición de la asignatura a eliminar (comienza en 1): "))
                    
                    if posicion_usuario < 1:
                        print("Error: La posición debe ser mayor a 0")
                    else:
                        posicion_real = posicion_usuario - 1
                        
                        if lista_asignaturas.eliminar_asignatura_posicion(posicion_real):
                            print(f"Asignatura en posición {posicion_usuario} eliminada correctamente")
                        else:
                            print(f"No existe asignatura en la posición {posicion_usuario}")
                            
                except ValueError:
                    print("Error: Debe ingresar un número entero válido")


            elif opcion == "7":
                reporte = lista_asignaturas.contar_estudiantes_por_asignatura()
                
                if len(reporte) == 0:
                    limpiar_pantalla()
                    print("Ninguna asignatura registrada.")
                else: 
                    for asignatura, cantidad in reporte.items():
                        print(f"{asignatura}: {cantidad} estudiantes")



            elif opcion == "x":
                limpiar_pantalla()
                break
            else:
                print("Opción no válida. Intente nuevamente.")

        except KeyboardInterrupt:
            print(f"\nSaliendo del programa por interrupción del teclado...")
            sys.exit(0)
            break

        except ValueError as e:
            print(f"Error: {e}. Por favor, ingrese un valor válido.")


def gestion_estudiantes():

    while True:

        try:
            print("1. Agregar estudiante")
            print("2. Mostrar estudiantes")
            print("3. Buscar estudiante por nombre")
            print("4. Eliminar estudiante por nombre")
            print("5. Buscar estudiante por posición")
            print("6. Eliminar estudiante por posición")
            
            print("x. Menú principal")
            print("ctrl + c. Salir")

            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                limpiar_pantalla()
                nombre = input("Ingrese el nombre del estudiante: ")
                genero = input("Ingrese el género del estudiante: ").upper()
                while genero not in {'M', 'F'}:
                    print("Error: Género inválido. Debe ser 'M' o 'F'.")
                    genero = input("Ingrese el género del estudiante: ").upper()

                    
                edad = int(input("Ingrese la edad del estudiante: "))
                estrato = int(input("Ingrese el estrato del estudiante (1-6): "))
                asignatura = input("Ingrese la asignatura del estudiante: ").upper()
                                
                if lista_asignaturas.buscar_por_nombre(asignatura) is None:
                    print(f"Asignatura '{asignatura}' no encontrada. No se puede agregar el estudiante.")
                    continue
                valor_pagar = lista_asignaturas.buscar_por_nombre(asignatura).dato.total_asign

                
                
                estudiante = Estudiante(nombre, genero, edad, estrato, asignatura, valor_pagar)
                lista_estudiantes.agregar(estudiante)
                limpiar_pantalla()
                print(f"Estudiante '{nombre}' agregado.")


            elif opcion == "2":
                limpiar_pantalla()
                if lista_estudiantes._head is None:
                    print("No hay estudiantes registrados.")
                    continue
                print("Lista de estudiantes:\n")
                
                lista_estudiantes.mostrar()



            elif opcion == "x":
                limpiar_pantalla()
                break
            else:
                print("Opción no válida. Intente nuevamente.")

        except KeyboardInterrupt:
            print(f"\nSaliendo del programa por interrupción del teclado...")
            break

        except ValueError as e:
            print(f"Error: {e}. Por favor, ingrese un valor válido.")


def reportes_asignaturas():

    while True:
        
        try:

            print("1. Estudiantes por asignatura")
            print("2. Total recaudado por asignatura")

            opcion = input("Seleccione una opción: ")


            if opcion == "1":
                limpiar_pantalla()
                conteo = lista_estudiantes.contar_estudiantes_por_asignatura()
                if not conteo:
                    print("No hay estudiantes registrados.")
                else:
                    print("Estudiantes por asignatura:\n")
                    for asignatura, cantidad in conteo.items():
                        print(f"{asignatura}: {cantidad} estudiante(s)")

                
                
                
            elif opcion == "x":
                limpiar_pantalla()
                break
            else:
                print("Opción no válida. Intente nuevamente.")

        except KeyboardInterrupt:
            print(f"\nSaliendo del programa por interrupción del teclado...")
            break

        except ValueError as e:
            print(f"Error: {e}. Por favor, ingrese un valor válido.")



    

    pass

def main():
    while True:
        try:
            print("1. Gestión de Asignaturas")
            print("2. Gestión de Estudiantes")
            print("3. Reportes")
            print("ctrl + c. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                limpiar_pantalla()
                gestion_asignaturas()

            elif opcion == "2":
                limpiar_pantalla()
                gestion_estudiantes()

            elif opcion == "3":
                limpiar_pantalla()
                reportes_asignaturas()


            else:
                print("Opción no válida. Intente nuevamente.")

        except KeyboardInterrupt:
            print(f"\nSaliendo del programa por interrupción del teclado...")
            break


main()
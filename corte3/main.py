#!/usr/bin/env python3
from unidecode import unidecode
import sys
sys.dont_write_bytecode = True

from colorama import Fore, Style

from pyfiles.class_Asignatura.Asigantura import Asignatura
from pyfiles.class_Asignatura.class_Lista_Asignatura import ListaAsignatura
from pyfiles.class_Estudiante.Estudiante import Estudiante
from pyfiles.class_Estudiante.class_Lista_Estudiante import ListaEstudiante

lista_asignaturas = ListaAsignatura()
lista_estudiantes = ListaEstudiante()

def limpiar_pantalla():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def cargar_datos_iniciales():
    asignatura1 = Asignatura("Matematicas", 3, 100000.0, 1)
    asignatura2 = Asignatura("Programacion", 4, 150000.0, 2)
    asignatura3 = Asignatura("Historia", 2, 80000.0, 1)
    asignatura4 = Asignatura("Ciencias", 3, 120000.0, 2)
    asignatura5 = Asignatura("Ingles", 2, 90000.0, 1)
    lista_asignaturas.agregar(asignatura1)
    lista_asignaturas.agregar(asignatura2)
    lista_asignaturas.agregar(asignatura3)
    lista_asignaturas.agregar(asignatura4)
    lista_asignaturas.agregar(asignatura5)

    alumno1 = Estudiante("Juan Perez", "M", 20, 3, "Matemáticas", 300000.0)
    alumno2 = Estudiante("Maria Lopez", "F", 22, 1, "Programacion", 600000.0)
    alumno3 = Estudiante("Carla Benjumea", "F", 23, 2, "Historia", 80000.0)
    lista_estudiantes.agregar(alumno1)
    lista_estudiantes.agregar(alumno2)
    lista_estudiantes.agregar(alumno3)
    lista_estudiantes.mostrar()


    lista_asignaturas.intercambiar_posiciones(2, 5)
    


def gestion_asignaturas():
    
    while True:
        try:
            print("1. Agregar asignatura")
            print("2. Mostrar asignaturas")
            print("3. Buscar asignatura por nombre")
            print("4. Eliminar asignatura por nombre")
            print("5. Buscar asignatura por posición")
            print("6. Eliminar asignatura por posición")
            print("7. Intercambiar posiciones en lista (1->2, 2->1)")
            
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
                if lista_asignaturas.existe_en_lista(asignatura.nom_asign):
                    limpiar_pantalla()
                    print(Fore.RED + f"Asignatura '{nombre}' ya existe." + Style.RESET_ALL)
                    continue
                lista_asignaturas.agregar(asignatura)
                limpiar_pantalla()
                print(Fore.GREEN + f"Asignatura '{nombre}' agregada." + Style.RESET_ALL)

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
                nombre = unidecode(nombre).upper()
                nombre = nombre.replace('1', 'I').replace('2', 'II').replace('3', 'III') \
                               .replace('4', 'IV').replace('5', 'V')
                resultado = lista_asignaturas.buscar_por_nombre(nombre)
                if resultado is not None:
                    print(Fore.GREEN + f"Asignatura encontrada: {resultado.dato}" + Style.RESET_ALL)
                else:
                    print(Fore.RED + f"Asignatura '{nombre}' no encontrada." + Style.RESET_ALL)
                
            elif opcion == "4":
                nombre = input("Ingrese el nombre de la asignatura a eliminar: ").upper()

                

                if not lista_asignaturas.eliminar_asignatura_nombre(nombre):
                    limpiar_pantalla()
                    print(Fore.RED + f"Asignatura '{nombre}' no encontrada para eliminar." + Style.RESET_ALL)
                else:
                    limpiar_pantalla()
                    print(Fore.GREEN + f"Asignatura '{nombre}' eliminada." + Style.RESET_ALL)

            elif opcion == "5":
                limpiar_pantalla()
                posicion = int(input("Ingrese la posición de la asignatura a buscar: "))
                resultado = lista_asignaturas.buscar_por_posicion(posicion)
                if resultado is not None:
                    print(Fore.GREEN + f"Asignatura en posición {posicion}: {resultado}" + Style.RESET_ALL)
                else:
                    print(Fore.RED + f"No hay asignatura en la posición {posicion}." + Style.RESET_ALL)


            elif opcion == "6":
                limpiar_pantalla()
                try:
                    posicion_usuario = int(input("Ingrese la posición de la asignatura a eliminar (comienza en 1): "))
                    
                    if posicion_usuario < 1:
                        print(Fore.RED + "Error: La posición debe ser mayor a 0" + Style.RESET_ALL)
                    else:
                        posicion_real = posicion_usuario - 1
                        
                        if lista_asignaturas.eliminar_por_posicion(posicion_real):
                            print(Fore.GREEN + f"Asignatura en posición {posicion_usuario} eliminada correctamente" + Style.RESET_ALL)
                        else:
                            print(Fore.RED + f"No existe asignatura en la posición {posicion_usuario}" + Style.RESET_ALL)
                            
                except ValueError:
                    print(Fore.RED + "Error: Debe ingresar un número entero válido" + Style.RESET_ALL)


            elif opcion == "7":
                
                while True:
                    try: 
                        posicion1 = int(input("Ingrese la primera posición a intercambiar: "))
                        posicion2 = int(input("Ingrese la segunda posición a intercambiar: "))
                        
                        if posicion1 < 0 or posicion2 < 0:
                            print(Fore.RED + "Error: Las posiciones deben ser mayores a 0" + Style.RESET_ALL)
                            continue
                        if posicion1 == posicion2:
                            print(Fore.RED + "Error: Las posiciones no pueden ser iguales" + Style.RESET_ALL)
                            continue

                        if lista_asignaturas.intercambiar_posiciones(posicion1, posicion2):
                            limpiar_pantalla()
                            print(Fore.GREEN + f"Asignaturas en posiciones {posicion1} y {posicion2} intercambiadas correctamente" + Style.RESET_ALL)
                            break
                        else:
                            print(Fore.RED + f"No existe asignatura en la posición {posicion1} o {posicion2}" + Style.RESET_ALL)
                        break
                    except ValueError:
                        limpiar_pantalla()
                        print(Fore.RED + "Error: Debe ingresar un número entero válido" + Style.RESET_ALL)




            elif opcion == "x":
                limpiar_pantalla()
                break
            else:
                print(Fore.RED + "Opción no válida. Intente nuevamente." + Style.RESET_ALL)

        except KeyboardInterrupt:
            print(Fore.YELLOW + f"\nSaliendo del programa por interrupción del teclado..." + Style.RESET_ALL)
            sys.exit(0)
            break

        except ValueError as e:
            print(Fore.RED + f"Error: {e}. Por favor, ingrese un valor válido." + Style.RESET_ALL)


def gestion_estudiantes():

    while True:

        try:
            print("1. Agregar estudiante")
            print("2. Mostrar estudiantes")
            print("3. Buscar estudiante por nombre")
            print("4. Eliminar estudiante por nombre")
            print("5. Buscar estudiante por posición")
            print("6. Eliminar estudiante por posición")
            print("7. Intercambiar posiciones en lista (1->2, 2->1)")
            print("8. Mover de posición inicial a final")
            
            print("x. Menú principal")
            print("ctrl + c. Salir")

            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                limpiar_pantalla()
                nombre = input("Ingrese el nombre del estudiante: ").title()
                genero = input("Ingrese el género del estudiante: ").upper()
                while genero not in {'M', 'F'}:
                    print(Fore.RED + "Error: Género inválido. Debe ser 'M' o 'F'." + Style.RESET_ALL)
                    genero = input("Ingrese el género del estudiante: ").upper()

                    
                edad = int(input("Ingrese la edad del estudiante: "))
                while edad < 13 or edad > 120:
                    print(Fore.RED + "Error: El estudiante debe de tener como mínimo 13 años." + Style.RESET_ALL)
                    edad = int(input("Ingrese la edad del estudiante: "))

                estrato = int(input("Ingrese el estrato del estudiante (1-6): "))
                asignatura = input("Ingrese la asignatura del estudiante: ")
                asignatura = unidecode(asignatura).upper()
                asignatura = asignatura.replace('1', 'I').replace('2', 'II').replace('3', 'III') \
                                       .replace('4', 'IV').replace('5', 'V')
                
                                
                if lista_asignaturas.buscar_por_nombre(asignatura) is None:
                    limpiar_pantalla()
                    print(Fore.RED + f"Asignatura '{asignatura}' no encontrada. No se puede agregar el estudiante." + Style.RESET_ALL)
                    continue
                valor_pagar = lista_asignaturas.buscar_por_nombre(asignatura).dato.total_asign

                
                
                estudiante = Estudiante(nombre, genero, edad, estrato, asignatura, valor_pagar)
                lista_estudiantes.agregar(estudiante)
                limpiar_pantalla()
                print(Fore.GREEN + f"Estudiante '{nombre}' agregado." + Style.RESET_ALL)


            elif opcion == "2":
                limpiar_pantalla()
                if lista_estudiantes._head is None:
                    print(Fore.RED + "No hay estudiantes registrados." + Style.RESET_ALL)
                    continue
                print("Lista de estudiantes:\n")
                
                lista_estudiantes.mostrar()


            elif opcion == "3":

                limpiar_pantalla()
                nombre = input("Ingrese el nombre del estudiante a buscar: ").title()
                resultado = lista_estudiantes.buscar_por_nombre(nombre)
                if resultado is not None:
                    print(Fore.GREEN + f"Estudiante encontrado:\n {resultado.dato}" + Style.RESET_ALL)
                else:
                    print(Fore.RED + f"Estudiante '{nombre}' no encontrado." + Style.RESET_ALL)

            elif opcion == "4":
                limpiar_pantalla()
                nombre = input("Ingrese el nombre del estudiante a eliminar: ").title()
                if not lista_estudiantes.eliminar_estudiante_nombre(nombre):
                    print(Fore.RED + f"Estudiante '{nombre}' no encontrado para eliminar." + Style.RESET_ALL)
                else:
                    limpiar_pantalla()
                    print(Fore.GREEN + f"Estudiante '{nombre}' eliminado." + Style.RESET_ALL)
            elif opcion == "5":
                limpiar_pantalla()
               
                posicion = int(input("Ingrese la posición del estudiante a buscar: "))
                resultado = lista_estudiantes.buscar_por_posicion(posicion)
                if resultado is not None:
                    print(Fore.GREEN + f"Estudiante en posición {posicion}: {resultado}" + Style.RESET_ALL)
                else:
                    print(Fore.RED + f"No hay estudiante en la posición {posicion}." + Style.RESET_ALL)

            elif opcion == "6":

                limpiar_pantalla()
                try:
                    posicion_usuario = int(input("Ingrese la posición del estudiante a eliminar (comienza en 1): "))
                    
                    if posicion_usuario < 1:
                        print(Fore.RED + "Error: La posición debe ser mayor a 0" + Style.RESET_ALL)
                    else:
                        posicion_real = posicion_usuario - 1
                        
                        if lista_estudiantes.eliminar_por_posicion(posicion_real):
                            print(Fore.GREEN + f"Asignatura en posición {posicion_usuario} eliminada correctamente" + Style.RESET_ALL)
                        else:
                            print(Fore.RED + f"No existe asignatura en la posición {posicion_usuario}" + Style.RESET_ALL)
                            
                except ValueError:
                    print(Fore.RED + "Error: Debe ingresar un número entero válido" + Style.RESET_ALL)

            elif opcion == "7":
                while True:
                    try: 
                        posicion1 = int(input("Ingrese la primera posición a intercambiar: "))
                        posicion2 = int(input("Ingrese la segunda posición a intercambiar: "))
                        
                        if posicion1 < 0 or posicion2 < 0:
                            print(Fore.RED + "Error: Las posiciones deben ser mayores a 0" + Style.RESET_ALL)
                            continue
                        if posicion1 == posicion2:
                            print(Fore.RED + "Error: Las posiciones no pueden ser iguales" + Style.RESET_ALL)
                            continue

                        if lista_asignaturas.intercambiar_posiciones(posicion1, posicion2):
                            limpiar_pantalla()
                            print(Fore.GREEN + f"Asignaturas en posiciones {posicion1} y {posicion2} intercambiadas correctamente" + Style.RESET_ALL)
                            break
                        else:
                            print(Fore.RED + f"No existe asignatura en la posición {posicion1} o {posicion2}" + Style.RESET_ALL)
                        break
                    except ValueError:
                        limpiar_pantalla()
                        print(Fore.RED + "Error: Debe ingresar un número entero válido" + Style.RESET_ALL)


            elif opcion == "8":
                limpiar_pantalla()
                posicion1 = 1
                posicion2 = lista_estudiantes.contar_nodos()

                if lista_estudiantes.posicion_inicial_final(posicion1, posicion2):
                    print(Fore.GREEN + f"Estudiante en posición {posicion1} movido a la posición {posicion2}." + Style.RESET_ALL)
                else:
                    print(Fore.RED + f"No existe estudiante en la posición {posicion1}." + Style.RESET_ALL)
                lista_estudiantes.mostrar()

            elif opcion == "x":
                limpiar_pantalla()
                break
            else:
                print(Fore.RED + "Opción no válida. Intente nuevamente." + Style.RESET_ALL)

        except KeyboardInterrupt:
            print(Fore.YELLOW + f"\nSaliendo del programa por interrupción del teclado..." + Style.RESET_ALL)
            limpiar_pantalla()
            sys.exit(0)
            

        except ValueError as e:
            print(Fore.RED + f"Error: Por favor, ingrese un valor válido." + Style.RESET_ALL)


def reportes_asignaturas():

    while True:
        
        try:

            print("1. Estudiantes por asignatura")
            print("2. Total recaudado por asignatura")
            print("3. Asignatura con mayor recaudo")
            print("4. Promedio de costos por asignatura")
            print("5. Total recaudado por estrato (1, 2 o 3)")
            print("6. Total recaudado entre todas las asignaturas")
            print("7. Cuantos estudiantes hay de estrato 1 por asignatura")
            print("8. Cantidad de asignaturas inscritas")
            print("x. Menú principal")

            opcion = input("Seleccione una opción: ")


            if opcion == "1":
                limpiar_pantalla()
                conteo = lista_estudiantes.contar_estudiantes_por_asignatura()
                if not conteo:
                    print(Fore.RED + "No hay estudiantes registrados." + Style.RESET_ALL)
                else:
                    print(Fore.GREEN + "Estudiantes por asignatura:\n" + Style.RESET_ALL)
                    for asignatura, cantidad in conteo.items():
                        print(Fore.YELLOW + f"{asignatura}: {cantidad} estudiante(s)" + Style.RESET_ALL)



            elif opcion == "2":
                limpiar_pantalla()
                conteo = lista_estudiantes.recaudo_por_asignatura()
                if not conteo:
                    print(Fore.RED + "No hay asignaturas registrados." + Style.RESET_ALL)
                else:
                    print(Fore.GREEN + "Recaudo total por asignatura:\n" + Style.RESET_ALL)
                    for asignatura, precio in conteo.items():
                        print(Fore.YELLOW + f"{asignatura}: ${precio}" + Style.RESET_ALL)


            elif opcion == "3":
                limpiar_pantalla()
                asignatura_mayor, recaudo = lista_asignaturas.asignatura_mayor_recaudo(lista_estudiantes)
                if asignatura_mayor is not None:
                    print(Fore.GREEN + f"Asignatura con mayor recaudo: {asignatura_mayor} con ${recaudo}" + Style.RESET_ALL)
                else:
                    print(Fore.RED + "No hay estudiantes registrados." + Style.RESET_ALL)
            elif opcion == "4":

                limpiar_pantalla()
                promedio = lista_asignaturas.promedio_costo_asignatura()
                if promedio > 0:
                    print(Fore.GREEN + f"Promedio de costos por asignatura: ${promedio:.2f}\n + " + Style.RESET_ALL)
                else:
                    print(Fore.RED + "No hay asignaturas registradas." + Style.RESET_ALL)
                
            elif opcion == "5":
                limpiar_pantalla()
                estrato = int(input("Ingrese el estrato (1-3) para calcular el total recaudado: "))
                if estrato not in [1, 2, 3]:
                    print(Fore.RED + "Error: El estrato debe ser 1, 2 o 3." + Style.RESET_ALL)
                    continue
                total_recaudado = lista_estudiantes.total_recaudado_por_estrato(estrato)
                print(Fore.GREEN + f"Total recaudado por estudiantes de estrato {estrato}: ${total_recaudado:.2f}" + Style.RESET_ALL)
                

            elif opcion == "6":
                limpiar_pantalla()
                total_recaudado = lista_estudiantes.recaudo_total()
                if total_recaudado > 0:
                    print(Fore.GREEN + f"Total recaudado entre todas las asignaturas: ${total_recaudado:.2f}" + Style.RESET_ALL)
                else:
                    print(Fore.RED + "No hay estudiantes registrados." + Style.RESET_ALL)


            elif opcion == "7":
                limpiar_pantalla()
                conteo = lista_estudiantes.contar_estrato_uno_por_asignatura()
                if not conteo:
                    print(Fore.RED + "No hay estudiantes de estrato 1 registrados." + Style.RESET_ALL)
                else:
                    print(Fore.GREEN + "Cantidad de estudiantes de estrato 1 por asignatura:\n" + Style.RESET_ALL)
                    for asignatura, cantidad in conteo.items():
                        print(Fore.YELLOW + f"  {asignatura}: {cantidad}\n" + Style.RESET_ALL)
                  



            elif opcion == "8":
                limpiar_pantalla()
                cantidad_asignaturas = lista_asignaturas.contar_nodos()

                if not cantidad_asignaturas:
                    print(Fore.RED + "No hay asignaturas inscritas." + Style.RESET_ALL)
                else:
                    print(Fore.GREEN + f"Cantidad de asignaturas inscritas: {cantidad_asignaturas}" + Style.RESET_ALL)

            elif opcion == "x":
                limpiar_pantalla()
                break
            else:
                print(Fore.RED + "Opción no válida. Intente nuevamente." + Style.RESET_ALL)

        except KeyboardInterrupt:
            print(Fore.YELLOW + f"\nSaliendo del programa por interrupción del teclado..." + Style.RESET_ALL)
            limpiar_pantalla()
            sys.exit(0)

        except ValueError as e:
            print(Fore.RED + f"Error: Por favor, ingrese un valor válido." + Style.RESET_ALL)


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
                limpiar_pantalla()
                print(Fore.RED + "Opción no válida. Intente nuevamente." + Style.RESET_ALL) 

        except KeyboardInterrupt:
            print(Fore.YELLOW + f"\nSaliendo del programa por interrupción del teclado..." + Style.RESET_ALL)
            limpiar_pantalla()
            sys.exit(0)

        except ValueError as e:
            limpiar_pantalla()
            print(Fore.RED + f"Error: Por favor, ingrese un valor válido." + Style.RESET_ALL)

cargar_datos_iniciales()
main()
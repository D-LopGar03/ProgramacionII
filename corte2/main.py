#!/usr/bin/env python3
from tiquete.class_tiquete import Tiquete
from tiquete.class_TiqueteEconomico import TiqueteEconomico
from tiquete.class_TiqueteEjecutivo import TiqueteEjecutivo
from tiquete.class_TiquetePremium import TiquetePremium
from pasajeros.class_pasajero import Pasajero
from ciudad.class_ciudad import Ciudad
from cargas_especiales.tipos_cargas import TIPOS_CARGA
from vuelo.class_vuelo import Vuelo
from cargas_especiales.class_bicicleta import Bicicleta
from cargas_especiales.class_perro import Perro
from cargas_especiales.class_gato import Gato
from cargas_especiales.class_otro import Otro


from datetime import datetime
import random
import string
import geonamescache
from unidecode import unidecode
gc = geonamescache.GeonamesCache()


vuelos = []
tiquetes = []
pasajeros = []


def validar_fecha_hora():
    while True:
        fecha_str = input("Ingrese la fecha de vuelo (DD/MM/AAAA): ")
        hora_str = input("Ingrese la hora de salida (HH:MM en formato 24h): ")
        try:
            fecha_hora_str = f"{fecha_str} {hora_str}"
            fecha_hora = datetime.strptime(fecha_hora_str, "%d-%m-%Y %H:%M")
            
            if fecha_hora < datetime.now():
                print("La fecha y hora no pueden ser anteriores a la actual.")
            else:
                return fecha_hora
        except ValueError:
            print("Fecha u hora inválida. Intente de nuevo.")
            
    

def obtener_pais_ciudad(mensaje):
    while True:
        nombre_ciudad = input(mensaje).lower().strip()
        ciudad_input = unidecode(nombre_ciudad)
        ciudades_mundo = gc.get_cities()
        paises = gc.get_countries()

        for ciudad in ciudades_mundo.values():
            if unidecode(ciudad['name'].lower()) == ciudad_input:
                return (ciudad_input, paises[ciudad['countrycode']]['name'])
        print("Ciudad no encontrada. Intente nuevamente.")

def generar_codigo_unico():
    generados = set()
    while True:
        codigo = f"{''.join(random.choices(string.ascii_uppercase, k=3))}-{random.randint(1, 999):03d}"
        if codigo not in generados:
            generados.add(codigo)
            return codigo

def verificar_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                raise ValueError
            return valor
        except ValueError:
            print("Por favor, ingrese un número entero positivo.")

def verificar_decimal(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                raise ValueError
            return valor
        except ValueError:
            print("Por favor, ingrese un número decimal positivo.")

def verificar_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Por favor, ingrese un texto válido.")

def crear_pasajero():
    identificacion = verificar_entero("Ingrese la identificación del pasajero: ")
    nombre = verificar_texto("Ingrese el nombre del pasajero: ")
    edad = verificar_entero("Ingrese la edad del pasajero: ")
    sexo = verificar_texto("Ingrese el sexo del pasajero (M/F): ").upper()
    while sexo not in ['M', 'F']:
        sexo = verificar_texto("Ingrese el sexo del pasajero (M/F): ").upper()

    embarazada = False
    if sexo == "F":
        embarazada = input("¿Está embarazada? (S/N): ").upper()
        while embarazada not in ['S', 'N']:
            embarazada = input("¿Está embarazada? (S/N): ").upper()
        embarazada = embarazada == "S"

    pasajero = Pasajero(identificacion, nombre, edad, sexo, embarazada)
    pasajeros.append(pasajero)
    print(f"Pasajero creado: {pasajero}")

def crear_vuelo():
    if len(tiquetes) == 0:
        print("Debe vender al menos un tiquete antes de crear un vuelo.")
        return

    codigo_vuelo = generar_codigo_unico()
    origen = Ciudad(*obtener_pais_ciudad("Ingrese la ciudad de origen: "))
    destino = Ciudad(*obtener_pais_ciudad("Ingrese la ciudad de destino: "))

    if origen.nombre == destino.nombre:
        print("La ciudad de origen y destino no pueden ser la misma.")
        return

    fecha = validar_fecha_hora()
    vuelo = Vuelo(origen, destino, fecha, codigo_vuelo, tiquetes)
    vuelos.append(vuelo)
    print(f"Vuelo creado: {vuelo}")

def vender_tiquete():
    TARIFAS = {"E": 100000, "EJ": 200000, "P": 300000}
    if not pasajeros:
        print("Debe crear al menos un pasajero.")
        return

    print("\nPasajeros disponibles:")
    for i, p in enumerate(pasajeros, 1):
        print(f"{i}. {p.nombre} (ID: {p.identificacion})")

    try:
        seleccion = int(input("Seleccione un pasajero: ")) - 1
        pasajero = pasajeros[seleccion]
    except (ValueError, IndexError):
        print("Selección inválida.")
        return

    print("\nTipos de tiquete:")
    print("1. Tiquete Económico")
    print("2. Tiquete Ejecutivo")
    print("3. Tiquete Premium")

    tipo = input("Seleccione el tipo de tiquete (1/2/3): ")
    while tipo not in ['1', '2', '3']:
        tipo = input("Seleccione el tipo de tiquete (1/2/3): ")

    if tipo == '1':
        tiquete = TiqueteEconomico(pasajero, TARIFAS["E"], 0)
    elif tipo == '2':
        tiquete = TiqueteEjecutivo(pasajero, TARIFAS["EJ"], 0)
    else:
        tiquete = TiquetePremium(pasajero, TARIFAS["P"], 0)

    tiquetes.append(tiquete)
    print("Tiquete vendido con éxito.")

def realizar_checkin():
    if not tiquetes:
        print("No hay tiquetes vendidos.")
        return

    print("\nTiquetes vendidos:")
    for i, tiquete in enumerate(tiquetes, 1):
        print(f"{i}. {tiquete}")

    try:
        tiquete_idx = int(input("Seleccione tiquete (número): ")) - 1
        tiquete = tiquetes[tiquete_idx]
    except (ValueError, IndexError):
        print("Selección no válida.")
        return

    equipajes = []
    while True:
        print("\nTipos de equipaje:")
        print("1. Equipaje normal (verificar exceso)")
        print("2. Bicicleta")
        print("3. Mascota")
        print("4. Finalizar check-in")

        opcion = input("Seleccione tipo de equipaje (1-4): ")
        if opcion == "4":
            break

        try:
            peso = float(input("Peso del equipaje (kg): "))
            if peso <= 0 or peso > 100:
                print("Peso inválido (debe ser entre 0 y 100 kg).")
                continue
        except ValueError:
            print("Peso inválido.")
            continue

        if opcion == "1":
            equipajes.append((peso, 0))  # normal
        elif opcion == "2":
            try:
                
                equipajes.append(Bicicleta(peso))
            except ValueError:
                print("Costo inválido.")
        elif opcion == "3":
            print("Tipo de mascota:\n1. Perro\n2. Gato")
            mascota = input("Seleccione (1 o 2): ")
            if mascota == "1":
                equipajes.append(Perro(peso))
            elif mascota == "2":
                equipajes.append(Gato(peso))
            else:
                print("Mascota no válida.")
        else:
            print("Opción inválida.")

    if equipajes:
        for carga in equipajes:
            tiquete.agregar_carga_especial(carga)
        print(f"Check-in completado para {tiquete.pasajero.nombre}")
        print(f"Nuevo total a pagar: ${tiquete.calcular_total():,.2f}")
    else:
        print("No se agregó ningún equipaje.")

def main():
    while True:
        print("\nOpciones:")
        print("1. Crear pasajero")
        print("2. Listar pasajeros")
        print("3. Crear vuelo")
        print("4. Vender tiquete")
        print("5. Realizar check-in")
        print("x. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            crear_pasajero()
        elif opcion == '2':
            if pasajeros:
                for p in pasajeros:
                    print(p)
            else:
                print("No hay pasajeros.")
        elif opcion == '3':
            crear_vuelo()
        elif opcion == '4':
            vender_tiquete()
        elif opcion == '5':
            realizar_checkin()
        elif opcion == 'x':
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

main()
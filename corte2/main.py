#!/usr/bin/env python3
from tiquete.class_tiquete import Tiquete
from tiquete.class_TiqueteEconomico import TiqueteEconomico
from tiquete.class_TiqueteEjecutivo import TiqueteEjecutivo
from tiquete.class_TiquetePremium import TiquetePremium
from pasajeros.class_pasajero import Pasajero
from ciudad.class_ciudad import Ciudad
from cargas_especiales.tipos_cargas import TIPOS_CARGA
from vuelo.class_vuelo import Vuelo

import random
import string
import geonamescache
from unidecode import unidecode
gc = geonamescache.GeonamesCache()


vuelos = []
tiquetes = []
pasajeros = []

def obtener_pais_ciudad(mensaje):

    while True:
        nombre_ciudad = input(mensaje).lower().strip()
        ciudad_input = unidecode(nombre_ciudad.strip().lower())

        ciudades_mundo = gc.get_cities()
        paises = gc.get_countries()

        for ciudad in ciudades_mundo.values():
            ciudad_nombre = unidecode(ciudad['name'].lower())
            if ciudad_nombre == ciudad_input:
                codigo_pais = ciudad['countrycode']
                return (ciudad_input, paises[codigo_pais]['name'])
        print("Ciudad no encontrada. Intente nuevamente.")

def generar_codigo_unico():
    generados = set()
    while True:
        letras = ''.join(random.choices(string.ascii_uppercase, k=3))
        numero = random.randint(1, 999)
        codigo = f"{letras}-{numero:03d}"
        if codigo not in generados:
            generados.add(codigo)
            return codigo

def crear_vuelo():
    codigo_vuelo = generar_codigo_unico()
    origen = obtener_pais_ciudad("Ingrese la ciudad de origen: ")
    origen = Ciudad(origen[0], origen[1])
   
    destino = obtener_pais_ciudad("Ingrese la ciudad de destino: ")
    destino = Ciudad(destino[0], destino[1])
    if origen.nombre == destino.nombre:
        print("La ciudad de origen y destino no pueden ser la misma.")
        return
    fecha = input("Ingrese la fecha del vuelo (DD/MM/AAAA): ")

    vuelo = Vuelo(origen, destino, fecha, codigo_vuelo, tiquetes)
    vuelos.append(vuelo)
    print(f"Vuelo creado: {vuelo}")

def crear_tiquete():

    if len(pasajeros) == 0:
        print("Debe de crear al menos un pasajero.")
        return

    print("Seleccione el tipo de tiquete:")
    print("1. Tiquete Económico")
    print("2. Tiquete Ejecutivo")
    print("3. Tiquete Premium")
    tipo_tiquete = input("Seleccione una opción: ")

    if tipo_tiquete not in ['1', '2', '3']:
        print("Opción no válida.")
        return

    pasajero = pasajeros[0]  # Asignar el primer pasajero por simplicidad
    costo_base = float(input("Ingrese el costo base del tiquete: "))
    kilos_equipaje = float(input("Ingrese los kilos de equipaje: "))

    if tipo_tiquete == '1':
        tiquete = TiqueteEconomico(pasajero, costo_base, kilos_equipaje)
    elif tipo_tiquete == '2':
        tiquete = TiqueteEjecutivo(pasajero, costo_base, kilos_equipaje)
    else:
        tiquete = TiquetePremium(pasajero, costo_base, kilos_equipaje)

    tiquetes.append(tiquete)
    print(f"Tiquete creado: {tiquete}")

def main():
    while True:
        print("\nOpciones:")
        print("1. Crear vuelo")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':

            if len(tiquetes) == 0:
                print("Debe de vender al menos un tiquete.")
                

            crear_vuelo()
        elif opcion == '2':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()


    
#!/usr/bin/env python3
from pasajeros.class_pasajero_economico import Pasajero_Economico
from pasajeros.class_pasajero_ejecutivo import Pasajero_Ejecutivo
from pasajeros.class_pasajero_premium import Pasajero_Premium


def crear_pasajero():

    tarifas = {
        "economico": 150000,
        "ejecutivo": 250000,
        "premium": 500000
    }

    def pedir_pasajero(mensaje):
        TIPO_PASAJERO = ["economico", "ejecutivo", "premium"]
        while True:
            tipo = input(mensaje).strip().lower()

            if tipo not in TIPO_PASAJERO:
                print("Ingrese un tipo de pasajero válido.")
            else:
                return tipo

    def pedir_entero(mensaje, minimo=None, maximo=None):
        while True:
            try:
                valor = int(input(mensaje))
                if (minimo is not None and valor < minimo) or (maximo is not None and valor > maximo):
                    print(f"El valor debe estar entre {minimo} y {maximo}.")
                    continue
                return valor
            except ValueError:
                print("Ingrese un número válido.")

    def pedir_texto(mensaje):
        while True:
            texto = input(mensaje).strip().title()
            if texto:
                return texto
            else:
                print("El campo no puede estar vacío.")

    def pedir_float(mensaje, minimo=None, maximo=None):
        while True:
            try:
                valor = float(input(mensaje))
                if (minimo is not None and valor < minimo) or (maximo is not None and valor > maximo):
                    print(f"El valor debe estar entre {minimo} y {maximo}.")
                    continue
                return valor
            except ValueError:
                print("Ingrese un número válido.")

    def pedir_sexo(mensaje):
        while True:
            sexo = input(mensaje).strip().upper()
            if sexo in ["M", "F"]:
                return sexo
            print("Sexo no válido. Ingrese 'M' o 'F'.")

    def pedir_embarazo(mensaje, sexo):
        sexo = sexo.upper()

        if sexo == "M":
            return False
        while True:
            respuesta = input(mensaje).strip().lower()
            if respuesta in ["s"]:
                return True
            elif respuesta in ["n"]:
                return False
            print("Responda 'S' o 'N'.")

    tipo = pedir_pasajero(
        "Ingrese el tipo de pasajero 'economico', 'ejecutivo', 'premium': ")
    identificacion = pedir_entero(
        "Ingrese el número de identificación del pasajero: ", 1)
    nombre = pedir_texto("Ingrese el nombre del pasajero: ")
    edad = pedir_entero("Ingrese la edad del pasajero: ", 0, 130)
    kilo_equipaje = pedir_float(
        "Ingrese los kilos del equipaje en KG: ", 0, 70)
    costo_tiquete = tarifas[tipo]
    sexo = pedir_sexo("Ingrese el sexo del pasajero: ")

    if sexo == "F":
        embarazo = pedir_embarazo(
            "¿La pasajera está embarazada? (S/N): ", sexo)
    else:
        embarazo = False

    if tipo == "economico":
        pasajero = Pasajero_Economico(
            identificacion, nombre, edad, kilo_equipaje, costo_tiquete, sexo, embarazo)
    elif tipo == "ejecutivo":
        pasajero = Pasajero_Ejecutivo(
            identificacion, nombre, edad, kilo_equipaje, costo_tiquete, sexo, embarazo)
    else:  
        pasajero = Pasajero_Premium(
            identificacion, nombre, edad, kilo_equipaje, costo_tiquete, sexo, embarazo)

    print(
        f"El valor total a pagar es de: ${pasajero.calcular_total_tiquete()}")


crear_pasajero()

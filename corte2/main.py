#!/usr/bin/env python3
from tiquete.class_tiquete import Tiquete
from tiquete.class_TiqueteEconomico import TiqueteEconomico
from tiquete.class_TiqueteEjecutivo import TiqueteEjecutivo
from tiquete.class_TiquetePremium import TiquetePremium
from pasajeros.class_pasajero import Pasajero


def crear_pasajero():

    tarifas = {
        "economico": (150000, TiqueteEconomico),
        "ejecutivo": (250000, TiqueteEjecutivo),
        "premium": (500000, TiquetePremium)
    }

    def pedir_tiquete(mensaje):
        TIPO_TIQUETE = ["economico", "ejecutivo", "premium"]
        while True:
            tipo = input(mensaje).strip().lower()

            if tipo not in TIPO_TIQUETE:
                print("Ingrese un tipo de tiquete válido.")
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

    tipo = pedir_tiquete(
        "Ingrese el tipo de tiquete 'economico', 'ejecutivo', 'premium': ")
    identificacion = pedir_texto(
        "Ingrese el número de identificación del pasajero: ")
    nombre = pedir_texto("Ingrese el nombre del pasajero: ")
    edad = pedir_entero("Ingrese la edad del pasajero: ", 0, 130)
    kilo_equipaje = pedir_float(
        "Ingrese los kilos del equipaje en KG: ", 0, 70)
    costo_tiquete = tarifas[tipo][0]
    print(f"El costo del tiquete es: ${costo_tiquete}")
    sexo = pedir_sexo("Ingrese el sexo del pasajero: ")

    if sexo == "F":
        embarazo = pedir_embarazo(
            "¿La pasajera está embarazada? (S/N): ", sexo)
    else:
        embarazo = False

    precio, clase_tiquete = tarifas[tipo]
    pasajero = Pasajero(
        identificacion=identificacion,
        nombre=nombre,
        edad=edad,
        sexo=sexo,
        embarazada=embarazo
    )

    tiquete = clase_tiquete(pasajero, precio, kilo_equipaje)
    tiquete.embarazada = embarazo
    

    print(
        f"El valor total a pagar es de: ${tiquete.calcular_total()}")


crear_pasajero()

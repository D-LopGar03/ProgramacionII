#!/usr/bin/env python3

from pyfiles.Asignatura import Asignatura

while True:

    asignatura = Asignatura()
    asignatura.registrar_asignatura()

    continuar = input("Desea registrar otra asignatura? (s/n): ")
    if continuar.lower() != "s":
        break
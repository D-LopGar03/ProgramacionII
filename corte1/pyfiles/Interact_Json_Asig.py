import json

path_asignaturas = "JSON/asignaturas.json"


def cargar_asignaturas():
    with open(path_asignaturas, "r") as file:
        return json.load(file)


def guardar_asignaturas(asignaturas):
    with open(path_asignaturas, "w") as file:
        json.dump(asignaturas, file, indent=4, ensure_ascii=False)

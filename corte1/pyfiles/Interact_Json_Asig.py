import json

path_asignaturas = "JSON/asignaturas.json"


def cargar_asignaturas():
     try:
        with open(path_asignaturas, "r", encoding="utf-8") as file:
            return json.load(file)
     except json.JSONDecodeError:
        print(f"Error: El archivo {path_asignaturas} está malformado. Se inicializará con una lista vacía.")
        return []


def guardar_asignaturas(asignaturas):
    with open(path_asignaturas, "w") as file:
        json.dump(asignaturas, file, indent=4, ensure_ascii=False)



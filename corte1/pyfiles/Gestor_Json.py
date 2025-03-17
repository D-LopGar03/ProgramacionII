import json

class Gestor_Json:

    def __init__(self, path_file):
        self.path_file = path_file

    def load_file(self):
        try:
            with open(self.path_file, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            print(f"Error: El archivo {self.path_file} está malformado o no existe. Se inicializará con una lista vacía.")
            return []

    def save_file(self, data):
        with open(self.path_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    

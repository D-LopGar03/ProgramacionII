class Asignatura:

    def __init__(self, nom_asign, cant_cred, cost_cred):
        if not nom_asign.isalpha():
            raise ValueError("Nombre de asignatura debe ser una cadena de texto")
        if cant_cred < 1:
            raise ValueError("Cantidad de creditos debe ser un numero entero positivo")
        if cost_cred < 1:
            raise ValueError("Costo de creditos debe ser un numero entero positivo")


        self.nom_asign = str(nom_asign)
        self.cant_cred = int(cant_cred)
        self.cost_cred = int(cost_cred)

    

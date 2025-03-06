def pedir_valor():
    return ""


class Asignature:

    def __init__(self, nom_asign, cant_cred, cost_cred):
        if not nom_asign and cant_cred <= 0 and cost_cred <= 0:
            raise ValueError("Los valores no pueden ser nulos")
    nom_asign = ""
    cant_cred = 0.0
    cost_cred = 0.0

import unidecode


class Asignatura:
    def __init__(self, nom_asign, cant_cred, cost_cred, semestre):
        self.nom_asign = nom_asign
        self.cant_cred = cant_cred
        self.cost_cred = cost_cred
        self.semestre = semestre
        self.valor_total = self.cant_cred * self.cost_cred


    def total_recaudado(self):
        return self.cant_cred * self.cost_cred

    @property
    def nom_asign(self):
        return self._nom_asign
    
    @nom_asign.setter
    def nom_asign(self, value):
        if isinstance(value, str):
            value = unidecode.unidecode(value).upper()
            value = value.replace('1', 'I').replace('2', 'II').replace('3', 'III') \
                         .replace('4', 'IV').replace('5', 'V')
            self._nom_asign = value
        else:
            raise TypeError("El nombre de la asignatura debe ser una cadena de texto.")

    @property
    def cant_cred(self):
        return self._cant_cred
    
    @cant_cred.setter
    def cant_cred(self, value):
        if isinstance(value, int):
            self._cant_cred = value
        else:
            raise TypeError("La cantidad de créditos debe ser un entero.")

    @property
    def cost_cred(self):
        return self._cost_cred
    
    @cost_cred.setter
    def cost_cred(self, value):
        if isinstance(value, float):
            self._cost_cred = value
        else:
            raise TypeError("El costo de los créditos debe ser un número decimal.")
    
    @property
    def semestre(self):
        return self._semestre
    
    @semestre.setter
    def semestre(self, value):
        if isinstance(value, int):
            self._semestre = value
        else:
            raise TypeError("El semestre debe ser un entero.")

    def __str__(self):
        return f"[Asignatura: {self.nom_asign},\n Créditos: {self.cant_cred},\n Costo/Crédito: {self.cost_cred},\n Semestre: {self.semestre}]\n"

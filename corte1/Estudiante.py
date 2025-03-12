import Asignatura

class Estudiante:

    DESCUENTOS = {1:0.50, 2:0.30, 3:0.20}

    def __init__(self, nom_est, gen_est, edad, estr_soc):
            
        if not nom_est.isalpha():
            raise ValueError("Nombre debe ser una cadena de texto")
        if not gen_est.isalpha():
            raise ValueError("Genero debe ser una cadena de texto")
        if  edad < 15:
            raise ValueError("Edad debe ser un numero")
        if estr_soc <= 0 or estr_soc >6:
            raise ValueError("El valor de estrato socioeconómico debe estar entre 1 y 6")

        
        self.nom_est = str(nom_est)
        self.gen_est = str(gen_est)
        self.edad = int(edad)
        self.estr_soc = int(estr_soc)

    def calcular_costo_matricula(self, costo_credito, cantidad_creditos):
        descuento = self.DESCUENTOS.get(self.estrato, 0)
        total_sin_descuento = costo_credito * cantidad_creditos
        descuento_aplicado = total_sin_descuento * descuento
        return total_sin_descuento - descuento_aplicado, descuento_aplicado

    def inscribir_asignatura(self, asignatura):
        if not isinstance(asignatura, Asignatura):
            raise ValueError("El objeto asignatura debe ser de la clase Asignatura")
        self.asignaturas.append(asignatura)
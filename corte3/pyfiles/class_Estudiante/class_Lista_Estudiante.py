from pyfiles.class_Lista.class_Lista import ListaGenerica

class ListaEstudiante(ListaGenerica):
    def __init__(self):
        super().__init__()
        self._head = None

    def contar_estudiantes_por_asignatura(self):
        conteo = {}
        actual = self._head
        while actual:
            asign = actual.dato.asignatura
            if asign in conteo:
                conteo[asign] += 1
            else:
                conteo[asign] = 1
            actual = actual.siguiente
        return conteo

    


    def troncar_posicion(self):
        pass
    
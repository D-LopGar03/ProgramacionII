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

    def recaudo_por_asignatura(self):
        conteo = {}
        actual = self._head
        while actual:
            asign = actual.dato.asignatura
            if asign in conteo:
                conteo[asign] += actual.dato.valor_pagar
            else:
                conteo[asign] = actual.dato.valor_pagar
            actual = actual.siguiente
        return conteo
    

    def eliminar_estudiante_nombre(self, nombre):
        actual = self._head
        anterior = None
        while actual:
            if actual.dato.nombre == nombre:
                if anterior is None:
                    self._head = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False


    def troncar_posicion(self):
        pass
    
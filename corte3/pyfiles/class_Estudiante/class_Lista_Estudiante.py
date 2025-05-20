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
    

    def total_recaudado_por_estrato(self, estrato):
        if estrato not in [1, 2, 3]:
            raise ValueError("El estrato debe ser 1, 2 o 3.")

        total = 0
        actual = self._head

        while actual:
            if actual.dato.estrato == estrato:
                total += actual.dato.valor_pagar
            actual = actual.siguiente

        return total


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

    def recaudo_total(self):
        total = 0
        actual = self._head
        while actual:
            total += actual.dato.valor_pagar
            actual = actual.siguiente
        return total
    

    def cuantos_estrato_uno(self):
        contador = 0
        actual = self._head
        while actual:
            if actual.dato.estrato == 1:
                contador += 1
            actual = actual.siguiente
        return contador


    def troncar_posicion(self):
        pass
    
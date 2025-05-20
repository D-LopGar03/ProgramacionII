from pyfiles.class_Lista.class_Lista import ListaGenerica

class ListaAsignatura(ListaGenerica):
    def __init__(self):
        super().__init__()
        self._head = None


    def eliminar_asignatura_nombre(self, nombre_a_eliminar):

        if self._head is None:
            return False
            
        if self._head.dato.nom_asign == nombre_a_eliminar:
            self._head = self._head.siguiente
            return True 
        
        nodo_actual = self._head
        while nodo_actual.siguiente is not None:
            if nodo_actual.siguiente.dato.nom_asign == nombre_a_eliminar:
                nodo_actual.siguiente = nodo_actual.siguiente.siguiente
                return True
            nodo_actual = nodo_actual.siguiente
        
        return False
    

    def asignatura_mayor_recaudo(self, lista_estudiantes):
        recaudos = lista_estudiantes.recaudo_por_asignatura()
        if not recaudos:
            return None
        asignatura_mayor = max(recaudos, key=recaudos.get)
        return asignatura_mayor, recaudos[asignatura_mayor]


    def recaudo_por_asignatura(self, lista_estudiantes):
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


    def buscar_por_nombre(self, nombre_buscar):
        nodo_actual = self._head
        while nodo_actual is not None:
            if nodo_actual.dato.nom_asign == nombre_buscar:
                return nodo_actual
            nodo_actual = nodo_actual.siguiente
        return None
    
         
    def troncar_posicion(self):
        pass
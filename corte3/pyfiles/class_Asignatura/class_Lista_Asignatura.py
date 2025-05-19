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
    



    def buscar_por_nombre(self, nombre_buscar):
        nodo_actual = self._head
        while nodo_actual is not None:
            if nodo_actual.dato.nom_asign == nombre_buscar:
                return nodo_actual
            nodo_actual = nodo_actual.siguiente
        return None
    
    def eliminar_asignatura_posicion(self, posicion):
        if self._head is None:
            return False
        
        if posicion == 0:
            self._head = self._head.siguiente
            return True
        
        nodo_actual = self._head
        contador = 0
        
        while nodo_actual is not None and contador < posicion - 1:
            nodo_actual = nodo_actual.siguiente
            contador += 1
        
        if nodo_actual is None or nodo_actual.siguiente is None:
            return False
        
        nodo_actual.siguiente = nodo_actual.siguiente.siguiente
        return True

    

         
    def troncar_posicion(self):
        pass
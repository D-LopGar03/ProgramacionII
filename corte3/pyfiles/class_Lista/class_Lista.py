from pyfiles.class_Lista.class_Nodo import Nodo
from abc import ABC, abstractmethod


class ListaGenerica(ABC):

    def __init__(self):
        self._head = None


    def contar_nodos(self):
        contador = 0
        nodo_actual = self._head

        while nodo_actual is not None:
            contador += 1
            nodo_actual = nodo_actual.siguiente

        return contador

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)

        if self._head is None:
            self._head = nuevo_nodo
        else:
            ultimo_nodo = self._head
            while ultimo_nodo.siguiente is not None:
                ultimo_nodo = ultimo_nodo.siguiente
            ultimo_nodo.siguiente = nuevo_nodo

    def mostrar(self):
        nodo_actual = self._head
        while nodo_actual is not None:
            print(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente


    def buscar_por_posicion(self, posicion):

        if posicion < 0:
            return None
        
        contador = 1
        actual = self._head
        
        while actual is not None:
            if contador == posicion:
                return actual.dato
            contador += 1
            actual = actual.siguiente
        
        return None


    def eliminar_por_posicion(self, posicion):
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



    @abstractmethod
    def troncar_posicion(self):
        pass
    

    
    
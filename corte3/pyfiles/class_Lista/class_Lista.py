from pyfiles.class_Lista.class_Nodo import Nodo
from abc import ABC, abstractmethod


class ListaGenerica(ABC):

    def __init__(self):
        self._head = None

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



    @abstractmethod
    def eliminar_asignatura_nombre(self, nombre_a_eliminar):
        pass
   

    @abstractmethod
    def troncar_posicion(self):
        pass
    

    
    
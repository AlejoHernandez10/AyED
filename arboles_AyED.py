class NodoArbol:
    def __init__(self, dato):
        """Clase Nodo para la implementacion de arboles en python."""
        self.informacion = dato
        self.izquierda = None
        self.derecha = None

def arbol_vacio(raiz) -> bool:
    return raiz is None 

def insertar_nodo(raiz, dato):
    """
    funcion que insterta nodos en el arbol
    Si son menores al valor del nodo comparado, a la izquierda
    Si son mayores al valor del nodo comparado, a la derecha
    """
    if arbol_vacio(raiz):
        raiz = NodoArbol(dato)
    elif (raiz.informacion <= dato):
        raiz.derecha = insertar_nodo(raiz.derecha, dato)
    else:
        raiz.izquierda = insertar_nodo(raiz.izquierda, dato)
    return raiz

def imprimir_arbol(raiz):
    if arbol_vacio(raiz):
        print(" - ")
    else:
        print(F"{ [raiz.informacion] }")
        print(F"Rama izquierda del nodo {raiz.informacion}") 
        imprimir_arbol(raiz.izquierda)
        print(F"Rama derecha del nodo {raiz.informacion}")
        imprimir_arbol(raiz.derecha)

arbol = insertar_nodo(None, 32)
arbol = insertar_nodo(arbol, 11)
arbol = insertar_nodo(arbol, 44)
arbol = insertar_nodo(arbol, 5)
imprimir_arbol(arbol)
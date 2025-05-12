class Nodo:

    def __init__(self, dato=None, siguiente=None):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
        """Implementación de una lista enlazada en Python."""
            
        def __init__(self):
            self.inicio = None
            self.tamanio = 0

def insertar(lista, elemento):
    """Agrega un nuevo nodo a la cima de la lista."""
    nodo_a_insertar = Nodo(elemento)
    if (lista.inicio is None) or (lista.inicio.dato > elemento):
        nodo_a_insertar.siguiente = lista.inicio
        lista.inicio = nodo_a_insertar
    else:
        anterior = lista.inicio
        actual = lista.inicio.siguiente
        while(actual is not None) and (actual.dato < elemento):
            anterior = anterior.siguiente
            actual = actual.siguiente
        anterior.siguiente = nodo_a_insertar
        nodo_a_insertar.siguiente = actual
    lista.tamanio += 1

def eliminar(lista, valor):
    dato = None
    if (lista.inicio.dato == valor):
        dato = lista.inicio.dato
        lista.inicio = lista.inicio.siguiente
        lista.tamanio -= 1
    else:
        anterior = lista.inicio
        actual = lista.inicio.siguiente
        while(actual is not None) and (actual.dato != valor):
            anterior = anterior.siguiente
            actual = actual.siguiente
        if actual is not None:
            dato = actual.dato
            anterior.siguiente = actual.siguiente
            lista.tamanio -= 1
    return dato

def print_lista(lista):
    if lista.tamanio == 0:
        print("La lista está vacía.")
    else:
        contador = 0
        nodo = lista.inicio
        while(contador < lista.tamanio):
            print(nodo.dato)
            nodo = nodo.siguiente
            contador += 1

def is_empty(lista):
    pass

def longitud(lista):
    pass

lista1 = ListaEnlazada()
insertar(lista1, 3)
insertar(lista1, 1)
insertar(lista1, 2)
insertar(lista1, 8)
insertar(lista1, 11)
insertar(lista1, 2)
print_lista(lista1)
print(F"Se elimina el primer elemento: {eliminar(lista1, 1)}")
print_lista(lista1)
print(F"Se elimina el elemento 11: {eliminar(lista1, 11)}")
print_lista(lista1)
print(F"Se elimina el elemento 2: {eliminar(lista1, 2)}")
print_lista(lista1)
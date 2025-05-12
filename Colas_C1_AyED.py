class Nodo:
    """Clase que representa un nodo para contruir una cola."""
    def __init__(self, dato=None, siguiente=None):
        self.dato = dato
        self.siguiente = None

class Cola:
    """implementación de una cola en phyton."""
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamanio = 0

def enqueue(cola, dato):
    nodo = Nodo(dato)
    if cola.frente is None:
        cola.frente = nodo
    else:
        cola.final.siguiente = nodo
    cola.final = nodo
    cola.tamanio += 1

def dequeue(cola):
    if cola.tamanio == 0:
        raise RuntimeError("No hay mas elementos para remover")
    else:
        nodo_a_devolver = cola.frente
        cola.frente = nodo_a_devolver.siguiente
        if (cola.frente is None):
            cola.final = None
        cola.tamanio -= 1
        return nodo_a_devolver

def is_empty(cola):
    """Verifica si la cola está vacía."""
    return (cola.tamanio == 0)


def imprimir_cola(cola):
    """Imprime los elementos de la cola."""
    if cola.tamanio == 0:
        return 
    else:
        nodo = cola.frente
        print(cola.frente.dato)
        while (nodo.siguiente is not None):
            nodo = nodo.siguiente
            print(nodo.dato)

def front(cola):
    """Devuelve el nodo del frente de la cola sin eliminarlo."""
    if cola.tamanio == 0:
        return None
    else:
        return cola.frente.dato

cola1 = Cola()
enqueue(cola1, "1")
enqueue(cola1, "2")
enqueue(cola1, "3")
enqueue(cola1, "4")
print("Contenido de la cola:")
imprimir_cola(cola1)
print(F"el dato del frente es: {front(cola1)}")
print(F"El dato del frente es: {cola1.frente.dato}")
print(F"El dato del final es: {cola1.final.dato}")
print(F"remuevo el primer elemento de la cola {dequeue(cola1).dato}")
print(F"remuevo el segundo elemento de la cola {dequeue(cola1).dato}")
print(F"remuevo el tercer elemento de la cola {dequeue(cola1).dato}")
print(F"remuevo el cuarto elemento de la cola {dequeue(cola1).dato}")#
print(cola1.tamanio)
print(F"el dato del frente es: {front(cola1)}")
class Nodo:
    """Clase que representa un nodo para contruir una pila."""
    def __init__(self, dato=None, siguiente=None):
        self.dato = dato
        self.siguiente = None

class Pila:
    """implementación de una pila en phyton."""
    def __init__(self):
        self.cima = None
        self.tamanio = 0


nodo1 = Nodo()  
nodo2 = Nodo(1)
nodo3 = Nodo(2)

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
print(nodo1.siguiente.dato)  # Imprime el dato del segundo nodo (1)
print(nodo2.siguiente.dato)  # Imprime el dato del tercer nodo (2)
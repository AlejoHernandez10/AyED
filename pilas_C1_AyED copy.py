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


def push(pila, dato_nuevo):
    """Agrega un nuevo nodo a la cima de la pila."""
    nodo_a_apilar = Nodo(dato_nuevo)
    nodo_a_apilar.siguiente = pila.cima
    pila.cima = nodo_a_apilar
    pila.tamanio += 1

def pop(pila):
    """Elimina el nodo de la cima de la pila."""
    if pila.tamanio == 0:
        raise RuntimeError("No hay mas elementos para remover")
    else:
        nodo_a_retornar = pila.cima
        pila.cima = nodo_a_retornar.siguiente
        pila.tamanio -= 1
        return nodo_a_retornar

def is_empty(pila):
    """Verifica si la pila está vacía."""
    return (pila.tamanio == 0)

def top(pila):
    """Devuelve el nodo de la cima de la pila sin eliminarlo."""
    if pila.tamanio == 0:
        return None
    else:
        return pila.cima.dato
    
def print_pila(pila):
    """Imprime los elementos de la pila."""
    if pila.tamanio == 0:
        return 
    else:
        nodo = pila.cima
        print(pila.cima.dato)
        while (nodo.siguiente is not None):
            nodo = nodo.siguiente
            print(pila.cima.dato)   

pila1 = Pila()
push(pila1, "A")
push(pila1, "B")
push(pila1, "C")
print(F"El dato de la cima es: {top(pila1)}")
print(pila1.tamanio)  
print(F"¿La pila está vacía? {is_empty(pila1)}") 

print("--------")
print_pila(pila1)
print("--------")

resultado = pop(pila1)
print(resultado.dato)  
resultado = pop(pila1)
print(resultado.dato) 
resultado = pop(pila1)
print(resultado.dato)
print(F"¿La pila está vacía? {is_empty(pila1)}")
print(F"El dato de la cima es: {top(pila1)}")
print_pila(pila1)
resultado = pop(pila1)
print(resultado.dato)  
print(pila1.cima.dato)     
print(pila1.tamanio)  
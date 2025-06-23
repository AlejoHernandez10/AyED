# En una lista, tengo informacion sobre usuarios en forma de diccionarios
# Las claves son dni, apellido ( en mayúsculas), nombre (capitalizado), sueldo (Float)
# 10 usuarios deben ser ingresados previamente

# Menú
# 1 - ingresar usuario
# 2 - buscar usuario por DNI
# 0 - salir

# Lista de usuarios predefinidos (10 usuarios)
usuarios = [
    {"dni": "12345678", "apellido": "PEREZ", "nombre": "Juan", "sueldo": 50000.0},
    {"dni": "23456789", "apellido": "GOMEZ", "nombre": "Maria", "sueldo": 62000.0},
    {"dni": "34567890", "apellido": "LOPEZ", "nombre": "Carlos", "sueldo": 58000.0},
    {"dni": "45678901", "apellido": "RODRIGUEZ", "nombre": "Ana", "sueldo": 54000.0},
    {"dni": "56789012", "apellido": "FERNANDEZ", "nombre": "Luis", "sueldo": 60000.0},
    {"dni": "67890123", "apellido": "MARTINEZ", "nombre": "Sofia", "sueldo": 63000.0},
    {"dni": "78901234", "apellido": "GARCIA", "nombre": "Pedro", "sueldo": 51000.0},
    {"dni": "89012345", "apellido": "RAMIREZ", "nombre": "Lucia", "sueldo": 59000.0},
    {"dni": "90123456", "apellido": "SANCHEZ", "nombre": "Diego", "sueldo": 61000.0},
    {"dni": "01234567", "apellido": "ALVAREZ", "nombre": "Laura", "sueldo": 57000.0}
]

def mostrar_menu():
    print("\nMenú")
    print("1 - Ingresar usuario")
    print("2 - Buscar usuario por DNI")
    print("0 - Salir")

def ingresar_usuario():
    dni = input("Ingrese el DNI: ")
    apellido = input("Ingrese el apellido (se guardará en mayúsculas): ").upper()
    nombre = input("Ingrese el nombre (se capitalizará): ").capitalize()
    try:
        sueldo = float(input("Ingrese el sueldo: "))
    except ValueError:
        print("Sueldo inválido. Debe ser un número.")
        return
    usuario = {"dni": dni, "apellido": apellido, "nombre": nombre, "sueldo": sueldo}
    usuarios.append(usuario)
    print("Usuario ingresado con éxito.")

def buscar_usuario_por_dni():
    dni = input("Ingrese el DNI a buscar: ")
    for usuario in usuarios:
        if usuario["dni"] == dni:
            print("Usuario encontrado:")
            print(usuario)
            return
    print("Usuario no encontrado.")

# Bucle principal
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        ingresar_usuario()
    elif opcion == "2":
        buscar_usuario_por_dni()
    elif opcion == "0":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
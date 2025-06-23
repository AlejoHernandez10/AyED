# Lista de usuarios
usuarios = [
    {"dni": "11222331", "apellido": "HERNANDEZ", "nombre": "Alejo", "sueldo": 100000},
    {"dni": "11222332", "apellido": "GOMEZ", "nombre": "Maria", "sueldo": 120000},
    {"dni": "11222333", "apellido": "LOPEZ", "nombre": "Carlos", "sueldo": 130000},
    {"dni": "11222334", "apellido": "RAMIREZ", "nombre": "Pepe", "sueldo": 140000}
]

# Mostrar búsqueda
valor = input("Ingrese valor a buscar -> ")

print("¿Por qué criterio busca?")
print("1 - DNI")
print("2 - Apellido")
print("3 - Nombre")
print("4 - Sueldo")

criterio = input("Ingrese el número del criterio: ")

encontrado = False

for usuario in usuarios:
    if criterio == "1":  # Buscar por DNI
        if not valor.isdigit():
            print("Error: El DNI debe contener solo números.")
            break
        if usuario["dni"] == valor:
            print("Usuario encontrado:")
            print(usuario)
            encontrado = True
            break

    if criterio in ["2", "3", "4"]:
        clave = {"2": "apellido", "3": "nombre", "4": "sueldo"}[criterio]
        dato_usuario = usuario[clave]

    try:
        valor_comparado = float(valor) if clave == "sueldo" else valor.lower()
        dato_comparado = dato_usuario if clave == "sueldo" else dato_usuario.lower()

        if dato_comparado == valor_comparado:
            print("Usuario encontrado:")
            print(usuario)
            encontrado = True
            break
    except ValueError:
        print("Error: El sueldo debe ser un número válido.")
        break

    else:
        print("Criterio inválido.")
        break

if not encontrado and criterio in ["1", "2", "3", "4"]:
    print("No se encontró ningún usuario con ese dato.")


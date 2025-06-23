import os
import shutil
import fnmatch

def listar_archivos():
    print("\nArchivos en el directorio actual:")
    for archivo in os.listdir():
        print(" -", archivo)

def mostrar_directorio_actual():
    print("\nDirectorio de trabajo actual:")
    print(os.getcwd())

def listar_por_patron():
    patron = input("Introduce el patrón a buscar (ej: *.txt): ")
    print(f"\nArchivos que coinciden con el patrón '{patron}':")
    archivos = fnmatch.filter(os.listdir(), patron)
    if archivos:
        for archivo in archivos:
            print(" -", archivo)
    else:
        print("No se encontraron archivos que coincidan.")

def crear_carpeta():
    nombre = input("Introduce el nombre de la carpeta a crear: ")
    if not os.path.exists(nombre):
        os.makedirs(nombre)
        print(f"Carpeta '{nombre}' creada exitosamente.")
    else:
        print(f"La carpeta '{nombre}' ya existe.")

def borrar_carpeta():
    nombre = input("Introduce el nombre de la carpeta a borrar: ")
    try:
        os.rmdir(nombre)
        print(f"Carpeta '{nombre}' borrada exitosamente.")
    except Exception as e:
        print(f"No se pudo borrar la carpeta: {e}")

def copiar_archivo():
    archivo_original = input("Introduce el nombre del archivo a copiar: ")
    if not os.path.isfile(archivo_original):
        print(f"El archivo '{archivo_original}' no existe.")
        return
    nuevo_nombre = input("Introduce el nuevo nombre para el archivo: ")
    try:
        shutil.copy(archivo_original, nuevo_nombre)
        print(f"Archivo copiado como '{nuevo_nombre}'.")
    except Exception as e:
        print(f"No se pudo copiar el archivo: {e}")

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1 - Listar todos los archivos")
        print("2 - Mostrar el directorio de trabajo actual")
        print("3 - Listar los archivos según patrón o condición")
        print("4 - Crear una nueva carpeta")
        print("5 - Borrar una carpeta")
        print("6 - Copiar un archivo con otro nombre")
        print("0 - Salir del Programa")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            listar_archivos()
        elif opcion == "2":
            mostrar_directorio_actual()
        elif opcion == "3":
            listar_por_patron()
        elif opcion == "4":
            crear_carpeta()
        elif opcion == "5":
            borrar_carpeta()
        elif opcion == "6":
            copiar_archivo()
        elif opcion == "0":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()
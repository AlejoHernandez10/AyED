

with open("archivoinfo.txt", "r") as f:
    contenido = f.readlines()
    for i in range(0, len(contenido)):
        registro = contenido[i].split(" ")  
        print(F"Linea {i}: {registro[1]}, {registro[2]}, DNI: {registro[0]} cobra un sueldo de ${registro[3]}")
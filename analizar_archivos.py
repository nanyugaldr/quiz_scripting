
import os
import sys

def analizar_archivos(directorio):
    if not os.path.isdir(directorio):
        print("Error: El directorio no existe.")
        print("Uso: python analizar_archivos.py <directorio>")
        sys.exit(1)

    informe = []
    archivos_encontrados = False

    for archivo in os.listdir(directorio):
        if archivo.endswith('.txt'):
            archivos_encontrados = True
            ruta_archivo = os.path.join(directorio, archivo)
            try:
                with open(ruta_archivo, 'r') as f:
                    contenido = f.readlines()
                    num_lineas = len(contenido)
                    num_palabras = sum(len(line.split()) for line in contenido)
                    num_python = sum(line.lower().count('python') for line in contenido)

                    informe.append(f"Archivo: {archivo}\n"
                                   f"Número de líneas: {num_lineas}\n"
                                   f"Número total de palabras: {num_palabras}\n"
                                   f"Número de veces que aparece 'Python': {num_python}\n")
            except PermissionError:
                print(f"Error: No se puede leer el archivo {archivo}. Sin permisos.")
            except Exception as e:
                print(f"Error al procesar el archivo {archivo}: {e}")

    if not archivos_encontrados:
        informe.append("No se encontraron archivos de texto.\n")

    # Escribir el informe en un archivo
    with open(os.path.join(directorio, 'informe.txt'), 'w') as f:
        f.write("\n".join(informe))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Se debe proporcionar un directorio.")
        print("Uso: python analizar_archivos.py <directorio>")
        sys.exit(1)

    directorio = sys.argv[1]
    analizar_archivos(directorio)


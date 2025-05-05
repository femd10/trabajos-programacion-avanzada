
import os

def cargar_notas():
    """Carga las notas desde el archivo 'notas.txt'.
    Retorna una lista de diccionarios con las notas."""
    notas = []
    if os.path.exists("notas.txt"):
        with open("notas.txt", "r") as archivo:
            for linea in archivo:
                # Divide cada línea por coma y extrae los datos
                partes = linea.strip().split(",")
                if len(partes) == 3:
                    nota = {
                        "titulo": partes[0],
                        "contenido": partes[1],
                        "fecha": partes[2]
                    }
                    notas.append(nota)
    return notas

def guardar_nota(nota):
    """Guarda una nueva nota en el archivo 'notas.txt'.
    La nota debe ser un diccionario con título, contenido y fecha."""
    with open("notas.txt", "a") as archivo:
        linea = f"{nota['titulo']},{nota['contenido']},{nota['fecha']}\n"
        archivo.write(linea)

def mostrar_nota(nota):
    """Muestra en consola el contenido de una nota."""
    print("Título:", nota["titulo"])
    print("Contenido:", nota["contenido"])
    print("Fecha:", nota["fecha"])
    print("-" * 30)

def contar_notas():
    """Cuenta cuántas notas hay en el archivo 'notas.txt'."""
    if not os.path.exists("notas.txt"):
        return 0
    with open("notas.txt", "r") as archivo:
        return sum(1 for _ in archivo)

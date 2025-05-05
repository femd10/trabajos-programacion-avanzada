
from utils import guardar_nota, cargar_notas, mostrar_nota, contar_notas
from datetime import datetime

def crear_nota():
    while True:
        titulo = input("Ingrese el título de la nota: ").strip()
        if titulo == "":
            print("El título no puede estar vacío.")
            continue
        break

    while True:
        contenido = input("Ingrese el contenido de la nota: ").strip()
        if contenido == "":
            print("El contenido no puede estar vacío.")
            continue
        break

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nota = {"titulo": titulo, "contenido": contenido, "fecha": fecha}
    guardar_nota(nota)
    print("Nota guardada exitosamente.")

def ver_notas():
    notas = cargar_notas()
    if not notas:
        print("No hay notas guardadas.")
    else:
        for nota in notas:
            mostrar_nota(nota)

def menu():
    while True:
        print("\n--- MENÚ DE NOTAS ---")
        print("1. Crear nota")
        print("2. Ver notas")
        print("3. Contar notas")
        print("4. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            crear_nota()
        elif opcion == "2":
            ver_notas()
        elif opcion == "3":
            print(f"Total de notas guardadas: {contar_notas()}")
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()

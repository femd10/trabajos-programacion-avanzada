
from utils import init, register, login, crear_nota, listar_notas, leer_nota, editar_nota, eliminar_nota, contar_notas, exportar_pdf
from getpass import getpass

def menu_principal(username):
    while True:
        print(f"\n--- MENÚ de {username} ---")
        print("1. Crear nota")
        print("2. Listar notas")
        print("3. Leer nota")
        print("4. Editar nota")
        print("5. Eliminar nota")
        print("6. Contar notas")
        print("7. Exportar a PDF")
        print("8. Salir")
        opcion = input("Seleccione opción: ").strip()
        if opcion == "1":
            titulo = input("Título: ").strip()
            contenido = input("Contenido: ").strip()
            crear_nota(username, titulo, contenido)
        elif opcion == "2":
            listar_notas(username)
        elif opcion == "3":
            titulo = input("Título: ").strip()
            leer_nota(username, titulo)
        elif opcion == "4":
            titulo = input("Título: ").strip()
            nuevo = input("Nuevo contenido: ").strip()
            editar_nota(username, titulo, nuevo)
        elif opcion == "5":
            titulo = input("Título: ").strip()
            eliminar_nota(username, titulo)
        elif opcion == "6":
            print(f"Total: {contar_notas(username)} notas")
        elif opcion == "7":
            titulo = input("Título: ").strip()
            exportar_pdf(username, titulo)
        elif opcion == "8":
            break
        else:
            print("Opción inválida.")

def main():
    init()
    while True:
        print("\n--- Autenticación ---")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        op = input("Seleccione opción: ").strip()
        if op == "1":
            user = input("Usuario nuevo: ").strip()
            pwd = getpass("Contraseña: ")
            if register(user, pwd):
                print("Usuario registrado.")
            else:
                print("Usuario ya existe.")
        elif op == "2":
            user = input("Usuario: ").strip()
            pwd = getpass("Contraseña: ")
            if login(user, pwd):
                print("Ingreso exitoso.")
                menu_principal(user)
            else:
                print("Credenciales inválidas.")
        elif op == "3":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()

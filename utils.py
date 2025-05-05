
import os
import json
import shutil
from datetime import datetime
from fpdf import FPDF

CONFIG_FILE = "users.json"
NOTAS_DIR = "notas"

def init():
    """Inicializa las carpetas y archivo de usuarios."""
    os.makedirs(NOTAS_DIR, exist_ok=True)
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "w") as f:
            json.dump({}, f)

def register(username, password):
    """Registra un nuevo usuario con contraseña hashed."""
    with open(CONFIG_FILE, "r+") as f:
        users = json.load(f)
        if username in users:
            return False
        users[username] = sha256(password.encode()).hexdigest()
        f.seek(0)
        json.dump(users, f)
        f.truncate()
    os.makedirs(os.path.join(NOTAS_DIR, username), exist_ok=True)
    return True

def login(username, password):
    """Verifica credenciales de usuario."""
    with open(CONFIG_FILE) as f:
        users = json.load(f)
    hashed = users.get(username)
    return hashed == sha256(password.encode()).hexdigest()

def _nota_path(username, titulo):
    """Construye la ruta para la nota con estructura año/mes."""
    fecha = datetime.now()
    folder = os.path.join(NOTAS_DIR, username, f"{fecha.year}", f"{fecha.month:02d}")
    os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, f"{titulo}.txt")

def crear_nota(username, titulo, contenido):
    """Crea una nota de texto para el usuario."""
    ruta = _nota_path(username, titulo)
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(f"Fecha: {fecha}\n\n{contenido}")

def listar_notas(username):
    """Lista todas las notas del usuario."""
    base = os.path.join(NOTAS_DIR, username)
    for root, _, files in os.walk(base):
        for file in files:
            if file.endswith(".txt"):
                rel = os.path.relpath(root, base)
                print(f"- {os.path.join(rel, file)[:-4]}")

def leer_nota(username, titulo):
    """Muestra el contenido de una nota."""
    for root, _, files in os.walk(os.path.join(NOTAS_DIR, username)):
        if f"{titulo}.txt" in files:
            with open(os.path.join(root, f"{titulo}.txt"), "r", encoding="utf-8") as f:
                print(f.read())
            return
    print("Nota no encontrada.")

def editar_nota(username, titulo, nuevo_contenido):
    """Edita una nota creando un respaldo previo."""
    for root, _, files in os.walk(os.path.join(NOTAS_DIR, username)):
        if f"{titulo}.txt" in files:
            ruta = os.path.join(root, f"{titulo}.txt")
            respaldo = ruta.replace(".txt", "_bak.txt")
            shutil.copy(ruta, respaldo)
            with open(ruta, "w", encoding="utf-8") as f:
                f.write(nuevo_contenido)
            print("Nota actualizada y respaldo creado.")
            return
    print("Nota no encontrada.")

def eliminar_nota(username, titulo):
    """Elimina una nota del usuario."""
    for root, _, files in os.walk(os.path.join(NOTAS_DIR, username)):
        if f"{titulo}.txt" in files:
            os.remove(os.path.join(root, f"{titulo}.txt"))
            print("Nota eliminada.")
            return
    print("Nota no encontrada.")

def contar_notas(username):
    """Cuenta cuántas notas tiene un usuario."""
    count = 0
    for _, _, files in os.walk(os.path.join(NOTAS_DIR, username)):
        count += sum(1 for f in files if f.endswith(".txt"))
    return count

def exportar_pdf(username, titulo):
    """Exporta una nota a PDF usando FPDF."""
    for root, _, files in os.walk(os.path.join(NOTAS_DIR, username)):
        if f"{titulo}.txt" in files:
            ruta_txt = os.path.join(root, f"{titulo}.txt")
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            with open(ruta_txt, "r", encoding="utf-8") as f:
                for line in f:
                    pdf.cell(0, 10, line.strip(), ln=True)
            out_dir = os.path.join("pdfs", username)
            os.makedirs(out_dir, exist_ok=True)
            out_path = os.path.join(out_dir, f"{titulo}.pdf")
            pdf.output(out_path)
            print(f"Nota exportada a PDF: {out_path}")
            return
    print("Nota no encontrada para exportar.")

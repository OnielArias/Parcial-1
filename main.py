import sqlite3
import argparse

# Crea una conexión a la base de datos SQLite
conn = sqlite3.connect('inventario.db')
c = conn.cursor()

# Crea la tabla para almacenar los artículos del inventario
c.execute('''CREATE TABLE IF NOT EXISTS inventario
             (id integer PRIMARY KEY, nombre text, cantidad integer, precio real)''')

# Registrar un nuevo artículo en el inventario
def registrar_articulo(nombre, cantidad, precio):
    try:
        c.execute("INSERT INTO inventario (nombre, cantidad, precio) VALUES (?, ?, ?)", (nombre, cantidad, precio))
        conn.commit()
        print(f"El artículo '{nombre}' ha sido registrado en el inventario.")
    except sqlite3.IntegrityError:
        print(f"El artículo '{nombre}' ya existe en el inventario.")

# Editar un artículo existente
def editar_articulo(id, nombre, cantidad, precio):
    try:
        c.execute("UPDATE inventario SET nombre=?, cantidad=?, precio=? WHERE id=?", (nombre, cantidad, precio, id))
        conn.commit()
        print(f"El artículo con id '{id}' ha sido editado en el inventario.")
    except sqlite3.OperationalError:
        print(f"El artículo con id '{id}' no existe en el inventario.")

# Eliminar un artículo existente
def eliminar_articulo(id):
    try:
        c.execute("DELETE FROM inventario WHERE id=?", (id,))
        conn.commit()
        print(f"El artículo con id '{id}' ha sido eliminado del inventario.")
    except sqlite3.OperationalError:
        print(f"El artículo con id '{id}' no existe en el inventario.")

# Buscar un artículo en el inventario
def buscar_articulo(nombre):
    c.execute("SELECT * FROM inventario WHERE nombre=?", (nombre,))
    articulo = c.fetchone()
    if articulo:
        print(f"El artículo '{articulo[1]}' está en el inventario con id '{articulo[0]}', cantidad '{articulo[2]}' y precio '{articulo[3]}'.")
    else:
        print(f"No se encontró el artículo '{nombre}' en el inventario.")

# Listar todos los artículos en el inventario
def listar_articulos():
    c.execute("SELECT * FROM inventario")
    articulos = c.fetchall()
    if articulos:
        print("Los artículos en el inventario son:")
        for articulo in articulos:
            print(f"- id: {articulo[0]}, nombre: {articulo[1]}, cantidad: {articulo[2]}, precio: {articulo[3]}")
    else:
        print("No hay artículos en el inventario.")

# Configuración de la interfaz de línea de comandos
parser = argparse.ArgumentParser(description='Sistema de inventario.')
subparsers = parser.add_subparsers()

# Comando para registrar un artículo en el inventario
registrar_parser = subparsers.add_parser('registrar', help='Registrar un nuevo artículo en el inventario.')
registrar_parser.add_argument('nombre', type=str, help='Nombre del artículo.')
registrar_parser.add_argument('cantidad', type=int, help='Cantidad del artículo.')
registrar_parser.add_argument('precio')
import sqlite3
import argparse

# Crea una conexión a la base de datos SQLite
conn = sqlite3.connect('inventario.db')
c = conn.cursor()

# Crea la tabla para almacenar los artículos del inventario
c.execute('''CREATE TABLE IF NOT EXISTS inventario
             (id integer PRIMARY KEY, nombre text, cantidad integer, precio real)''')

# Registrar un nuevo artículo en el inventario
def registrar_articulo(nombre, cantidad, precio):
    try:
        c.execute("INSERT INTO inventario (nombre, cantidad, precio) VALUES (?, ?, ?)", (nombre, cantidad, precio))
        conn.commit()
        print(f"El artículo '{nombre}' ha sido registrado en el inventario.")
    except sqlite3.IntegrityError:
        print(f"El artículo '{nombre}' ya existe en el inventario.")

# Editar un artículo existente
def editar_articulo(id, nombre, cantidad, precio):
    try:
        c.execute("UPDATE inventario SET nombre=?, cantidad=?, precio=? WHERE id=?", (nombre, cantidad, precio, id))
        conn.commit()
        print(f"El artículo con id '{id}' ha sido editado en el inventario.")
    except sqlite3.OperationalError:
        print(f"El artículo con id '{id}' no existe en el inventario.")

# Eliminar un artículo existente
def eliminar_articulo(id):
    try:
        c.execute("DELETE FROM inventario WHERE id=?", (id,))
        conn.commit()
        print(f"El artículo con id '{id}' ha sido eliminado del inventario.")
    except sqlite3.OperationalError:
        print(f"El artículo con id '{id}' no existe en el inventario.")

# Buscar un artículo en el inventario
def buscar_articulo(nombre):
    c.execute("SELECT * FROM inventario WHERE nombre=?", (nombre,))
    articulo = c.fetchone()
    if articulo:
        print(f"El artículo '{articulo[1]}' está en el inventario con id '{articulo[0]}', cantidad '{articulo[2]}' y precio '{articulo[3]}'.")
    else:
        print(f"No se encontró el artículo '{nombre}' en el inventario.")

# Listar todos los artículos en el inventario
def listar_articulos():
    c.execute("SELECT * FROM inventario")
    articulos = c.fetchall()
    if articulos:
        print("Los artículos en el inventario son:")
        for articulo in articulos:
            print(f"- id: {articulo[0]}, nombre: {articulo[1]}, cantidad: {articulo[2]}, precio: {articulo[3]}")
    else:
        print("No hay artículos en el inventario.")

# Configuración de la interfaz de línea de comandos
parser = argparse.ArgumentParser(description='Sistema de inventario.')
subparsers = parser.add_subparsers()

# Comando para registrar un artículo en el inventario
registrar_parser = subparsers.add_parser('registrar', help='Registrar un nuevo artículo en el inventario.')
registrar_parser.add_argument('nombre', type=str, help='Nombre del artículo.')
registrar_parser.add_argument('cantidad', type=int, help='Cantidad del artículo.')
registrar_parser.add_argument('precio')

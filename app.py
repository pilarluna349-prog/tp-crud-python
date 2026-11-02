import sqlite3


def conectar():
  return sqlite3.connect("libreria.db")


def consultar():
  con = conectar()
  cur = con.cursor()
  cur.execute("SELECT * FROM libros")
  for row in cur.fetchall():
    print(row)
  cur.close()
  con.close()


def buscar():
  con = conectar()
  cur = con.cursor()
  id_libro = int(input("ID a buscar: "))
  cur.execute("SELECT * FROM libros WHERE id = ?", (id_libro,))
  row = cur.fetchone()
  print(row if row else "No encontrado")
  cur.close()
  con.close()


def agregar():
  con = conectar()
  cur = con.cursor()
  t = input("Título: ")
  a = input("Autor: ")
  anio = int(input("Año: "))
  p = float(input("Precio: "))
  cur.execute(
      "INSERT INTO libros (titulo, autor, anio, precio) VALUES (?, ?, ?, ?)",
      (t, a, anio, p),
  )
  con.commit()
  cur.close()
  con.close()


def actualizar():
  con = conectar()
  cur = con.cursor()
  id_libro = int(input("ID a actualizar: "))
  t = input("Nuevo título: ")
  a = input("Nuevo autor: ")
  anio = int(input("Nuevo año: "))
  p = float(input("Nuevo precio: "))
  cur.execute(
      "UPDATE libros SET titulo = ?, autor = ?, anio = ?, precio = ? WHERE id ="
      " ?",
      (t, a, anio, p, id_libro),
  )
  con.commit()
  cur.close()
  con.close()


def eliminar():
  con = conectar()
  cur = con.cursor()
  id_libro = int(input("ID a eliminar: "))
  cur.execute("DELETE FROM libros WHERE id = ?", (id_libro,))
  con.commit()
  cur.close()
  con.close()


def menu():
  while True:
    print("\n1. Consultar\n2. Buscar\n3. Agregar\n4. Actualizar\n5. Eliminar\n6. Salir")
    op = input("Opción: ")
    if op == "1":
      consultar()
    elif op == "2":
      buscar()
    elif op == "3":
      agregar()
    elif op == "4":
      actualizar()
    elif op == "5":
      eliminar()
    elif op == "6":
      break


if __name__ == "__main__":
  menu()
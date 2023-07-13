import sqlite3 as sql
from tkinter import messagebox


class Register:
    def __init__(self):
        self.cone = sql.connect("../LabManager.db")
        self.cursor = self.cone.cursor()
        self.create_login()

    def create_login(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS usuarios(id integer PRIMARY KEY AUTOINCREMENT, nome text NOT NULL, senha text NOT NULL, identificacao interger NOT NULL)")

    def cadastrar(self, dados):
        self.cursor.execute("INSERT INTO usuarios (nome, senha, identificacao) VALUES (?,?,?)", dados)
        messagebox.showinfo('Sucesso', 'Dados adicionados')
        self.cone.commit()

    def read_all(self):
        self.cursor.execute("SELECT * FROM usuarios")
        resultado = self.cursor.fetchall()
        for i in resultado:
            print(f"Id: {i[0]}, Usuário: {i[1]}, senha: {i[2]}, identificação: {i[3]}")

    def read_one(self, id):
        self.cursor.execute("SELECT * FROM usuarios WHERE id = ?",(id,))
        i = self.cursor.fetchone()
        print(f"Id: {i[0]}Usuário: {i[1]}, senha: {i[2]}, identificação: {i[3]}")

    def update(self, dados):
        self.cursor.execute("UPDATE usuarios SET nome = ?, senha = ?, identificacao=? WHERE id = ?", (dados))
        self.cone.commit()

    def delete(self,id):
        self.cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
        self.cone.commit()

    def deleteall(self):
        self.cursor.execute("DELETE FROM usuarios")
        self.cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'usuarios'")
        self.cone.commit()

    def close(self):
        self.cone.close()



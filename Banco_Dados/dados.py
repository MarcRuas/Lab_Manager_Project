import sqlite3 as sql

class Database:
    def __init__(self):
        self.dados = sql.connect('../LabManager.db')
        self.cursor = self.dados.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS equipamentos 
                                (id integer PRIMARY KEY AUTOINCREMENT,
                                 equipamento text NOT NULL,
                                 codigo integer NOT NULL,
                                 fornecedor text NOT NULL,
                                 status text NOT NULL,
                                 inicio text NULL,
                                 fim text NULL,
                                 responsavel text NULL,
                                 ra integer NULL,
                                 email text NULL,
                                 telefone integer NULL)''')

    def create(self, dados):
        self.cursor.execute('''INSERT INTO equipamentos 
                                (equipamento, codigo, 
                                fornecedor, status, inicio, fim,
                                responsavel, ra, 
                                email, telefone) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', dados)
        self.dados.commit()


    def read(self):
        self.cursor.execute('''SELECT * FROM equipamentos''')
        resultado = self.cursor.fetchall()
        for i in resultado:
            print(f"ID: {i[0]}, Equipamento: {i[1]}, Código: {i[2]}, Fornecedor: {i[3]}, Status: {i[4]}, Inicio: {i[5]}, Fim: {i[6]}, Responsável: {i[7]}, R.A: {i[8]}, E-mail: {i[9]}, Telefone: {i[10]}")

    def update(self, dados):
        novos_dados = "UPDATE equipamentos SET equipamento = ?, codigo = ?, fornecedor = ?, status = ?, inicio = ?, fim = ?, responsavel = ?, ra = ?, email = ?, telefone = ? WHERE id = ?"
        self.cursor.execute(novos_dados, dados)
        self.dados.commit()

    def delete(self, ID):
        self.cursor.execute("DELETE FROM equipamentos WHERE id = ?", (ID,))
        self.cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'equipamentos'")
        self.dados.commit()

    def search(self, id):
        self.cursor.execute('''SELECT * FROM equipamentos WHERE id = ? ''', (id,))
        i = self.cursor.fetchone()
        if i is not None:
            print(f"ID: {i[0]}, Equipamento: {i[1]}, Código: {i[2]}, Fornecedor: {i[3]}, Status: {i[4]}, Inicio: {i[5]}, Fim: {i[6]}, Responsável: {i[7]}, R.A: {i[8]}, E-mail: {i[9]}, Telefone: {i[10]}")
        else:
            print("ID não encontrado")
        return i


    def deleteall(self):
        self.cursor.execute("DELETE FROM equipamentos")
        self.cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'equipamentos'")
        self.dados.commit()

    def get_all_data(self):
        self.cursor.execute("SELECT * FROM equipamentos")
        return self.cursor.fetchall()

    def retorna(self, id):
        self.cursor.execute('''SELECT * FROM equipamentos WHERE id = ? ''', (id,))
        return self.cursor.fetchall()


    def close(self):
        self.dados.close()

dados = Database()
dados.read()






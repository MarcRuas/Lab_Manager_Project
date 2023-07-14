from Back_End.modulos_main import *
class Funcs():
    def adicionar_dados(self):
        equipamento = self.equipamento_entry.get()
        codigo = self.codigo_entry.get()
        fornecedor = self.fornecedor_entry.get()
        status = self.status_entry.get()
        responsavel = self.responsavel_entry.get()
        ra = self.ra_entry.get()
        email = self.email_entry.get()
        inicio = self.data_inicio.get()
        fim = self.data_fim.get()
        telefone = self.telefone_entry.get()

        dados = (equipamento, codigo, fornecedor, status, inicio, fim, responsavel, ra, email, telefone)
        self.db.create(dados)
        messagebox.showinfo('Sucesso', 'Dados adicionados')

        self.tree.delete(*self.tree.get_children())  # Limpa a Treeview
        data = self.db.get_all_data()  # Obtém os dados atualizados
        for item in data:
            self.tree.insert('', 'end', values=item)

        self.limpar()

    def procurar_dados(self):
        id = self.e_procurar.get()
        valor = self.db.search(id)  # Obter os dados do banco de dados
        if valor:
            _, equipamento, codigo, fornecedor, status, inicio, fim, responsavel, ra, email, telefone = valor

            self.equipamento_entry.delete(0, 'end')
            self.equipamento_entry.insert(0, equipamento)

            self.codigo_entry.delete(0, 'end')
            self.codigo_entry.insert(0, codigo)

            self.fornecedor_entry.delete(0, 'end')
            self.fornecedor_entry.insert(0, fornecedor)

            self.status_entry.delete(0, 'end')
            self.status_entry.insert(0, status)

            self.data_inicio.delete(0, 'end')
            self.data_inicio.insert(0, inicio)

            self.data_fim.delete(0, 'end')
            self.data_fim.insert(0, fim)

            self.responsavel_entry.delete(0, 'end')
            self.responsavel_entry.insert(0, responsavel)

            self.ra_entry.delete(0, 'end')
            self.ra_entry.insert(0, ra)

            self.email_entry.delete(0, 'end')
            self.email_entry.insert(0, email)

            self.telefone_entry.delete(0, 'end')
            self.telefone_entry.insert(0, telefone)
        else:
            messagebox.showinfo('Erro', 'ID não encontrado')

    def atualizar(self):
        id = self.e_procurar.get()
        equipamento = self.equipamento_entry.get()
        codigo = self.codigo_entry.get()
        fornecedor = self.fornecedor_entry.get()
        status = self.status_entry.get()
        responsavel = self.responsavel_entry.get()
        ra = self.ra_entry.get()
        email = self.email_entry.get()
        inicio = self.data_inicio.get()
        fim = self.data_fim.get()
        telefone = self.telefone_entry.get()

        dados = (id, equipamento, codigo, fornecedor, status, inicio, fim, responsavel, ra, email, telefone)
        self.db.update(dados)

        self.e_procurar.delete(0, 'end')

    def limpar(self):
        self.e_procurar.delete(0, 'end')
        self.equipamento_entry.delete(0, 'end')
        self.codigo_entry.delete(0, 'end')
        self.fornecedor_entry.delete(0, 'end')
        self.status_entry.delete(0, 'end')
        self.responsavel_entry.delete(0, 'end')
        self.ra_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.telefone_entry.delete(0, 'end')
        self.data_fim.delete(0, 'end')
        self.data_inicio.delete(0, 'end')

    def double(self, event):
        self.limpar()
        item = self.tree.selection()[0]  # Obtém o item selecionado
        dados = self.tree.item(item, 'values')  # Obtém os valores do item selecionado
        print(dados)  # Imprime os valores para verificar a estrutura
        id, equipamento, codigo, fornecedor, status, inicio, fim, responsavel, ra, email, telefone = dados

        self.e_procurar.insert(0, id)
        self.equipamento_entry.insert(0, equipamento)
        self.codigo_entry.insert(0, codigo)
        self.fornecedor_entry.insert(0, fornecedor)
        self.status_entry.insert(0, status)
        self.data_inicio.insert(0, inicio)
        self. data_fim.insert(0,fim)
        self.responsavel_entry.insert(0, responsavel)
        self.ra_entry.insert(0, ra)
        self.email_entry.insert(0, email)
        self.telefone_entry.insert(0, telefone)

    def apagar(self):
        id = self.e_procurar.get()
        self.db.delete(id)

        item = self.tree.selection()[0]
        self.tree.delete(item)
        self.limpar()
        messagebox.showinfo("Sucesso", "Dados apagadados com sucesso!")

    def atualizar(self):
        id = self.e_procurar.get()
        equipamento = self.equipamento_entry.get()
        codigo = self.codigo_entry.get()
        fornecedor = self.fornecedor_entry.get()
        status = self.status_entry.get()
        responsavel = self.responsavel_entry.get()
        ra = self.ra_entry.get()
        email = self.email_entry.get()
        inicio = self.data_inicio.get()
        fim = self.data_fim.get()
        telefone = self.telefone_entry.get()

        dados = (equipamento, codigo, fornecedor, status, inicio, fim, responsavel, ra, email, telefone, id)
        self.db.update(dados)

        self.tree.delete(*self.tree.get_children())  # Limpa a Treeview
        data = self.db.get_all_data()  # Obtém os dados atualizados
        for item in data:
            self.tree.insert('', 'end', values=item)
        self.limpar()
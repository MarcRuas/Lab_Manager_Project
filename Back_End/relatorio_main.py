from Back_End.modulos_main import *
class Relatorio():

    def abrir(self):
        webbrowser.open("relatorio.pdf")

    def enviar_email(self):
        email_usuario = self.email_entry.get()
        if email_usuario:
            url = f"https://mail.google.com/mail/?view=cm&fs=1&to={email_usuario}"
            webbrowser.open(url)
        else:
            print("email não encontrado")

    def relatorio(self):
        nome_arquivo = "relatorio.pdf"
        pdf = canvas.Canvas(nome_arquivo)


        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawString(50, 800, "Relatório de Dados")

        dados = []
        for item in self.tree.get_children():
            dados.append(self.tree.item(item, "values"))


        linha = 770
        for item in dados:
            texto = ", ".join(item)
            pdf.setFont("Helvetica", 12)
            pdf.drawString(50, linha, texto)
            linha -= 20


        pdf.showPage()
        pdf.save()
        self.abrir()

    def exportar_excel(self):
        dados = []

        for item in self.tree.get_children():
            dados.append(self.tree.item(item, "values"))

        df = pd.DataFrame(dados, columns=["ID", "Equipamento", "Código", "Fornecedor", "Status", "Início", "Fim", "Responsável", "R.A", "E-mail", "Telefone"])

        Relatorios = "Relatorio_dados.xlsx"

        df.to_excel(Relatorios, index=False)

        print(f"Os dados foram exportados para o arquivo {Relatorios}.")

    def sobre(self):
        messagebox.showinfo("Sobre", "Desenvolvido por Marco Ruas")
from tkinter import Tk, Label, Frame, PhotoImage, Entry, messagebox
from main import App
from Banco_Dados.admin import Register
from customtkinter import CTkButton


class Login:
    def __init__(self, janela):
        self.config(janela)
        self.layout(janela)
        self.db = Register()
        self.janela = janela


    def config(self, janela):
        self.janela = janela
        self.janela.title("LabManager")
        self.janela.resizable(False, False)
        self.janela.configure(background='white')

        largura = 500
        altura = 335
        largura_screen = self.janela.winfo_screenwidth()
        altura_screen = self.janela.winfo_screenheight()
        pos_x = (largura_screen - largura) // 2
        pos_y = (altura_screen - altura) // 2
        self.janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

    def abrir_main(self):
        nome = self.user.get()
        key = self.cod.get()
        Id = self.id.get()
        query = "SELECT * FROM usuarios WHERE nome=? AND senha=? AND identificacao=?"

        self.db.cursor.execute(query, (nome, key, Id))
        resultado = self.db.cursor.fetchone()

        if resultado:
            messagebox.showinfo("Sucesso", 'Conta Logada com Sucesso!')
            self.janela.destroy()  # Fechar a janela de login
            janela_app = Tk()
            app = App(janela_app)
            janela_app.mainloop()

        elif Id == '':
            messagebox.showerror("Erro", 'Preencha o id de funcionário!')


        elif nome == '':
            messagebox.showerror("Erro", 'Preencha o nome de funcionário!')

        elif key =='':
            messagebox.showerror("Erro", 'Preencha a senha de funcionário')

        else:
            messagebox.showerror("Erro", 'Funcionário não encontrado')
            self.user.delete(0, 'end')
            self.cod.delete(0, 'end')

    def layout(self, janela):

        self.frame_esquerda = Frame(janela, width='250', height='335', bg='white')
        self.frame_esquerda.grid(row=0, column=0)

        img = PhotoImage(file='../image/4.png')
        img_label = Label(self.frame_esquerda, image=img, bg="white")
        img_label.place(x=-30, y=45)
        img_label.image = img

        # Frame direita
        self.frame_direita = Frame(janela, width='250', height='335', bg='#8C52FF')
        self.frame_direita.grid(row=0, column=1)

        self.lb = Label(self.frame_direita, text="Login", font=("Montserrat 22"), bg='#8C52FF', foreground="white")
        self.lb.place(relx=0.5, y=15, anchor="n")

        # Label_Identificação
        label_id = Label(self.frame_direita, anchor='nw', text="R.A *:", bg='#8C52FF',
                           font=('MontserratSemiBold 10 '), fg="white")
        label_id.place(x=40, y=75)

        # Entry_Identificação
        self.id = Entry(self.frame_direita, width=20, fg="white", bg="#8C52FF", border=0, font="Inter 9")
        self.id.place(relx=0.5, y=95, anchor="n")
        self.linha3 = Frame(self.frame_direita, width=163, height=1, bg="white")
        self.linha3.place(relx=0.5, y=115, anchor="n")

        # Label_Usuário
        label_user = Label(self.frame_direita, anchor='nw', text="Funcionário *:", bg='#8C52FF', font=('MontserratSemiBold 10 '), fg="white")
        label_user.place(x=40, y=135)

        # Entry_Usuário
        self.user = Entry(self.frame_direita, width=20, fg="white", bg="#8C52FF", border=0, font="Inter 9")
        self.user.place(relx=0.5, y=155, anchor="n")
        self.linha = Frame(self.frame_direita, width=163, height=1, bg="white")
        self.linha.place(relx=0.5, y=175, anchor="n")

        # Label_Senha
        label_senha = Label(self.frame_direita, anchor='nw', text="Senha *:", bg='#8C52FF', font=('MontserratSemiBold 10'), fg="white")
        label_senha.place(x=40, y=195)

        # Entry_senha
        self.cod = Entry(self.frame_direita, width=20, fg="white", bg="#8C52FF", border=0, font="Inter 9 ")
        self.cod.place(relx=0.5, y=215, anchor="n")
        self.linha2 = Frame(self.frame_direita, width=163, height=1, bg="white")
        self.linha2.place(relx=0.5, y=235, anchor="n")

        fonte = ('Montserrat', 15)
        # Botão
        self.bot = CTkButton(self.frame_direita, width=130, corner_radius=15, text="Criar", fg_color='#4833DA',
                             hover_color='white', font=fonte, command=self.abrir_main)
        self.bot.place(relx=0.5, y=255, anchor="n")





if __name__ == "__main__":
    janela = Tk()
    app = Login(janela)
    janela.mainloop()

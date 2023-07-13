from tkinter import Tk, Entry, Label, Frame, PhotoImage, messagebox
from customtkinter import *
from Banco_Dados.admin import Register
class Admin:
    def __init__(self, janela):
        self.config(janela)
        self.layout(janela)
        self.db = Register()

    def config(self, janela):
        self.janela = janela
        self.janela.title("Administrador")
        self.janela.resizable(False, False)

        largura = 500
        altura = 350
        largura_screen = self.janela.winfo_screenwidth()
        altura_screen = self.janela.winfo_screenheight()
        pos_x = (largura_screen - largura) // 2
        pos_y = (altura_screen - altura) // 2
        self.janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

    def criar(self):
        senha_admin = self.admin.get()
        user = self.user.get()
        key = self.cod.get()
        id_user = self.id.get()
        dados = (user, key, id_user)
        key_admin = "12345"

        if senha_admin == key_admin:
            self.db.cadastrar(dados)

            self.user.delete(0, 'end')
            self.cod.delete(0, 'end')
            self.admin.delete(0, 'end')
            self.id.delete(0, 'end')

        elif senha_admin == '':
            messagebox.showinfo('Erro', 'Preencha a senha do Administrador!')


        elif user == '':
            messagebox.showinfo('Erro', 'Preencha o nome do funcionário!')

        elif key == '':
            messagebox.showinfo('Erro', 'Preencha a senha do funcionário!')

        elif id_user == '':
            messagebox.showinfo('Erro', 'Preencha o R.A do funcionário!')

        else:
            messagebox.showinfo('Erro', 'Senha do Administrador incorreta!')


    def layout(self, janela):
        self.frame_dir = Frame(janela, width='250', height='350', bg='white')
        self.frame_dir.grid(row=0, column=1)

        img = PhotoImage(file='../image/5.png')
        img_label = Label(self.frame_dir, image=img, bg="white")
        img_label.place(x=35, y=100)
        img_label.image = img

        # Frame esquerda
        self.frame_esq = Frame(janela, width='250', height='350', bg='#8C52FF')
        self.frame_esq.grid(row=0, column=0)

        self.lb = Label(self.frame_esq, text="Administrador", font=("Montserrat 18"), bg='#8C52FF', foreground="white")
        self.lb.place(relx=0.5, y=15, anchor="n")

        # Label_Admin
        label_admin = Label(self.frame_esq, anchor='nw', text="Senha do Admin *:", bg='#8C52FF',
                         font=('MontserratSemiBold 10 '), fg="white")
        label_admin.place(x=40, y=75)

        # Entry_Admin
        self.admin = Entry(self.frame_esq, width=20, fg="white", bg="#8C52FF", border=0, font="Inter 9")
        self.admin.place(relx=0.5, y=95, anchor="n")
        self.linha3 = Frame(self.frame_esq, width=163, height=1, bg="white")
        self.linha3.place(relx=0.5, y=115, anchor="n")

        # Label_Usuário
        label_user = Label(self.frame_esq, anchor='nw', text="Novo Funcionário *:", bg='#8C52FF',
                           font=('MontserratSemiBold 10 '), fg="white")
        label_user.place(x=40, y=135)

        # Entry_Usuário
        self.user = Entry(self.frame_esq, width=20, fg="white", bg="#8C52FF", border=0, font="Inter 9")
        self.user.place(relx=0.5, y=155, anchor="n")
        self.linha = Frame(self.frame_esq, width=163, height=1, bg="white")
        self.linha.place(relx=0.5, y=175, anchor="n")

        # Label_Senha
        label_senha = Label(self.frame_esq, anchor='nw', text="Senha do Funcionário *:", bg='#8C52FF',
                            font=('MontserratSemiBold 10'), fg="white")
        label_senha.place(x=40, y=195)

        # Entry_senha
        self.cod = Entry(self.frame_esq, width=20, fg="white", bg="#8C52FF", border=0, font="Inter 9 ")
        self.cod.place(relx=0.5, y=215, anchor="n")
        self.linha2 = Frame(self.frame_esq, width=163, height=1, bg="white")
        self.linha2.place(relx=0.5, y=235, anchor="n")

        # Label_id
        label_senha = Label(self.frame_esq, anchor='nw', text="R.A do Funcionário *:", bg='#8C52FF',
                            font=('MontserratSemiBold 10'), fg="white")
        label_senha.place(x=40, y=255)

        # Entry_id
        self.id = Entry(self.frame_esq, width=20, fg="white", bg="#8C52FF", border=0, font="Inter 9 ")
        self.id.place(relx=0.5, y=275, anchor="n")
        self.linha5 = Frame(self.frame_esq, width=163, height=1, bg="white")
        self.linha5.place(relx=0.5, y=295, anchor="n")

        fonte = ('Montserrat', 15)

        # Botão
        self.bot = CTkButton(self.frame_esq, width=130, corner_radius=15, text="Criar", fg_color='#4833DA',
                             hover_color='white', font=fonte, command=self.criar)
        self.bot.place(relx=0.5, y=315, anchor="n")


if __name__ == '__main__':
    janela = Tk()
    app = Admin(janela)
    janela.mainloop()

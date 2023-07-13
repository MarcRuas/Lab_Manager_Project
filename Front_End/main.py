from Back_End.relatorio_main import *
from Back_End.funcs_main import *

class App(Funcs, Relatorio):
    def __init__(self, janela):
        self.db = Database()

        self.config(janela)
        self.create_frames(janela)
        self.create_btn()
        self.create_widgets()
        self.create_treeview()

        self.janela = janela
        self.Menus()

    def config(self, janela):
        self.janela = janela
        self.janela.title("LabManager")
        self.janela.resizable(False, False)

        # Dimensionamento e Resolução
        largura = 800
        altura = 530
        largura_screen = self.janela.winfo_screenwidth()
        altura_screen = self.janela.winfo_screenheight()
        pos_x = (largura_screen - largura) // 2
        pos_y = (altura_screen - altura) // 2
        self.janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
        style = Style(janela)
        style.theme_use("clam")

    def create_frames(self, janela):
        # Frame Logo---------------------------------------------------------------------------------------------
        self.frame_logo = tk.Frame(janela, width=850, height=45, bg='#4833DA')
        self.frame_logo.grid(row=0, column=0, padx=0, pady=0, sticky=tk.NSEW, columnspan=6)

        # Frame esquerdo
        self.frame_esquerdo = tk.Frame(janela, width=100, height=200, background='white', relief='raised')
        self.frame_esquerdo.grid(row=1, column=0, padx=5, pady=5, sticky=tk.NSEW)

        # Frame direito
        self.frame_direito = tk.Frame(janela, width=500, height=225, background='white', relief='solid')
        self.frame_direito.grid(row=1, column=1, pady=5, padx=5, sticky='NSEW')

        # Frame usuario
        self.frame_user = tk.Frame(janela, width=125, height=200, background='white', relief='solid')
        self.frame_user.grid(row=1, column=2, pady=3, padx=5, sticky='NSEW')

        # Frame Tree View
        self.frame_tabela = tk.Frame(janela, width=800, height=100, bg='white', relief='solid')
        self.frame_tabela.grid(row=3, column=0, pady=5, padx=5, sticky='NSEW', columnspan=5)

    def create_btn(self):
        fonte = ('Montserrat', 15)
        self.l_nome = Label(self.frame_esquerdo, text="Procurar [ ID ]", height=1, anchor='center',
                            font=('Ivy 10 bold'), bg='white',
                            fg='#403d3d')
        self.l_nome.place(relx=0.5, y=20, anchor='n')
        self.e_procurar = Entry(self.frame_esquerdo, width=10, justify='center', relief="solid", font=('Ivy 10'))
        self.e_procurar.place(relx=0.5, y=60, anchor='n')

        self.botao_procurar = CTkButton(self.frame_esquerdo, width=15, fg_color='#4833DA', font=fonte,
                                        bg_color='white', text="Pesquisar", command=self.procurar_dados)
        self.botao_procurar.place(relx=0.5, y=90, anchor='n')

        self.btn_adicionar = CTkButton(self.frame_direito, text="Adicionar", width=15, fg_color='#4833DA', font=fonte,
                                        bg_color='white', command=self.adicionar_dados)
        self.btn_adicionar.place(x=4, y=190)

        self.btn_atualizar = CTkButton(self.frame_direito, text="Atualizar", width=15, fg_color='#4833DA', font=fonte,
                                        bg_color='white', command=self.atualizar)
        self.btn_atualizar.place(x=104, y=190)

        self.btn_remover = CTkButton(self.frame_direito, text="Remover", width=15, fg_color='#4833DA', font=fonte,
                                        bg_color='white', command=self.apagar)
        self.btn_remover.place(x=204, y=190)

        self.btn_limpar = CTkButton(self.frame_direito, text="Limpar", width=15, fg_color='#4833DA', font=fonte,
                                    bg_color='white', command=self.limpar)
        self.btn_limpar.place(x=304, y=190)

    def create_widgets(self):
        # Titulo - Lab Manager
        self.title = tk.Label(self.frame_logo, text="Lab Manager", font=("Montserrat 22"), bg='#4833DA',
                              foreground="white")
        self.title.place(x=5, y=0)

        self.equipamento = Label(self.frame_direito, text='Equipamentos *:', anchor='nw', font=('Ivy 10'),
                                 fg='#403d3d', bg='white')
        self.equipamento.place(x=4, y=10)
        self.equipamento_entry = Entry(self.frame_direito, width=20, justify='left', relief='solid')
        self.equipamento_entry.place(x=7, y=40)

        self.codigo_label = tk.Label(self.frame_direito, text="Código *:", anchor='nw', font=('Ivy 10'),
                                     fg='#403d3d', bg='white')
        self.codigo_label.place(x=4, y=70)
        self.codigo_entry = tk.Entry(self.frame_direito, width=20, justify='left', relief='solid')
        self.codigo_entry.place(x=7, y=100)

        self.fornecedor_label = tk.Label(self.frame_direito, text="Fornecedor *:", anchor='nw', font=('Ivy 10'),
                                         fg='#403d3d', bg='white')
        self.fornecedor_label.place(x=4, y=130)
        self.fornecedor_entry = tk.Entry(self.frame_direito, width=20, justify='left', relief='solid')
        self.fornecedor_entry.place(x=7, y=160)

        self.status_label = tk.Label(self.frame_direito, text="Status *:", anchor='nw', font=('Ivy 10'),
                                     fg='#403d3d', bg='white')
        self.status_label.place(x=150, y=130)
        self.status_entry = ttk.Combobox(self.frame_direito, width=12, font=('Ivy 7 bold'), justify='center')
        self.status_entry['values'] = ('Disponível', 'Indisponível')
        self.status_entry.place(x=153, y=160)

        self.linha = tk.Frame(self.frame_direito, width=500, height=1, bg="black")
        self.linha.place(x=260, y=184, anchor="n")

        self.l_data_inicio = Label(self.frame_direito, text="Data de Inicio *:", anchor='nw', font=('Ivy 10'),
                                   bg='white',
                                   fg='#403d3d')
        self.l_data_inicio.place(x=220, y=10)
        self.data_inicio = DateEntry(self.frame_direito, width=18, justify='center', background='darkblue',
                                     foreground='white', borderwidth=2, year=2023)
        self.data_inicio.place(x=224, y=40)

        self.l_data_fim = Label(self.frame_direito, text="Data Final *:", anchor='nw', font=('Ivy 10'),
                                bg='white',
                                fg='#403d3d')
        self.l_data_fim.place(x=370, y=10)
        self.data_fim = DateEntry(self.frame_direito, width=18, justify='center', background='darkblue',
                                  foreground='white', borderwidth=2, year=2023)
        self.data_fim.place(x=374, y=40)

        self.data_inicio.delete(0, 'end')
        self.data_fim.delete(0, 'end')

        self.responsavel_label = tk.Label(self.frame_user, text="Responsável *:", anchor='nw', font=('Ivy 10'),
                                          fg='#403d3d', bg='white')
        self.responsavel_label.place(x=4, y=5)
        self.responsavel_entry = tk.Entry(self.frame_user, width=20, justify='left', relief='solid')
        self.responsavel_entry.place(x=7, y=35)

        self.ra_label = tk.Label(self.frame_user, text="R.A *:", anchor='nw', font=('Ivy 10'),
                                 fg='#403d3d', bg='white')
        self.ra_label.place(x=4, y=65)
        self.ra_entry = tk.Entry(self.frame_user, width=20, justify='left', relief='solid')
        self.ra_entry.place(x=7, y=95)

        self.email_label = tk.Label(self.frame_user, text="E-mail *:", anchor='nw', font=('Ivy 10'),
                                    fg='#403d3d', bg='white')
        self.email_label.place(x=4, y=125)
        self.email_entry = tk.Entry(self.frame_user, width=20, justify='left', relief='solid')
        self.email_entry.place(x=7, y=155)

        self.telefone_label = tk.Label(self.frame_user, text="Telefone *:", anchor='nw', font=('Ivy 10'),
                                    fg='#403d3d', bg='white')
        self.telefone_label.place(x=4, y=185)
        self.telefone_entry = tk.Entry(self.frame_user, width=20, justify='left', relief='solid')
        self.telefone_entry.place(x=7, y=205)

    def create_treeview(self):
        list_header = ['id', 'Equipamento', 'Código', 'Fornecedor', 'Status', 'Início', 'Fim', 'Responsável', 'E-mail', 'R.A', 'Telefone']
        df_list = self.db.get_all_data()  # Obter os dados do banco de dados
        self.tree = ttk.Treeview(self.frame_tabela, selectmode="extended", columns=list_header, show="headings")

        vsb = ttk.Scrollbar(self.frame_tabela, orient="vertical", command=self.tree.yview)
        # horizontal scrollbar
        hsb = ttk.Scrollbar(self.frame_tabela, orient="horizontal", command=self.tree.xview)

        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        self.frame_tabela.grid_rowconfigure(0, weight=12)

        hd = ["nw", "nw", "nw", "center", "center", "center", "center", "center", "center", 'center', 'center']
        h = [40, 100, 70, 70, 70, 70, 75, 90, 70, 50, 65]
        n = 0

        for col in list_header:
            self.tree.heading(col, text=col.title(), anchor='nw')
            self.tree.column(col, width=h[n], anchor=hd[n])

            n += 1

        for item in df_list:
            self.tree.insert('', 'end', values=item)

        self.tree.bind("<Double-1>", self.double)

    def Menus(self):

        menubar = Menu(self.janela)
        self.janela.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)
        filemenu3 = Menu(menubar)

        menubar.add_cascade(label="Opções", menu=filemenu)
        menubar.add_cascade(label="Relatório", menu=filemenu2)
        menubar.add_cascade(label="E-mail", menu=filemenu3)

        filemenu.add_command(label="Sobre", command=self.sobre)
        filemenu.add_command(label="Sair", command=self.close)
        filemenu2.add_command(label="Relatório - PDF", command=self.relatorio)
        filemenu2.add_command(label="Relatório - Excel", command=self.exportar_excel)
        filemenu3.add_command(label="Enviar E-mail", command=self.enviar_email)

    def close(self):
        self.db.close()
        self.janela.destroy()

if __name__ == '__main__':
    janela = tk.Tk()
    app = App(janela)
    janela.protocol("WM_DELETE_WINDOW", app.close)
    janela.mainloop()

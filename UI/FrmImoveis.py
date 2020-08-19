
from tkinter import Tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import lib.ColumnListview as multiList
import os

class FrmImoveis():

    def on_imo_select(self, data):
        print("called command when row is selected")
        print(data)
        print("\n")

    def janela_imovel(self):
        if self.jan == None:
            self.padInY = 5
            self.entryWidth = 58

            self.jan = Tk()

            self.jan.protocol("WM_DELETE_WINDOW", self.fecha_janela)
            self.janFrame = Frame(self.jan)
            self.janFrame.pack(side=LEFT, fill=X, anchor=NW, expand=True)

            self.lfJanelaDados = LabelFrame(self.janFrame, text="Dados")
            self.lfJanelaDados.pack(fill=X, anchor=NW, padx=3, pady=3)

            self.lfJanelaBtns = LabelFrame(self.janFrame)
            self.lfJanelaBtns.pack(fill=X, anchor=NW, padx=3, pady=3)

            self.l1 = Label(self.lfJanelaDados, text="Nome:").grid(row=0, sticky=W, padx=5, pady=self.padInY)
            self.e1 = Entry(self.lfJanelaDados, width=self.entryWidth).grid(row=0, column=1)

            self.l2 = Label(self.lfJanelaDados, text="Telefone 1:").grid(row=1, sticky=W, padx=5, pady=self.padInY)
            self.e2 = Entry(self.lfJanelaDados, width=self.entryWidth).grid(row=1, column=1)

            self.l3 = Label(self.lfJanelaDados, text="Telefone 2:").grid(row=2, sticky=W, padx=5, pady=self.padInY)
            self.e3 = Entry(self.lfJanelaDados, width=self.entryWidth).grid(row=2, column=1)

            self.l4 = Label(self.lfJanelaDados, text="CPF:").grid(row=3, sticky=W, padx=5, pady=self.padInY)
            self.e4 = Entry(self.lfJanelaDados, width=self.entryWidth).grid(row=3, column=1)

            self.l5 = Label(self.lfJanelaDados, text="E-mail:").grid(row=4, sticky=W, padx=5, pady=self.padInY)
            self.e5 = Entry(self.lfJanelaDados, width=self.entryWidth).grid(row=4, column=1)

            self.l6 = Label(self.lfJanelaDados, text="Observação:").grid(row=5, sticky=NW, padx=5, pady=self.padInY)
            self.t1 = Text(self.lfJanelaDados, height=5, width=15).grid(row=5, column=1, padx=1, pady=self.padInY,
                                                                        stick=W + E)

            self.btnSalvar = Button(self.lfJanelaBtns, text="Salvar", width=10).pack(anchor=NW, padx=5, pady=5,
                                                                                     side=LEFT)
            self.btnCancel = Button(self.lfJanelaBtns, text="Cancelar", width=10, command=self.fecha_janela).pack(
                anchor=NW, padx=5, pady=5, side=LEFT)

            self.jan.geometry("520x344+200+200")
            self.jan.title("Imovel")
            self.jan.iconbitmap(os.path.dirname(__file__) + '/../images/icon.ico')
            self.jan.resizable(0, 0)
        else:
            self.jan.lift()

    def fecha_janela(self):
        if self.jan != None:
            self.jan.destroy()
            self.jan = None

    def __init__(self, conteudoFrame):

        self.filtroImovel = IntVar()

        self.jan = None

        self.frame = Frame(conteudoFrame)
        self.frame.pack(fill=BOTH, expand=TRUE)
        self.frame.propagate(0)



        #FRAME TÍTULO

        '''self.lfTitulo = LabelFrame(self.frame)
        self.lfTitulo.pack(anchor=NW, fill=X, padx=5, pady=5)

        self.frameTitulo = Frame(self.lfTitulo)
        self.frameTitulo.pack(fill=X, anchor=NW, padx=3, pady=3)
        self.labelTitulo = Label(self.frameTitulo, text="PROPRIETARIOS", font="Arial 20")
        self.labelTitulo.pack(anchor=NW)'''

        #FRAME PARA FILTRO E PESQUISA
        self.frameOpc = Frame(self.frame)
        self.frameOpc.pack(anchor=NW, fill=X)


        '''
        #FRAME PESQUISA
        self.lfPesquisa = LabelFrame(self.frameOpc, text="Pesquisa")
        self.lfPesquisa.pack(anchor=NW, padx=5, pady=5, side=LEFT)

        self.framePesquisa = Frame(self.lfPesquisa)
        self.framePesquisa.pack(anchor=NW, padx=3, pady=3, side=BOTTOM)



        self.framePesquisaBtn = Frame(self.framePesquisa)
        self.framePesquisaBtn.pack(anchor=NE, side=BOTTOM, pady=5)

        self.labelPesquisa = Label(self.lfPesquisa, text="Tipo de pesquisa").pack(anchor=NW, side=TOP)

        self.pesquisaCombobox = ttk.Combobox(self.framePesquisa, values=["Código", "Nome"], width=8)
        self.pesquisaCombobox.pack(anchor=NW, side=LEFT, padx=5)
        self.pesquisaCombobox.current(0)

        self.pesquisaEntry = Entry(self.framePesquisa, width=35)
        self.pesquisaEntry.pack(anchor=NW, side=LEFT, padx=5)

        self.pesquisaBtn = Button(self.framePesquisaBtn, text="Pesquisar",command=print("oi"))
        self.pesquisaBtn.pack(anchor=NE, padx=5)
        '''

        # FRAME FILTRAR
        self.lfPesquisa = LabelFrame(self.frameOpc, text="Filtrar")
        self.lfPesquisa.pack(anchor=NW, padx=5, pady=5, side=LEFT)

        self.radioTodos = Radiobutton(self.lfPesquisa, text="Mostrar todos os imóveis", variable=self.filtroImovel ,value=0)
        self.radioTodos.pack(anchor=NW, padx=5, pady=2, side=LEFT)

        self.radioAlugados = Radiobutton(self.lfPesquisa, text="Mostrar imóveis Alugados", variable=self.filtroImovel, value=1)
        self.radioAlugados.pack(anchor=NW, padx=5, pady=2, side=LEFT)

        self.radioDesalugado = Radiobutton(self.lfPesquisa, text="Mostrar imóveis Disponíveis", variable=self.filtroImovel, value=2)
        self.radioDesalugado.pack(anchor=NW, padx=5, pady=2, side=LEFT)
        '''
        self.framePesquisa = Frame(self.lfPesquisa)
        self.framePesquisa.pack(anchor=NW, padx=3, pady=3, side=BOTTOM)

        self.framePesquisaBtn = Frame(self.framePesquisa)
        self.framePesquisaBtn.pack(anchor=NE, side=BOTTOM, pady=5)

        self.labelPesquisa = Label(self.lfPesquisa, text="Tipo de pesquisa").pack(anchor=NW, side=TOP)

        self.pesquisaCombobox = ttk.Combobox(self.framePesquisa, values=["Código", "Nome"], width=8)
        self.pesquisaCombobox.pack(anchor=NW, side=LEFT, padx=5)
        self.pesquisaCombobox.current(0)

        self.pesquisaEntry = Entry(self.framePesquisa, width=35)
        self.pesquisaEntry.pack(anchor=NW, side=LEFT, padx=5)

        self.pesquisaBtn = Button(self.framePesquisaBtn, text="Pesquisar", command=print("oi"))
        self.pesquisaBtn.pack(anchor=NE, padx=5)
        '''

        #FRAME PROPRIETARIOS MULTILIST

        self.lfInqs = LabelFrame(self.frame, text="Imoveis")
        self.lfInqs.pack(anchor=NW, fill=X, padx=5, pady=5)

        self.frameInquilinos = Frame(self.lfInqs, bd=3, relief=SUNKEN)
        self.frameInquilinos.pack(anchor=NW, fill=X, pady=5, padx=5)

        self.inqMc = multiList.Multicolumn_Listbox(self.frameInquilinos,
                                                   ["Código",
                                                    "Proprietário",
                                                    "Logadouro",
                                                    "Número",
                                                    "Bairro",
                                                    "Cidade",
                                                    "UF",
                                                    "nº Companhia Elétrica",
                                                    "nº Companhia Sanitária",
                                                    "Observação do Imóvel"
                                                    ], stripped_rows=("black", "#f2f2f2"),
                                 command=self.on_imo_select, cell_anchor="w", heading_anchor=W)

        self.verscrollbar = ttk.Scrollbar(self.frameInquilinos, orient="vertical", command=self.inqMc.interior.yview)

        self.xScrollBar = ttk.Scrollbar(self.frameInquilinos, orient="horizontal", command=self.inqMc.interior.xview)

        self.verscrollbar.pack(side="right", fill="y")
        self.xScrollBar.pack(side="bottom", fill=X)

        #propMc.interior.columnconfigure()
        self.inqMc.interior.config(yscrollcommand=self.verscrollbar.set, xscrollcommand=self.xScrollBar.set)



        self.inqMc.interior.pack(fill=X, expand=True)



        #FRAME BOTÕES
        self.lfBtns = LabelFrame(self.frame)
        self.lfBtns.pack(anchor=NW, fill=X, padx=5, pady=5)

        self.frameButton = Frame(self.lfBtns)
        self.frameButton.pack(anchor=NW, padx=5, pady=5, fill=X)


        self.button_novo = Button(self.frameButton, text="Novo", command=self.janela_imovel)
        self.button_novo.pack(side=LEFT, padx=5)

        self.button_editar = Button(self.frameButton, text="Alterar")
        self.button_editar.pack(side=LEFT, padx=5)

        self.button_excluir = Button(self.frameButton, text="Excluir")
        self.button_excluir.pack(side=LEFT, padx=5)




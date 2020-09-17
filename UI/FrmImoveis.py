
from tkinter import Tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import lib.ColumnListview as multiList
import os

class FrmImoveis():

    def on_select(self, data):
        self.selecionado = data[0]

    def on_imo_select(self, data):
        print("called command when row is selected")
        print(data)
        print("\n")

    def janela_imovel(self):
        if self.jan == None:

            self.padInY = 5
            self.entryWidth = 58

            self.jan = Toplevel()

            #Variáveis de controle
            self.ufSelect = StringVar(self.jan)
            self.ufSelect.set("SP")

            self.OptionList = ["Código", "Nome"]

            self.tipoPesquisa = StringVar(self.jan)
            self.tipoPesquisa.set(self.OptionList[0])

            #Fim variáveis de controle

            self.jan.protocol("WM_DELETE_WINDOW", self.fecha_janela)
            self.janFrame = Frame(self.jan)
            self.janFrame.pack(side=LEFT, fill=X, anchor=NW, expand=True)

            self.lfJanelaDados = LabelFrame(self.janFrame)
            self.lfJanelaDados.pack(fill=X, anchor=NW, padx=3, pady=3)

            self.lfJanelaBtns = LabelFrame(self.janFrame)
            self.lfJanelaBtns.pack(fill=X, anchor=NW, padx=3, pady=3)

            #Coluna proprietario

            self.frameContratos = LabelFrame(self.lfJanelaDados, text="Proprietário")
            self.frameContratos.pack(anchor=NW, fill=X, pady=5, padx=5)

            # FRAME PESQUISA
            self.lfPesquisa = LabelFrame(self.frameContratos, text="Pesquisar Proprietário:")
            self.lfPesquisa.pack(anchor=NW, padx=5, pady=5)

            self.framePesquisa = Frame(self.lfPesquisa)
            self.framePesquisa.pack(anchor=NW, padx=3, pady=3, side=LEFT)

            self.labelPesquisa = Label(self.framePesquisa, text="Tipo:")
            self.labelPesquisa.pack(anchor=NW, side=LEFT, pady=5)

            self.opTipo = OptionMenu(self.framePesquisa, self.tipoPesquisa, *self.OptionList)
            self.opTipo.pack(anchor=NW, side=LEFT)

            self.pesquisaEntry = Entry(self.framePesquisa, width=35)
            self.pesquisaEntry.pack(anchor=NW, side=LEFT, padx=5, pady=5)

            self.framePesquisaBtn = Frame(self.framePesquisa)
            self.framePesquisaBtn.pack(anchor=NE, side=LEFT)

            self.pesquisaBtn = Button(self.framePesquisaBtn, text="Pesquisar", command=print("oi"))
            self.pesquisaBtn.pack(anchor=NE, padx=5, side=LEFT)

            self.frameProprietarios = LabelFrame(self.frameContratos, text="Selecione o Proprietário:")
            self.frameProprietarios.pack(anchor=NW, fill=X, pady=5, padx=5)

            self.propMcn = multiList.Multicolumn_Listbox(self.frameProprietarios, [
                "Código",
                "Nome do proprietário",
                "Endereço",
                "Telefone 1",
                "Telefone 2",
                "E-mail",
                "Observações"
            ], stripped_rows=("black", "#f2f2f2"),
                                                         command=self.on_select, cell_anchor="w", heading_anchor=W,
                                                         height=7)

            self.propMcn.configure_column(0, stretch=False, minwidth=65, width=65)
            self.propMcn.configure_column(1, stretch=False, minwidth=200, width=200)
            self.propMcn.configure_column(2, stretch=False, minwidth=250, width=250)
            self.propMcn.configure_column(3, stretch=False, minwidth=85, width=85)
            self.propMcn.configure_column(4, stretch=False, minwidth=85, width=85)
            self.propMcn.configure_column(5, stretch=False, minwidth=85, width=85)
            self.propMcn.configure_column(6, stretch=False, minwidth=450, width=450)

            self.verscrollbar = ttk.Scrollbar(self.frameProprietarios, orient="vertical",
                                              command=self.propMcn.interior.yview)

            self.xScrollBar = ttk.Scrollbar(self.frameProprietarios, orient="horizontal",
                                            command=self.propMcn.interior.xview)

            self.verscrollbar.pack(side="right", fill="y")
            self.xScrollBar.pack(side="bottom", fill=X)

            # propMc.interior.columnconfigure()
            self.propMcn.interior.config(yscrollcommand=self.verscrollbar.set, xscrollcommand=self.xScrollBar.set)

            self.propMcn.interior.pack(fill=X, expand=True)
            #FIM SELECIONA PROPRIETARIO

            #Linha1
            self.fLinha1 = Frame(self.lfJanelaDados)
            self.fLinha1.pack(anchor=NW, fill=X, padx=5, pady=5)

            #Logadouro
            self.lfLog = LabelFrame(self.fLinha1, text="Logadrouro:")
            self.lfLog.pack(anchor=NW, padx=5, side=LEFT)
            self.eLog = Entry(self.lfLog, width=60)
            self.eLog.pack(anchor=NW, padx=5, pady=5, side=LEFT)

            #Numero
            self.lfNum = LabelFrame(self.fLinha1, text="Número:")
            self.lfNum.pack(anchor=NW, padx=5, side=LEFT)
            self.eNum = Entry(self.lfNum, width=15)
            self.eNum.pack(anchor=NW, padx=5, pady=5, side=LEFT)

            # Linha2
            self.fLinha2 = Frame(self.lfJanelaDados)
            self.fLinha2.pack(anchor=NW, fill=X, padx=5, pady=5)

            # Complemento
            self.lfComp = LabelFrame(self.fLinha2, text="Complemento:")
            self.lfComp.pack(anchor=NW, padx=5, side=LEFT)
            self.eComp = Entry(self.lfComp, width=85)
            self.eComp.pack(anchor=NW, padx=5, pady=5, side=LEFT)

            # Linha3
            self.fLinha3 = Frame(self.lfJanelaDados)
            self.fLinha3.pack(anchor=NW, fill=X, padx=5, pady=5)

            # Bairro
            self.lfBairro = LabelFrame(self.fLinha3, text="Bairro:")
            self.lfBairro.pack(anchor=NW, padx=5, side=LEFT)
            self.eBairro = Entry(self.lfBairro, width=40)
            self.eBairro.pack(anchor=NW, padx=5, pady=5, side=LEFT)

            # Cidade
            self.lfCidade = LabelFrame(self.fLinha3, text="Cidade:")
            self.lfCidade.pack(anchor=NW, padx=5, side=LEFT)
            self.eCidade = Entry(self.lfCidade, width=25)
            self.eCidade.pack(anchor=NW, padx=5, pady=5, side=LEFT)

            # Unidade Federativa
            self.lfUF= LabelFrame(self.fLinha3, text="UF:")
            self.lfUF.pack(anchor=NW, padx=5, side=LEFT)
            self.opUF = OptionMenu(self.lfUF, self.ufSelect, "SP", "AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR", "RJ", "RN", "RS", "RO", "RR", "SC", "SE", "TO")
            self.opUF.pack(anchor=NW, side=LEFT)

            # Linha4
            self.fLinha4 = Frame(self.lfJanelaDados)
            self.fLinha4.pack(anchor=NW, fill=X, padx=5, pady=5)

            # Bairro
            self.lfObs = LabelFrame(self.fLinha4, text="Observação:")
            self.lfObs.pack(anchor=NW, padx=5, side=LEFT)
            self.eObs = Entry(self.lfObs, width=85)
            self.eObs.pack(anchor=NW, padx=5, pady=5, side=LEFT)

            #FIM DADOS DO IMÓVEL

            self.btnSalvar = Button(self.lfJanelaBtns, text="Salvar", width=10).pack(anchor=NW, padx=5, pady=5,
                                                                                     side=LEFT)
            self.btnCancel = Button(self.lfJanelaBtns, text="Cancelar", width=10, command=self.fecha_janela).pack(
                anchor=NW, padx=5, pady=5, side=LEFT)

            self.jan.geometry("600x630+200+200")
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
        self.selecionado = None

        self.filtroImovel = IntVar()

        self.jan = None

        self.frame = Frame(conteudoFrame)
        self.frame.pack(fill=BOTH, expand=TRUE)
        self.frame.propagate(0)

        #FRAME PARA FILTRO E PESQUISA
        self.frameOpc = Frame(self.frame)
        self.frameOpc.pack(anchor=NW, fill=X)

        # FRAME FILTRAR
        self.lfPesquisa = LabelFrame(self.frameOpc, text="Filtrar")
        self.lfPesquisa.pack(anchor=NW, padx=5, pady=5, side=LEFT)

        self.radioTodos = Radiobutton(self.lfPesquisa, text="Mostrar todos os imóveis", variable=self.filtroImovel ,value=0)
        self.radioTodos.pack(anchor=NW, padx=5, pady=2, side=LEFT)

        self.radioAlugados = Radiobutton(self.lfPesquisa, text="Mostrar imóveis Alugados", variable=self.filtroImovel, value=1)
        self.radioAlugados.pack(anchor=NW, padx=5, pady=2, side=LEFT)

        self.radioDesalugado = Radiobutton(self.lfPesquisa, text="Mostrar imóveis Disponíveis", variable=self.filtroImovel, value=2)
        self.radioDesalugado.pack(anchor=NW, padx=5, pady=2, side=LEFT)

        #FRAME PROPRIETARIOS MULTILIST

        self.lfInqs = LabelFrame(self.frame, text="Imoveis")
        self.lfInqs.pack(anchor=NW, fill=X, padx=5, pady=5)

        self.frameInquilinos = Frame(self.lfInqs, bd=3, relief=SUNKEN)
        self.frameInquilinos.pack(anchor=NW, fill=X, pady=5, padx=5)

        self.inqMc = multiList.Multicolumn_Listbox(self.frameInquilinos,
                                                   ["Código",
                                                    "Proprietário",
                                                    "Logadrouro",
                                                    "Número",
                                                    "Complemento",
                                                    "CEP",
                                                    "Bairro",
                                                    "Cidade",
                                                    "UF",
                                                    "Observação do Imóvel"
                                                    ], stripped_rows=("black", "#f2f2f2"),
                                 command=self.on_imo_select, cell_anchor="w", heading_anchor=W)
        self.inqMc.configure_column(0, stretch=False, minwidth=65, width=65)
        self.inqMc.configure_column(1, stretch=False, minwidth=200, width=200)
        self.inqMc.configure_column(2, stretch=False, minwidth=250, width=250)
        self.inqMc.configure_column(3, stretch=False, minwidth=65, width=65)
        self.inqMc.configure_column(4, stretch=False, minwidth=200, width=200)
        self.inqMc.configure_column(5, stretch=False, minwidth=80, width=80)
        self.inqMc.configure_column(6, stretch=False, minwidth=200, width=200)
        self.inqMc.configure_column(7, stretch=False, minwidth=120, width=120)
        self.inqMc.configure_column(8, stretch=False, minwidth=30, width=30)
        self.inqMc.configure_column(9, stretch=True, minwidth=550, width=550)

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


        self.button_novo = Button(self.frameButton, text="Novo Imovel", command=self.janela_imovel)
        self.button_novo.pack(side=LEFT, padx=5)

        self.button_editar = Button(self.frameButton, text="Alterar Imovel")
        self.button_editar.pack(side=LEFT, padx=5)

        self.button_excluir = Button(self.frameButton, text="Excluir Imovel")
        self.button_excluir.pack(side=LEFT, padx=5)

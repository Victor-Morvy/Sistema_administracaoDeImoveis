from tkinter import Tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import lib.ColumnListview as multiList
import os

class FrmContas():

    def on_select(self, data):
        print("called command when row is selected")
        print(data)
        print("\n")

    def janela_conta(self):
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

            self.l2 = Label(self.lfJanelaDados, text="Endereço:").grid(row=1, sticky=W, padx=5, pady=self.padInY)
            self.e2 = Entry(self.lfJanelaDados, width=self.entryWidth).grid(row=1, column=1)

            self.l2 = Label(self.lfJanelaDados, text="Telefone 1:").grid(row=2, sticky=W, padx=5, pady=self.padInY)
            self.e2 = Entry(self.lfJanelaDados, width=self.entryWidth).grid(row=2, column=1)

            self.l3 = Label(self.lfJanelaDados, text="Telefone 2:").grid(row=3, sticky=W, padx=5, pady=self.padInY)
            self.e3 = Entry(self.lfJanelaDados, width=self.entryWidth).grid(row=3, column=1)

            self.l4 = Label(self.lfJanelaDados, text="CPF:").grid(row=4, sticky=W, padx=5, pady=self.padInY)
            self.e4 = Entry(self.lfJanelaDados, width=self.entryWidth).grid(row=4, column=1)

            self.l5 = Label(self.lfJanelaDados, text="E-mail:").grid(row=5, sticky=W, padx=5, pady=self.padInY)
            self.e5 = Entry(self.lfJanelaDados, width=self.entryWidth).grid(row=5, column=1)

            self.l6 = Label(self.lfJanelaDados, text="Observação:").grid(row=6, sticky=NW, padx=5, pady=self.padInY)
            self.t1 = Text(self.lfJanelaDados, height=5, width=15).grid(row=6, column=1, padx=1, pady=self.padInY, stick=W+E)

            self.btnSalvar = Button(self.lfJanelaBtns, text="Salvar", width=10).pack(anchor=NW, padx=5, pady=5, side=LEFT)
            self.btnCancel = Button(self.lfJanelaBtns, text="Cancelar", width=10, command=self.fecha_janela).pack(anchor=NW, padx=5, pady=5, side=LEFT)

            self.jan.geometry("520x377+200+200")
            self.jan.title("Proprietário")
            self.jan.iconbitmap(os.path.dirname(__file__) + '/../images/icon.ico')
            self.jan.resizable(0, 0)
        else:
            self.jan.lift()

    def fecha_janela(self):
        if self.jan != None:
            self.jan.destroy()
            self.jan = None

    def __init__(self, conteudoFrame):

        self.filtroConta = IntVar()

        self.jan = None

        self.frame = Frame(conteudoFrame)
        self.frame.pack(fill=BOTH, expand=TRUE)
        self.frame.propagate(0)



        #FRAME TÍTULO

        '''self.lfTitulo = LabelFrame(self.frame)
        self.lfTitulo.pack(anchor=NW, fill=X, padx=5, pady=5)

        self.frameTitulo = Frame(self.lfTitulo)
        self.frameTitulo.pack(fill=X, anchor=NW, padx=3, pady=3)
        self.labelTitulo = Label(self.frameTitulo, text="Contratos", font="Arial 20")
        self.labelTitulo.pack(anchor=NW)'''

        #FRAME PESQUISA
        '''
        self.lfPesquisa = LabelFrame(self.frame, text="Pesquisa")
        self.lfPesquisa.pack(anchor=NW, padx=5, pady=5)

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

        #FRAME Contratos MULTILIST

        self.lfProps = LabelFrame(self.frame, text="Contratos")
        self.lfProps.pack(anchor=NW, fill=X, padx=5, pady=5)

        self.frameContratos = Frame(self.lfProps, bd=3, relief=SUNKEN)
        self.frameContratos.pack(anchor=NW, fill=X, pady=5, padx=5)

        self.propMc = multiList.Multicolumn_Listbox(self.frameContratos, [
            "Código",
            "Nome do proprietário",
            "Nome do Inquilino",
            "Status",
            "Endereço do imóvel",
            "Data Inicial",
            "Data Final",
            "Valor",
            "Garantia",
            "Observações"
        ], stripped_rows=("black", "#f2f2f2"),
                                 command=self.on_select, cell_anchor="w", heading_anchor=W, height=9)

        self.verscrollbar = ttk.Scrollbar(self.frameContratos, orient="vertical", command=self.propMc.interior.yview)

        self.xScrollBar = ttk.Scrollbar(self.frameContratos, orient="horizontal", command=self.propMc.interior.xview)

        self.verscrollbar.pack(side="right", fill="y")
        self.xScrollBar.pack(side="bottom", fill=X)

        #propMc.interior.columnconfigure()
        self.propMc.interior.config(yscrollcommand=self.verscrollbar.set, xscrollcommand=self.xScrollBar.set)



        self.propMc.interior.pack(fill=X, expand=True)

        '''

        #FRAME BOTÕES
        self.lfBtns = LabelFrame(self.frame)
        self.lfBtns.pack(anchor=NW, fill=X, padx=5, pady=5)

        self.frameButton = Frame(self.lfBtns)
        self.frameButton.pack(anchor=NW, padx=5, pady=5, fill=X)


        self.button_novo = Button(self.frameButton, text="Novo Contrato", command=self.janela_conta)
        self.button_novo.pack(side=LEFT, padx=5)

        self.button_editar = Button(self.frameButton, text="Alterar Contrato")
        self.button_editar.pack(side=LEFT, padx=5)

        self.button_excluir = Button(self.frameButton, text="Excluir Contrato")
        self.button_excluir.pack(side=LEFT, padx=5)
        '''

        # FRAME PARA FILTRO E PESQUISA
        self.frameOpc = Frame(self.frame)
        self.frameOpc.pack(anchor=NW, fill=X)

        # FRAME FILTRAR
        self.lfPesquisa = LabelFrame(self.frameOpc, text="Filtrar Pagamentos")
        self.lfPesquisa.pack(anchor=NW, padx=5, pady=5, side=LEFT, fill=X, expand=TRUE)

        self.radioTodos = Radiobutton(self.lfPesquisa, text="Mostrar todas as contas", variable=self.filtroConta,
                                      value=0)
        self.radioTodos.pack(anchor=NW, padx=5, pady=2, side=LEFT)

        self.radioAlugados = Radiobutton(self.lfPesquisa, text="Mostrar contas em aberto", variable=self.filtroConta,
                                         value=1)
        self.radioAlugados.pack(anchor=NW, padx=5, pady=2, side=LEFT)

        self.radioDesalugado = Radiobutton(self.lfPesquisa, text="Mostrar contas pagas",
                                           variable=self.filtroConta, value=2)
        self.radioDesalugado.pack(anchor=NW, padx=5, pady=2, side=LEFT)

        # FRAME CONTAS VINCULADAS MULTILIST

        self.lfProps2 = LabelFrame(self.frame, text="Resumo de Pagamentos")
        self.lfProps2.pack(anchor=NW, fill=X, padx=5, pady=5)

        self.labelExplica = Label(self.lfProps2, text="*Selecione um contrato para exibir as contas vinculadas", font="Verdana 9", fg="red")
        self.labelExplica.pack(anchor=NW, padx=5, pady=5)

        self.frameContratos2 = Frame(self.lfProps2, bd=3, relief=SUNKEN)
        self.frameContratos2.pack(anchor=NW, fill=X, pady=5, padx=5)

        self.propMc2 = multiList.Multicolumn_Listbox(self.frameContratos2, [
            "Código",
            "Tipo",
            "Dia do Vencimento",
            "Status",
            "Observações"
        ], stripped_rows=("black", "#f2f2f2"),
                                                    command=self.on_select, cell_anchor="w", heading_anchor=W, height=8)

        self.verscrollbar2 = ttk.Scrollbar(self.frameContratos2, orient="vertical", command=self.propMc2.interior.yview)

        self.xScrollBar2 = ttk.Scrollbar(self.frameContratos2, orient="horizontal", command=self.propMc2.interior.xview)

        self.verscrollbar2.pack(side="right", fill="y")
        self.xScrollBar2.pack(side="bottom", fill=X)

        # propMc.interior.columnconfigure()
        self.propMc2.interior.config(yscrollcommand=self.verscrollbar2.set, xscrollcommand=self.xScrollBar2.set)

        self.propMc2.interior.pack(fill=X, expand=True)

        # FRAME BOTÕES
        self.lfBtns2 = LabelFrame(self.frame)
        self.lfBtns2.pack(anchor=NW, fill=X, padx=5, pady=5)

        self.frameButton2 = Frame(self.lfBtns2)
        self.frameButton2.pack(anchor=NW, padx=5, pady=5, fill=X)

        self.button_novo2 = Button(self.frameButton2, text="Confirmar Envio", command=self.janela_conta)
        self.button_novo2.pack(side=LEFT, padx=5)

        self.button_editar2 = Button(self.frameButton2, text="Confirmar Pagamento")
        self.button_editar2.pack(side=LEFT, padx=5)






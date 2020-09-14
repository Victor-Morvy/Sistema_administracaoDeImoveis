from tkinter import Tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import lib.ColumnListview as multiList
import os
from lib.funcoes import *


class FrmContas():

    def on_select(self, data):
        self.selecionado = data[0]

    def janela_pagamento(self):
        if self.jan == None:

            self.padInY = 5
            self.entryWidth = 58

            self.jan = Tk()

            self.validate = self.jan.register(validate_entry)

            # self.entt = validEntry.Valid_Entry(self.jan, 2)

            self.jan.protocol("WM_DELETE_WINDOW", self.fecha_janela)
            self.janFrame = Frame(self.jan)
            self.janFrame.pack(side=LEFT, fill=X, anchor=NW, expand=True)

            ##ENVIO
            self.lfJanelaDados = LabelFrame(self.janFrame, text=("Data do pagamento:"))
            self.lfJanelaDados.pack(fill=X, anchor=NW, padx=3, pady=3)

            self.diaIni = Entry(self.lfJanelaDados, width=3, validate="key", validatecommand=(self.validate, "%P", 2))
            self.diaIni.pack(anchor=NW, padx=5, pady=5, side=LEFT)
            self.diaIni.focus_set()

            self.labelBarra = Label(self.lfJanelaDados, text="/")
            self.labelBarra.pack(anchor=NW, side=LEFT)

            self.mesIni = Entry(self.lfJanelaDados, width=3, validate="key", validatecommand=(self.validate, "%P", 2))
            self.mesIni.pack(anchor=NW, padx=5, pady=5, side=LEFT)

            self.labelBarra = Label(self.lfJanelaDados, text="/")
            self.labelBarra.pack(anchor=NW, side=LEFT)

            self.anoIni = Entry(self.lfJanelaDados, width=5, validate="key", validatecommand=(self.validate, "%P", 4))
            self.anoIni.pack(anchor=NW, padx=5, pady=5, side=LEFT)

            # observacao
            self.lfObs = LabelFrame(self.janFrame, text=("Observação:"))
            self.lfObs.pack(fill=X, anchor=NW, padx=3, pady=3)
            self.eObs = Entry(self.lfObs, width=50)
            self.eObs.pack(anchor=NW, padx=5, pady=5, side=LEFT)

            ##FIM ENVIO
            self.lfJanelaBtns = LabelFrame(self.janFrame)
            self.lfJanelaBtns.pack(fill=X, anchor=NW, padx=3, pady=3)
            self.btnSalvar = Button(self.lfJanelaBtns, text="Salvar", width=10).pack(anchor=NW, padx=5, pady=5,
                                                                                     side=LEFT)
            self.btnCancel = Button(self.lfJanelaBtns, text="Cancelar", width=10, command=self.fecha_janela).pack(
                anchor=NW, padx=5, pady=5, side=LEFT)

            # self.jan.geometry("250x112+200+200")
            self.jan.title("Pagamento")
            self.jan.iconbitmap(os.path.dirname(__file__) + '/../images/icon.ico')
            self.jan.resizable(0, 0)

            self.jan.lift()
        else:
            self.fecha_janela()

    def janela_conta(self):

        if self.jan == None:

            self.padInY = 5
            self.entryWidth = 58

            self.jan = Tk()

            # tipo de conta
            self.tipoList = ["ALUGUEL", "ÁGUA", "ENERGIA"]

            self.tipoConta = StringVar(self.jan)
            self.tipoConta.set(self.tipoList[0])

            self.validate = self.jan.register(validate_entry)

            #self.entt = validEntry.Valid_Entry(self.jan, 2)

            self.jan.protocol("WM_DELETE_WINDOW", self.fecha_janela)
            self.janFrame = Frame(self.jan)
            self.janFrame.pack(side=LEFT, fill=X, anchor=NW, expand=True)

            #LINHA 1
            self.frameL1 = Frame(self.janFrame)
            self.frameL1.pack(anchor=NW, padx=3, pady=3)

            #data envio
            self.lfJanelaDados = LabelFrame(self.frameL1, text=("Data de envio:"))
            self.lfJanelaDados.pack(fill=X, anchor=NW, padx=3, pady=3, side=LEFT)

            self.diaIni = Entry(self.lfJanelaDados, width=3, validate="key", validatecommand=(self.validate, "%P", 2))
            self.diaIni.pack(anchor=NW, padx=5, pady=5, side=LEFT)
            self.diaIni.focus_set()

            self.labelBarra = Label(self.lfJanelaDados, text="/")
            self.labelBarra.pack(anchor=NW, side=LEFT)

            self.mesIni = Entry(self.lfJanelaDados, width=3, validate="key", validatecommand=(self.validate, "%P", 2))
            self.mesIni.pack(anchor=NW, padx=5, pady=5, side=LEFT)

            self.labelBarra = Label(self.lfJanelaDados, text="/")
            self.labelBarra.pack(anchor=NW, side=LEFT)

            self.anoIni = Entry(self.lfJanelaDados, width=5, validate="key", validatecommand=(self.validate, "%P", 4))
            self.anoIni.pack(anchor=NW, padx=5, pady=5, side=LEFT)

            # data vencimento

            self.lfJanelaVenci = LabelFrame(self.frameL1, text=("Data de vencimento:"))
            self.lfJanelaVenci.pack(fill=X, anchor=NW, padx=3, pady=3, side=LEFT)

            self.diaVenci = Entry(self.lfJanelaVenci, width=3, validate="key", validatecommand=(self.validate, "%P", 2))
            self.diaVenci.pack(anchor=NW, padx=5, pady=5, side=LEFT)

            self.labelBarra2 = Label(self.lfJanelaVenci, text="/")
            self.labelBarra2.pack(anchor=NW, side=LEFT)

            self.mesVenci = Entry(self.lfJanelaVenci, width=3, validate="key", validatecommand=(self.validate, "%P", 2))
            self.mesVenci.pack(anchor=NW, padx=5, pady=5, side=LEFT)

            self.labelBarra2 = Label(self.lfJanelaVenci, text="/")
            self.labelBarra2.pack(anchor=NW, side=LEFT)

            self.anoVenci = Entry(self.lfJanelaVenci, width=5, validate="key", validatecommand=(self.validate, "%P", 4))
            self.anoVenci.pack(anchor=NW, padx=5, pady=5, side=LEFT)

            # LINHA 2
            self.frameL2 = Frame(self.janFrame)
            self.frameL2.pack(anchor=NW, padx=3, pady=3)

            #mes ref
            self.lfMesRef = LabelFrame(self.frameL2, text=("Mês Ref.:"))
            self.lfMesRef.pack(fill=X, anchor=NW, padx=3, pady=3, side=LEFT)
            self.mesRef = Entry(self.lfMesRef, width=5, validate="key", validatecommand=(self.validate, "%P", 2))
            self.mesRef.pack(anchor=NW, padx=5, pady=5, side=LEFT)

            #tipo conta (select_box)
            self.lfTipo = LabelFrame(self.frameL2, text=("Tipo de conta:"))
            self.lfTipo.pack(fill=X, anchor=NW, padx=3, pady=3, side=LEFT)

            self.opTipo = OptionMenu(self.lfTipo, self.tipoConta, *self.tipoList)
            self.opTipo.pack(anchor=NW, side=LEFT)

            #valor
            self.lfValor = LabelFrame(self.frameL2, text=("Valor:"))
            self.lfValor.pack(fill=X, anchor=NW, padx=3, pady=3, side=LEFT)

            self.brl = Label(self.lfValor, text="R$")
            self.brl.pack(anchor=NW, side=LEFT, pady=5)

            self.eValAluguel = Entry(self.lfValor, width=10)
            self.eValAluguel.pack(anchor=NW, padx=5, pady=5, side=LEFT)

            self.brl = Label(self.lfValor, text=",00")
            self.brl.pack(anchor=NW, side=LEFT, pady=5)

            # LINHA 3
            self.frameL3 = Frame(self.janFrame)
            self.frameL3.pack(anchor=NW, padx=3, pady=3)

            #observacao
            self.lfObs = LabelFrame(self.frameL3, text=("Observação:"))
            self.lfObs.pack(fill=X, anchor=NW, padx=3, pady=3, side=LEFT)
            self.eObs = Entry(self.lfObs, width=50)
            self.eObs.pack(anchor=NW, padx=5, pady=5, side=LEFT)

            # LINHA 4
            self.frameL4 = Frame(self.janFrame)
            self.frameL4.pack(anchor=NW, padx=3, pady=3)

            #Botoes
            self.lfJanelaBtns = LabelFrame(self.frameL4)
            self.lfJanelaBtns.pack(fill=X, anchor=NW, padx=3, pady=3, side=LEFT)

            self.btnSalvar = Button(self.lfJanelaBtns, text="Salvar", width=10).pack(anchor=NW, padx=5, pady=5, side=LEFT)
            self.btnCancel = Button(self.lfJanelaBtns, text="Cancelar", width=10, command=self.fecha_janela).pack(anchor=NW, padx=5, pady=5, side=LEFT)

            #self.jan.geometry("250x112+200+200")
            self.jan.title("Confirmirme a conta")
            self.jan.iconbitmap(os.path.dirname(__file__) + '/../images/icon.ico')
            self.jan.resizable(0, 0)
        else:
            self.fecha_janela()

    def fecha_janela(self):

        if self.jan != None:
            self.jan.destroy()
            self.jan = None

    def __init__(self, conteudoFrame):
        self.selecionado = None

        self.filtroConta = IntVar()

        self.jan = None

        self.frame = Frame(conteudoFrame)
        self.frame.pack(fill=BOTH, expand=TRUE)
        self.frame.propagate(0)

        #FRAME Contratos MULTILIST

        self.lfProps = LabelFrame(self.frame, text="Contratos")
        self.lfProps.pack(anchor=NW, fill=X, padx=5, pady=5)

        self.frameContratos = Frame(self.lfProps, bd=3, relief=SUNKEN)
        self.frameContratos.pack(anchor=NW, fill=X, pady=5, padx=5)

        self.propMc = multiList.Multicolumn_Listbox(self.frameContratos, [
            "Código",
            "Status",
            "Nome do proprietário",
            "Nome do Inquilino",
            "Endereço do imóvel",
            "Data Inicial",
            "Data Final",
            "Valor",
            "Garantia",
            "Observações"
        ], stripped_rows=("black", "#f2f2f2"),
                                 command=self.on_select, cell_anchor="w", heading_anchor=W, height=9)

        self.propMc.configure_column(0, stretch=False, minwidth=65, width=65)
        self.propMc.configure_column(1, stretch=False, minwidth=140, width=140)
        self.propMc.configure_column(2, stretch=False, minwidth=200, width=200)
        self.propMc.configure_column(3, stretch=False, minwidth=200, width=200)
        self.propMc.configure_column(4, stretch=False, minwidth=450, width=450)
        self.propMc.configure_column(5, stretch=False, minwidth=100, width=100)
        self.propMc.configure_column(6, stretch=False, minwidth=100, width=100)
        self.propMc.configure_column(7, stretch=False, minwidth=100, width=100)
        self.propMc.configure_column(8, stretch=False, minwidth=75, width=75)
        self.propMc.configure_column(9, stretch=True, minwidth=450, width=450)

        self.verscrollbar = ttk.Scrollbar(self.frameContratos, orient="vertical", command=self.propMc.interior.yview)

        self.xScrollBar = ttk.Scrollbar(self.frameContratos, orient="horizontal", command=self.propMc.interior.xview)

        self.verscrollbar.pack(side="right", fill="y")
        self.xScrollBar.pack(side="bottom", fill=X)

        #propMc.interior.columnconfigure()
        self.propMc.interior.config(yscrollcommand=self.verscrollbar.set, xscrollcommand=self.xScrollBar.set)

        self.propMc.interior.pack(fill=X, expand=True)

        # FRAME CONTAS VINCULADAS MULTILIST

        self.lfProps2 = LabelFrame(self.frame, text="Resumo de Pagamentos")
        self.lfProps2.pack(anchor=NW, fill=X, padx=5, pady=5)

        self.labelExplica = Label(self.lfProps2, text="*Selecione um contrato para exibir as contas vinculadas",
                                  font="Verdana 9", fg="red")
        self.labelExplica.pack(anchor=NW, padx=5, pady=5)

        # FRAME PARA FILTRO E PESQUISA
        self.frameOpc = Frame(self.lfProps2)
        self.frameOpc.pack(anchor=NW, fill=X)

        # FRAME FILTRAR
        self.lfPesquisa = LabelFrame(self.frameOpc, text="Filtrar Pagamentos")
        self.lfPesquisa.pack(anchor=NW, padx=5, pady=5, side=LEFT, fill=X, expand=TRUE)

        self.radioTodos = Radiobutton(self.lfPesquisa, text="Mostrar contas em aberto", variable=self.filtroConta,
                                      value=0)
        self.radioTodos.pack(anchor=NW, padx=5, pady=2, side=LEFT)

        self.radioAlugados = Radiobutton(self.lfPesquisa, text="Mostrar todas as contas", variable=self.filtroConta,
                                         value=1)
        self.radioAlugados.pack(anchor=NW, padx=5, pady=2, side=LEFT)

        self.radioDesalugado = Radiobutton(self.lfPesquisa, text="Mostrar contas pagas",
                                           variable=self.filtroConta, value=2)
        self.radioDesalugado.pack(anchor=NW, padx=5, pady=2, side=LEFT)

        # CONTINUA FRAME CONTAS VINCULADAS MULTILIST

        self.frameContratos2 = Frame(self.lfProps2, bd=3, relief=SUNKEN)
        self.frameContratos2.pack(anchor=NW, fill=X, pady=5, padx=5)

        self.propMc2 = multiList.Multicolumn_Listbox(self.frameContratos2, [
            "Tipo", #Não existe código pois ele funciona de acordo com as entidades conta_vinculada e conta_paga
            "Número de Referência",
            "Valor",
            "Mês de Referência",
            "Data do Vencimento",
            "Data de Envio",
            "Data do Pagamento",
            "Observações"
        ], stripped_rows=("black", "#f2f2f2"),
                                                    command=self.on_select, cell_anchor="w", heading_anchor=W, height=8)

        self.propMc2.configure_column(0, stretch=False, minwidth=150, width=150)
        self.propMc2.configure_column(1, stretch=False, minwidth=150, width=150)
        self.propMc2.configure_column(2, stretch=False, minwidth=100, width=100)
        self.propMc2.configure_column(3, stretch=False, minwidth=130, width=130)
        self.propMc2.configure_column(4, stretch=False, minwidth=130, width=130)
        self.propMc2.configure_column(5, stretch=False, minwidth=130, width=130)
        self.propMc2.configure_column(6, stretch=False, minwidth=130, width=130)
        self.propMc2.configure_column(7, stretch=True, minwidth=450, width=450)

        self.verscrollbar2 = ttk.Scrollbar(self.frameContratos2, orient="vertical", command=self.propMc2.interior.yview)

        self.xScrollBar2 = ttk.Scrollbar(self.frameContratos2, orient="horizontal", command=self.propMc2.interior.xview)

        self.verscrollbar2.pack(side="right", fill="y")
        self.xScrollBar2.pack(side="bottom", fill=X)

        # propMc.interior.columnconfigure()
        self.propMc2.interior.config(yscrollcommand=self.verscrollbar2.set, xscrollcommand=self.xScrollBar2.set)

        self.propMc2.interior.pack(fill=X, expand=True)

        # FRAME BOTÕES
        self.lfBtns2 = LabelFrame(self.lfProps2)
        self.lfBtns2.pack(anchor=NW, fill=X, padx=5, pady=5)

        self.frameButton2 = Frame(self.lfBtns2)
        self.frameButton2.pack(anchor=NW, padx=5, pady=5, fill=X)

        self.button_novo2 = Button(self.frameButton2, text="Confirmar Envio", command=self.janela_conta)
        self.button_novo2.pack(side=LEFT, padx=5)

        self.button_editar2 = Button(self.frameButton2, text="Confirmar Pagamento", command=self.janela_pagamento)
        self.button_editar2.pack(side=LEFT, padx=5)

        self.button_novo3 = Button(self.frameButton2, text="Editar Envio")
        self.button_novo3.pack(side=LEFT, padx=5)

        self.button_editar3 = Button(self.frameButton2, text="Editar Pagamento")
        self.button_editar3.pack(side=LEFT, padx=5)

        self.button_exclui = Button(self.frameButton2, text="Excluir Conta Selecionada")
        self.button_exclui.pack(side=LEFT, padx=5)
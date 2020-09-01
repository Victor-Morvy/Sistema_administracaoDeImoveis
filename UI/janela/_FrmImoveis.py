from tkinter import Tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import lib.ColumnListview as multiList
import os
from lib.ValidEntry import validate_entry

class JanImoveis():

    def __init__(self):
        if self.jan == None:


            self.padInY = 5
            self.entryWidth = 58

            self.jan = Tk()

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

            # FRAME PROPRIETARIOS


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


            '''
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
                                                                        stick=W + E)'''

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
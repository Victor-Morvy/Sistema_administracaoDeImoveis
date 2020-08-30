import os
from tkinter import *
from tkinter import ttk
import lib.ColumnListview as multiList
from lib.ValidEntry import validate_entry

class FrmContrato():

    def on_select(self, data):
        print("called command when row is selected")
        print(data)
        print("\n")

    def janela_proprietario(self):
        if self.jan == None:

            self.padInY = 5
            self.entryWidth = 58

            self.jan = Tk()
            self.validate = self.jan.register(validate_entry)

            # Variáveis de controle


            self.OptionListGarantia = ["CALÇÃO", "FIADOR", "OUTRO"]

            self.OptionList = ["Código", "Nome"]

            self.OptionListImo = ["Código", "Proprietário"]

            self.tipoGarantia = StringVar(self.jan)
            self.tipoGarantia.set(self.OptionListGarantia[0])

            self.tipoPesquisa = StringVar(self.jan)
            self.tipoPesquisa.set(self.OptionList[0])

            self.tipoPesquisaImo = StringVar(self.jan)
            self.tipoPesquisaImo.set(self.OptionListImo[0])

            # Fim variáveis de controle

            self.jan.protocol("WM_DELETE_WINDOW", self.fecha_janela)
            self.janFrame = Frame(self.jan)
            self.janFrame.pack(side=LEFT, fill=X, anchor=NW, expand=True)

            self.lfJanelaDados = LabelFrame(self.janFrame)
            self.lfJanelaDados.pack(fill=X, anchor=NW, padx=3, pady=3)

            self.lfJanelaBtns = LabelFrame(self.janFrame)
            self.lfJanelaBtns.pack(fill=X, anchor=NW, padx=3, pady=3)

            # Coluna proprietario

            # FRAME PROPRIETARIOS

            self.frameContratos = LabelFrame(self.lfJanelaDados, text="Inquilino")
            self.frameContratos.pack(anchor=NW, fill=X, pady=5, padx=5)

            # FRAME PESQUISA
            self.lfPesquisa = LabelFrame(self.frameContratos, text="Pesquisar Inquilino:")
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

            self.frameProprietarios = LabelFrame(self.frameContratos, text="Selecione o Inquilino:")
            self.frameProprietarios.pack(anchor=NW, fill=X, pady=5, padx=5)

            self.propMcn = multiList.Multicolumn_Listbox(self.frameProprietarios, [
                "Código",
                "Nome do inquilino",
                "Telefone 1",
                "Telefone 2",
                "E-mail",
                "Observações"
            ], stripped_rows=("black", "#f2f2f2"),
             command=self.on_select, cell_anchor="w", heading_anchor=W,
             height=3)

            self.propMcn.configure_column(0, stretch=False, minwidth=65, width=65)
            self.propMcn.configure_column(1, stretch=False, minwidth=200, width=200)
            self.propMcn.configure_column(2, stretch=False, minwidth=85, width=85)
            self.propMcn.configure_column(3, stretch=False, minwidth=85, width=85)
            self.propMcn.configure_column(4, stretch=False, minwidth=85, width=85)
            self.propMcn.configure_column(5, stretch=False, minwidth=450, width=450)

            self.verscrollbar = ttk.Scrollbar(self.frameProprietarios, orient="vertical",
                                              command=self.propMcn.interior.yview)

            self.xScrollBar = ttk.Scrollbar(self.frameProprietarios, orient="horizontal",
                                            command=self.propMcn.interior.xview)

            self.verscrollbar.pack(side="right", fill="y")
            self.xScrollBar.pack(side="bottom", fill=X)

            # propMc.interior.columnconfigure()
            self.propMcn.interior.config(yscrollcommand=self.verscrollbar.set, xscrollcommand=self.xScrollBar.set)

            self.propMcn.interior.pack(fill=X, expand=True)
            # FIM SELECIONA PROPRIETARIO

            ##########FRAME Imóvel#################
            # FRAME PROPRIETARIOS

            self.frameContratos2 = LabelFrame(self.lfJanelaDados, text="Imóvel")
            self.frameContratos2.pack(anchor=NW, fill=X, pady=5, padx=5)

            # FRAME PESQUISA
            self.lfPesquisa2 = LabelFrame(self.frameContratos2, text="Pesquisar Imóvel:")
            self.lfPesquisa2.pack(anchor=NW, padx=5, pady=5)

            self.framePesquisa2 = Frame(self.lfPesquisa2)
            self.framePesquisa2.pack(anchor=NW, padx=3, pady=3, side=LEFT)

            self.labelPesquisa2 = Label(self.framePesquisa2, text="Tipo:")
            self.labelPesquisa2.pack(anchor=NW, side=LEFT, pady=5)

            self.opTipo2 = OptionMenu(self.framePesquisa2, self.tipoPesquisaImo, *self.OptionListImo)
            self.opTipo2.pack(anchor=NW, side=LEFT)

            self.pesquisaEntry2 = Entry(self.framePesquisa2, width=35)
            self.pesquisaEntry2.pack(anchor=NW, side=LEFT, padx=5, pady=5)

            self.framePesquisaBtn2 = Frame(self.framePesquisa2)
            self.framePesquisaBtn2.pack(anchor=NE, side=LEFT)

            self.pesquisaBtn2 = Button(self.framePesquisaBtn2, text="Pesquisar", command=print("oi"))
            self.pesquisaBtn2.pack(anchor=NE, padx=5, side=LEFT)

            self.frameProprietarios2 = LabelFrame(self.frameContratos2, text="Selecione o Imóvel:")
            self.frameProprietarios2.pack(anchor=NW, fill=X, pady=5, padx=5)

            self.propMcn2 = multiList.Multicolumn_Listbox(self.frameProprietarios2, [
                "Código",
                "Proprietário",
                "Logadouro",
                "Número",
                "Complemento",
                "Bairro",
                "Cidade",
                "UF",
                "Observação do Imóvel"
            ], stripped_rows=("black", "#f2f2f2"),
                                                         command=self.on_select, cell_anchor="w", heading_anchor=W,
                                                         height=3)

            self.propMcn2.configure_column(0, stretch=False, minwidth=65, width=65)
            self.propMcn2.configure_column(1, stretch=False, minwidth=200, width=200)
            self.propMcn2.configure_column(2, stretch=False, minwidth=250, width=250)
            self.propMcn2.configure_column(3, stretch=False, minwidth=65, width=65)
            self.propMcn2.configure_column(4, stretch=False, minwidth=200, width=200)
            self.propMcn2.configure_column(5, stretch=False, minwidth=200, width=200)
            self.propMcn2.configure_column(6, stretch=False, minwidth=120, width=120)
            self.propMcn2.configure_column(7, stretch=False, minwidth=30, width=30)
            self.propMcn2.configure_column(8, stretch=True, minwidth=550, width=550)

            self.verscrollbar2 = ttk.Scrollbar(self.frameProprietarios2, orient="vertical",
                                              command=self.propMcn2.interior.yview)

            self.xScrollBar2 = ttk.Scrollbar(self.frameProprietarios2, orient="horizontal",
                                            command=self.propMcn2.interior.xview)

            self.verscrollbar2.pack(side="right", fill="y")
            self.xScrollBar2.pack(side="bottom", fill=X)

            # propMc.interior.columnconfigure()
            self.propMcn2.interior.config(yscrollcommand=self.verscrollbar2.set, xscrollcommand=self.xScrollBar2.set)

            self.propMcn2.interior.pack(fill=X, expand=True)
            # FIM SELECIONA PROPRIETARIO



            #############################


            # Linha1
            self.fLinha1 = Frame(self.lfJanelaDados)
            self.fLinha1.pack(anchor=NW, fill=X, padx=5, pady=5)

            # DataInicial

            self.dataIni = LabelFrame(self.fLinha1, text="Data Inicial:")
            self.dataIni.pack(anchor=NW, padx=5, side=LEFT)

            self.diaIni = Entry(self.dataIni, width=3, validate="key", validatecommand=(self.validate, "%P", 2))
            self.diaIni.pack(anchor=NW, padx=5, pady=5, side=LEFT)

            self.labelBarra = Label(self.dataIni, text="/")
            self.labelBarra.pack(anchor=NW, side=LEFT)

            self.mesIni = Entry(self.dataIni, width=3, validate="key", validatecommand=(self.validate, "%P", 2))
            self.mesIni.pack(anchor=NW, padx=5, pady=5, side=LEFT)

            self.labelBarra = Label(self.dataIni, text="/")
            self.labelBarra.pack(anchor=NW, side=LEFT)

            self.anoIni = Entry(self.dataIni, width=5, validate="key", validatecommand=(self.validate, "%P", 4))
            self.anoIni.pack(anchor=NW, padx=5, pady=5, side=LEFT)

            # DataFinal


            self.dataFim = LabelFrame(self.fLinha1, text="Data Final:")
            self.dataFim.pack(anchor=NW, padx=5, side=LEFT)

            self.diaFim = Entry(self.dataFim, width=3, validate="key", validatecommand=(self.validate, "%P", 2))
            self.diaFim.pack(anchor=NW, padx=5, pady=5, side=LEFT)

            self.labelBarra = Label(self.dataFim, text="/")
            self.labelBarra.pack(anchor=NW, side=LEFT)

            self.mesFim = Entry(self.dataFim, width=3, validate="key", validatecommand=(self.validate, "%P", 2))
            self.mesFim.pack(anchor=NW, padx=5, pady=5, side=LEFT)

            self.labelBarra = Label(self.dataFim, text="/")
            self.labelBarra.pack(anchor=NW, side=LEFT)

            self.anoFim = Entry(self.dataFim, width=5, validate="key", validatecommand=(self.validate, "%P", 4))
            self.anoFim.pack(anchor=NW, padx=5, pady=5, side=LEFT)

            #DIA PGTO
            self.diaPgto = LabelFrame(self.fLinha1, text="Dia Pgto.:")
            self.diaPgto.pack(anchor=NW, padx=5, side=LEFT)

            self.eDiaPgto = Entry(self.diaPgto, width=3, validate="key", validatecommand=(self.validate, "%P", 2))
            self.eDiaPgto.pack(padx=5, pady=5, side=LEFT)

            #NUM CONTA DE ÁGUA
            self.lfContaAgua = LabelFrame(self.fLinha1, text="Número de Conta de Água:")
            self.lfContaAgua.pack(anchor=NW, padx=5, side=LEFT)

            self.eContaAgua = Entry(self.lfContaAgua, width=30)
            self.eContaAgua.pack(padx=5, pady=5, side=LEFT)

            # Linha2
            self.fLinha2 = Frame(self.lfJanelaDados)
            self.fLinha2.pack(anchor=NW, fill=X, padx=5, pady=5)

            # VALOR ALUGUEL
            self.valAluguel = LabelFrame(self.fLinha2, text="Valor do aluguel:")
            self.valAluguel.pack(anchor=NW, padx=5, side=LEFT)

            self.brl = Label(self.valAluguel, text="R$")
            self.brl.pack(anchor=NW, side=LEFT, pady=5)

            self.eValAluguel = Entry(self.valAluguel, width=10)
            self.eValAluguel.pack(anchor=NW, padx=5, pady=5, side=LEFT)

            self.brl = Label(self.valAluguel, text=",00")
            self.brl.pack(anchor=NW, side=LEFT, pady=5)

            #% de administração
            self.porcAdmin = LabelFrame(self.fLinha2, text="Admin.:")
            self.porcAdmin.pack(anchor=NW, padx=5, side=LEFT)

            self.ePorAdmin = Entry(self.porcAdmin, width=3)
            self.ePorAdmin.pack(anchor=NW, padx=5, pady=5, side=LEFT)

            self.lPorc = Label(self.porcAdmin, text="%")
            self.lPorc.pack(anchor=NW, side=LEFT, pady=5)

            # Garantia
            self.lfComp = LabelFrame(self.fLinha2, text="Garantia:")
            self.lfComp.pack(anchor=NW, padx=5, side=LEFT)

            self.opGarantia = OptionMenu(self.lfComp, self.tipoGarantia, *self.OptionListGarantia)
            self.opGarantia.pack(anchor=NW, side=LEFT)

            # NUM CONTA DE Energia
            self.lfContaEnergia = LabelFrame(self.fLinha2, text="Número de Conta de Energia:")
            self.lfContaEnergia.pack(anchor=NW, padx=5, side=LEFT)

            self.eContaEnergia = Entry(self.lfContaEnergia, width=46)
            self.eContaEnergia.pack(padx=5, pady=5, side=LEFT)



            # Linha3
            self.fLinha3 = Frame(self.lfJanelaDados)
            self.fLinha3.pack(anchor=NW, fill=X, padx=5, pady=5)

            # VALOR ALUGUEL
            self.obsContrato = LabelFrame(self.fLinha3, text="Observação:")
            self.obsContrato.pack(anchor=NW, padx=5, side=LEFT)

            self.eObs = Entry(self.obsContrato, width=80)
            self.eObs.pack(anchor=NW, padx=5, pady=5, side=LEFT)


            # FIM DADOS DO IMÓVEL

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

            self.jan.geometry("600x720+200+200")
            self.jan.title("Contrato")
            self.jan.iconbitmap(os.path.dirname(__file__) + '/../images/icon.ico')
            self.jan.resizable(0, 0)
        else:
            self.jan.lift()

    def fecha_janela(self):
        if self.jan != None:
            self.jan.destroy()
            self.jan = None

    def __init__(self, conteudoFrame):

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
            "Endereço do imóvel",
            "Data Inicial",
            "Data Final",
            "Valor",
            "% Adm.",
            "Valor Adm.",
            "Garantia",
            "Observações"
        ], stripped_rows=("black", "#f2f2f2"),
                                 command=self.on_select, cell_anchor="w", heading_anchor=W, height=18)

        self.verscrollbar = ttk.Scrollbar(self.frameContratos, orient="vertical", command=self.propMc.interior.yview)

        self.xScrollBar = ttk.Scrollbar(self.frameContratos, orient="horizontal", command=self.propMc.interior.xview)

        self.verscrollbar.pack(side="right", fill="y")
        self.xScrollBar.pack(side="bottom", fill=X)

        #propMc.interior.columnconfigure()
        self.propMc.interior.config(yscrollcommand=self.verscrollbar.set, xscrollcommand=self.xScrollBar.set)



        self.propMc.interior.pack(fill=X, expand=True)



        #FRAME BOTÕES
        self.lfBtns = LabelFrame(self.lfProps)
        self.lfBtns.pack(anchor=NW, fill=X, padx=5, pady=5)

        self.frameButton = Frame(self.lfBtns)
        self.frameButton.pack(anchor=NW, padx=5, pady=5, fill=X)


        self.button_novo = Button(self.frameButton, text="Novo Contrato", command=self.janela_proprietario)
        self.button_novo.pack(side=LEFT, padx=5)

        self.button_editar = Button(self.frameButton, text="Alterar Contrato")
        self.button_editar.pack(side=LEFT, padx=5)

        self.button_excluir = Button(self.frameButton, text="Excluir Contrato")
        self.button_excluir.pack(side=LEFT, padx=5)

        self.button_exibir_dados_imovel = Button(self.frameButton, text="Exibir Detalhes do Imóvel")
        self.button_exibir_dados_imovel.pack(side=LEFT, padx=5)

        # FRAME CONTAS VINCULADAS MULTILIST
        '''
        self.lfProps2 = LabelFrame(self.frame, text="Contas Vinculadas")
        self.lfProps2.pack(anchor=NW, fill=X, padx=5, pady=5)

        self.labelExplica = Label(self.lfProps2, text="*Selecione um contrato para exibir as contas vinculadas", font="Verdana 9", fg="red")
        self.labelExplica.pack(anchor=NW, padx=5, pady=5)

        self.frameContratos2 = Frame(self.lfProps2, bd=3, relief=SUNKEN)
        self.frameContratos2.pack(anchor=NW, fill=X, pady=5, padx=5)

        self.propMc2 = multiList.Multicolumn_Listbox(self.frameContratos2, [
            "Código",
            "Tipo",
            "Dia do pagamento",
            "Observações"
        ], stripped_rows=("black", "#f2f2f2"),
                                                    command=self.on_select, cell_anchor="w", heading_anchor=W, height=5)

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

        self.button_novo2 = Button(self.frameButton2, text="Vincular Conta ao Contrato", command=self.janela_proprietario)
        self.button_novo2.pack(side=LEFT, padx=5)

        self.button_editar2 = Button(self.frameButton2, text="Alterar Conta do Contrato")
        self.button_editar2.pack(side=LEFT, padx=5)

        self.button_excluir2 = Button(self.frameButton2, text="Excluir Conta do Contrato")
        self.button_excluir2.pack(side=LEFT, padx=5)
        '''




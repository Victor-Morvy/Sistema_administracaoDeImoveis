from tkinter import Tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import os
import UI.FrmInquilino as frmInq
import UI.FrmProprietario as frmProp
import UI.FrmImoveis as frmImo
import UI.FrmContrato as frmContrato
import UI.FrmContas as frmContas
import UI.Inicio as pagInicial
import lib.ColumnListview as multiList
from lib.ValidEntry import validate_entry

conteudoFrame = None
selectedModulo = "INICIO"

#VARIÁVEL GLOBAL PRA JANELA
janela = None

def btn_clicked():
    global selectedModulo

    bInq.config(relief=RAISED)
    bProp.config(relief=RAISED)
    bConta.config(relief=RAISED)
    bImo.config(relief=RAISED)
    bContrato.config(relief=RAISED)
    bInicio.config(relief=RAISED)

    if selectedModulo == "INQUILINOS":
        bInq.config(relief=SUNKEN)

    elif selectedModulo == "PROPRIETARIOS":
        bProp.config(relief=SUNKEN)

    elif selectedModulo == "IMOVEIS":
        bImo.config(relief=SUNKEN)

    elif selectedModulo == "CONTRATOS":
        bContrato.config(relief=SUNKEN)

    elif selectedModulo == "CONTAS":
        bConta.config(relief=SUNKEN)

    elif selectedModulo == "INICIO":
        bInicio.config(relief=SUNKEN)

def destroyFrame():
    global conteudoFrame
    if conteudoFrame is not None:
        conteudoFrame.destroy()
        conteudoFrame = None

root = Tk()

caixa = Frame(root, bd=3, relief=SUNKEN)
caixa.pack(anchor=NW, fill=X)

def criaConteudoFrame(nome):
    global selectedModulo
    selectedModulo = nome
    destroyFrame()
    global root
    global conteudoFrame
    conteudoFrame = Frame(root, bd=5, relief=SUNKEN)
    conteudoFrame.pack(anchor=NW, fill=BOTH, expand=True, side="left")

def abrir_inq():
    criaConteudoFrame("INQUILINOS")
    global conteudoFrame
    frm_Inq = frmInq.FrmInquilino(conteudoFrame)
    frm_Inq.inqMc.table_data =[[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"]]

    btn_clicked()

def abrir_prop():
    criaConteudoFrame("PROPRIETARIOS")
    global conteudoFrame
    frm_prop = frmProp.FrmProprietario(conteudoFrame)
    frm_prop.propMc.table_data = [
        [
            1,
            "aVictor Hugo Martins de Oliveira",
            "Rua Ourides Poletto, n.11, Jd. Melle, Bairro do Bosque, Vinhedo - SP, CEP: 13234-428",
            "(19) 9 9272-6879",
            "(11) 9 8777-7788",
            "489.789.134-78",
            "emailaleatorioegrande@gmail.com",
            "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira", "Rua Ourides Poletto, n.11, Jd. Melle, Bairro do Bosque, Vinhedo - SP, CEP: 13234-428", "(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira", "Rua Ourides Poletto, n.11, Jd. Melle, Bairro do Bosque, Vinhedo - SP, CEP: 13234-428", "(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira", "Rua Ourides Poletto, n.11, Jd. Melle, Bairro do Bosque, Vinhedo - SP, CEP: 13234-428", "(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira", "Rua Ourides Poletto, n.11, Jd. Melle, Bairro do Bosque, Vinhedo - SP, CEP: 13234-428", "(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira", "Rua Ourides Poletto, n.11, Jd. Melle, Bairro do Bosque, Vinhedo - SP, CEP: 13234-428", "(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira", "Rua Ourides Poletto, n.11, Jd. Melle, Bairro do Bosque, Vinhedo - SP, CEP: 13234-428", "(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira", "Rua Ourides Poletto, n.11, Jd. Melle, Bairro do Bosque, Vinhedo - SP, CEP: 13234-428", "(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"]]
    #frm_prop.propMc.table_data =[["Ut volutpat nisl nec quam vestibulum",2,3,4,5,6],[1,2,3,4,5,6],[1,2,"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec leo erat, venenatis et nisl et, bibendum convallis massa. Sed et est id ipsum malesuada volutpat eu auctor sapien. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam erat risus, tristique nec bibendum at, tempor a lacus.",4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]]

    btn_clicked()

def abrir_imo():
    criaConteudoFrame("IMOVEIS")
    global conteudoFrame
    frm_imovel = frmImo.FrmImoveis(conteudoFrame)
    frm_imovel.inqMc.table_data = [[1,
                                    "Vilma Barbosa de Oliveira",
                                    "Rua das Andorinhas Amargas",
                                    2290,
                                    "Apartamento 15",
                                    "13280-000",
                                    "Jardim Nova Palmares Okay",
                                    "Vale do Sul",
                                    "SP",
                                    "Casa a, frente para a Rua bla bla bla"]]

    btn_clicked()

def abrir_contrato():
    criaConteudoFrame("CONTRATOS")
    global conteudoFrame
    frm_contrato = frmContrato.FrmContrato(conteudoFrame)
    frm_contrato.propMc.table_data = [
        [
            25,
            "Rosenir da Silva Sauro",
            "Mário dos Santos Junior",
            "Rua José Ourivo de Souza, n. 25, Jd. Caldas Novas, Vinhedo - SP",
            "01/09/2020",
            "03/06/2022",
            "R$ 30.000,00",
            "6",
            "R$ 1.600,00",
            "Calção",
            "Foram 03 alugueis de calção"
        ]
    ]


    '''frm_contrato.propMc2.table_data = [
        [
            "5",
            "Aluguél",
            "10",
            "Aluguel - destes serão repassados\n 6% para a imobiliária de administração e pago as contas do imóvel"
        ],
        [
            "2",
            "Conta de Água",
            "10",
            "Aluguel - destes serão repassados\n 6% para a imobiliária de administração e pago as contas do imóvel"
        ]
        ,
        [
            "2",
            "Conta de Energia Elétrica",
            "10",
            "Aluguel - destes serão repassados\n 6% para a imobiliária de administração e pago as contas do imóvel"
        ]
    ]

    frm_contrato.propMc2.configure_column(0, stretch=False, minwidth=65, width=65)
    frm_contrato.propMc2.configure_column(1, stretch=False, minwidth=150, width=150)
    frm_contrato.propMc2.configure_column(2, stretch=False, minwidth=120, width=120)
    frm_contrato.propMc2.configure_column(3, stretch=True, minwidth=450, width=450)
'''
    btn_clicked()

def abrir_conta():
    criaConteudoFrame("CONTAS")
    global conteudoFrame
    frm_contas = frmContas.FrmContas(conteudoFrame)
    frm_contas.propMc.table_data = [
        [
            25,
            "Contas em aberto",
            "Rosenir da Silva Sauro",
            "Mário dos Santos Junior",
            "Rua José Ourivo de Souza, n. 25, Jd. Caldas Novas, Vinhedo - SP",
            "01/09/2020",
            "03/06/2022",
            "R$ 30.000,00",
            "Calção",
            "Foram 03 alugueis de calção"
        ],
        [
            25,
            "Contas em aberto",
            "Rosenir da Silva Sauro",
            "Mário dos Santos Junior",
            "Rua José Ourivo de Souza, n. 25, Jd. Caldas Novas, Vinhedo - SP",
            "01/09/2020",
            "03/06/2022",
            "R$ 30.000,00",
            "Calção",
            "Foram 03 alugueis de calção"
        ],
        [
            25,
            "Sem contas",
            "Rosenir da Silva Sauro",
            "Mário dos Santos Junior",
            "Rua José Ourivo de Souza, n. 25, Jd. Caldas Novas, Vinhedo - SP",
            "01/09/2020",
            "03/06/2022",
            "R$ 30.000,00",
            "Calção",
            "Foram 03 alugueis de calção"
        ]
    ]

    frm_contas.propMc2.table_data = [
        [
            "Aluguel",
            "238472384-2",
            "R$ 12.500,00",
            "10",
            "10/08/2020",
            "09/08/2020",
            "25/07/2020",
            "Aluguel - destes serão repassados 6% para a imobiliária de administração e pago as contas do imóvel"
        ],
        [
            "Conta de Energia Elétrica",
            "823842342342",
            "R$ 12.500,00",
            "10",
            "10/08/2020",
            "09/08/2020",
            "25/07/2020",
            "Aluguel - destes serão repassados 6% para a imobiliária de administração e pago as contas do imóvel"
        ]
    ]

    btn_clicked()

def abrir_inicio():
    criaConteudoFrame("INICIO")
    global conteudoFrame
    pag_inicial = pagInicial.Inicio(conteudoFrame)
    btn_clicked()

zoomImage = 2

imgInicio = PhotoImage(file=os.path.dirname(__file__) + "/images/inicio.png").subsample(zoomImage)
imgInq = PhotoImage(file=os.path.dirname(__file__) + "/images/inquilino.png").subsample(zoomImage)
imgProp = PhotoImage(file=os.path.dirname(__file__) + "/images/proprietario.png").subsample(zoomImage)
imgImovel = PhotoImage(file=os.path.dirname(__file__) + "/images/imovel.png").subsample(zoomImage)
imgContrato = PhotoImage(file=os.path.dirname(__file__) + "/images/contrato.png").subsample(zoomImage)
imgContas = PhotoImage(file=os.path.dirname(__file__) + "/images/contas.png").subsample(zoomImage)

tamBotao = 100

bInicio = Button(caixa, text="Início", image=imgInicio, compound="top", width=tamBotao, command=abrir_inicio)
bInicio.pack(side="left")

bProp = Button(caixa, text="Proprietários", image=imgProp, compound="top", width=tamBotao, command=abrir_prop)
bProp.pack(side="left")

bInq = Button(caixa, text="Inquilinos", image=imgInq, compound="top", width=tamBotao, command=abrir_inq)
bInq.pack(side="left")

bImo = Button(caixa, text="Imoveis", image=imgImovel, compound="top", width=tamBotao, command=abrir_imo)
bImo.pack(side="left")

bContrato = Button(caixa, text="Contratos", image=imgContrato, compound="top", width=tamBotao, command=abrir_contrato)
bContrato.pack(side="left")

bConta = Button(caixa, text="Pagamentos", image=imgContas, compound="top", width=tamBotao, command=abrir_conta)
bConta.pack(side="left")


destroyFrame()
conteudoFrame = Frame(root, bd=5, relief=SUNKEN)
conteudoFrame.pack(anchor=NW, fill=BOTH, expand=True, side="left")

abrir_inicio()
'''
labelTitulo2 = Label(conteudoFrame, text="GERENCIAMENTO DE ALUGUEL BLABABALBABASKDSD", font="Arial 25")
labelTitulo2.pack(anchor=NW)
labelTitulo3 = Label(conteudoFrame, text="GERENCIAMENTO DE ALUGUEL BLABABALBABASKDSD", font="Arial 25")
labelTitulo3.pack(anchor=NW)
labelTitulo4 = Label(conteudoFrame, text="GERENCIAMENTO DE ALUGUEL BLABABALBABASKDSD", font="Arial 25")
labelTitulo4.pack(anchor=NW)'''



#yScrollBar.config(command=conteudoFrame.)
root.iconbitmap(os.path.dirname(__file__) + '/images/icon.ico')
root.geometry("800x600")
root.title("Administração de locação")
root.state("zoomed")
root.minsize(1024,768)

root.mainloop()


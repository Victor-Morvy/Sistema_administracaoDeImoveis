from tkinter import *
import tkinter as tk
import os
from tkinter.ttk import Style

import UI.FrmInquilino as frmInq
import UI.FrmProprietario as frmProp
import UI.FrmImoveis as frmImo
import UI.FrmContrato as frmContrato
import UI.FrmContas as frmContas
import UI.Inicio as pagInicial

import lib.ColumnListview as multiList
from lib.funcoes import validate_entry



conteudoFrame = None
selectedModulo = "INICIO"


#VARIÁVEL GLOBAL PRA JANELA
#janela = None
dados = None

frm_opened = None

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
    global frm_opened

    if hasattr(frm_opened, "jan"):
        frm_opened.fecha_janela()

    if conteudoFrame is not None:
        conteudoFrame.destroy()
        conteudoFrame = None

root = tk.Tk()

caixa = Frame(root)
caixa.pack(anchor=NW, fill=X)

def criaConteudoFrame(nome):
    global selectedModulo
    selectedModulo = nome
    destroyFrame()
    global root
    global conteudoFrame
    conteudoFrame = Frame(root)
    conteudoFrame.pack(anchor=NW, fill=BOTH, expand=True, side="left")

def abrir_inq():
    global frm_opened
    criaConteudoFrame("INQUILINOS")
    global conteudoFrame
    frm_opened = frmInq.FrmInquilino(conteudoFrame)
    frm_opened.inqMc.table_data =[[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"],[1,"Victor Hugo Martins de Oliveira","(19) 9 9272-6879","(11) 9 8777-7788","489.789.134-78","emailaleatorioegrande@gmail.com", "Ligar sempre que possível no horário da tarde, atende whatsapp"]]
    frm_opened.inqMc.toogle_selection(5)
    btn_clicked()

def abrir_prop():
    global frm_opened
    criaConteudoFrame("PROPRIETARIOS")
    global conteudoFrame
    frm_opened = frmProp.FrmProprietario(conteudoFrame)
    frm_opened.listar_proprietarios()

    btn_clicked()

def abrir_imo():
    global frm_opened
    criaConteudoFrame("IMOVEIS")
    global conteudoFrame
    frm_opened = frmImo.FrmImoveis(conteudoFrame)

    btn_clicked()

def abrir_contrato():
    global frm_opened
    criaConteudoFrame("CONTRATOS")
    global conteudoFrame
    frm_opened = frmContrato.FrmContrato(conteudoFrame)
    frm_opened.propMc.table_data = [
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


    btn_clicked()

def abrir_conta():
    global frm_opened
    criaConteudoFrame("CONTAS")
    global conteudoFrame
    frm_opened = frmContas.FrmContas(conteudoFrame)
    frm_opened.propMc.table_data = [
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

    frm_opened.propMc2.table_data = [
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
    global frm_opened
    criaConteudoFrame("INICIO")
    global conteudoFrame
    frm_opened = pagInicial.Inicio(conteudoFrame)
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
conteudoFrame = Frame(root)
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
#root.state("zoomed")
root.minsize(1024,768)

root.mainloop()


#valida o tamanho máximo e se o numero é inteiro
def validate_entry(valor, tam_maximo):
    valid = valor.isdigit() and len(valor) <= int(tam_maximo) or valor == ""
    return valid

#valida se o valor é um número inteiro
def number_entry(valor):
    valid = valor.isdigit() or valor == ""
    return valid

#traz para a frente a tupla na lista pelo id(valor[0])
def traz_para_frente(id, lista):
    listaRes = lista
    valor = [item for item in listaRes if item[0] == id]
    listaRes.remove(valor[0])
    listaRes.insert(0, valor[0])
    return listaRes

#transforma o resultado em list of tuples em list of list
def tratar_resultado_banco(lista):
    lista2 = []

    for elem in lista:
        lista_aux = []
        lista_aux.append(["" if i is None else i for i in elem])
        lista2.append(lista_aux[0])

    #print(lista2)
    return list(lista2)

#transforma tuplas dentro da lista em listas e joga o id de interesse para frente
#ideal para receber a lista que retorna no banco, e colocar o resultado
#de interesse na frente
def listar_interesse(id, lista):
    return tratar_resultado_banco(traz_para_frente(id, lista))


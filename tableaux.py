# -*- coding: utf-8 -*-

''' LISTA DE CARACTERES:
    e = Operador And
    v = Operador Or
    > = Implica que
    | = Prova que
'''
'''
clausula = "((s e t) > (p v (t v q)))"
            "
            (((t v q) v p) > (s e t))"
            "(((t v q) v p)) > (s e t)"
            ((p v (q v t)))
'''
#arquivo = open(tableaux,a)
ListaTotal = []
clausula = "(a v n)|(a v b),(b > a)"
gama1 = ''
gama2 = ''

#Aqui, será realizado a separação da hipotese e conclusão! :)
contemBarra = "|" in clausula
if(contemBarra == True):
    if(clausula[0] == '|'):
        clausulas = clausula.split('|')
        contemVirg = "," in clausulas[1]
        
        if(contemVirg == True):
            gama2 = clausulas[1].split(',')
        else:
            gama2 = clausulas[1]
    for qtdClausulas in range(0, len(gama2)):
        ListaTotal += ["F"+gama2[qtdClausulas]]
    else:
        clausulas = clausula.split('|')
        
        contemVirg = "," in clausulas[0]
        if(contemVirg == True):
            gama1 = clausulas[0].split(',')
            contemVirg = "," in clausulas[1]
        else:
            gama1 = clausulas[0]
        if(contemVirg == True):
            gama2 = clausulas[1].split(',')
        else:
            gama2 = clausulas[1]
    '''for qtdClausulas1 in range(0, len(gama1)):
        ListaTotal += ["T"+gama1[qtdClausulas]]
    for qtdClausulas2 in range(0, len(gama2)):
        ListaTotal += ["F"+gama2[qtdClausulas]]'''
else:
    gama1 = clausula

print(gama1)
print(gama2)
print(ListaTotal)
'''
contador = 0
parenteses1 = 0
parenteses2 = 0

print(ListaTotal)
'''
'''
#Aqui será realizado a divisão dos parentes, separando por clausulas
def EncontrarClausulas ()
    #para clausulas duplas com parênteses que não englobam todas as clausulas
    if(gama1 != ''):
        while contador 0 < gama1



'''
'''
def ListTableaux1(stringAux):
    stringAux = stringAux.replace(',', '\n')
    stringAux = stringAux.replace('[', '')
    stringAux = stringAux.replace(']', '')
    stringAux = stringAux.replace("'", "")
    stringAux = stringAux.replace(" ", "")
    stringAux = stringAux.replace("*", " ")
    return stringAux

clausula = "p>q, q>r | p>r"
lista = clausula.split('|')
print (lista[0])
valor = lista[0].count(',')
print (valor)'''

'''
def tableaux(clausula):
    lista_01 = clausula.split('|')

    #Verificar vírgulas na clausula:
    contVirgula = lista_01[0].count
    if(contVirgula > 0):
        print("Não tem vírgula")
    else:
        print("Tem vírgula")

   

tableaux()
'''
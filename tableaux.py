# -*- coding: utf-8 -*-

''' LISTA DE CARACTERES:
    e = Operador And
    v = Operador Or
    > = Implica que
    | = Prova que
'''
'''
clausula = "((s e t) > (p v (t v q)))"
            "(((t v q) v p) > (s e t))"
            "(((t v q) v p)) > (s e t)"
            ((p v (q v t)))
'''
#arquivo = open(tableaux,a)
ListaTotal = []
clausula = "|(a v b)"

#Aqui, será realizado a separação do gama e do alfa! :)
contemBarra = "|" in clausula
if(contemBarra == True):
    if(clausula[0] == '|'):
        clausulas = clausula.split('|')
        gama2 = clausulas[1]
        ListaTotal += ["F"+gama2]
    else:
        clausulas = clausula.split('|')
        gama1 = clausulas[0]
        gama2 = clausulas[1]
        ListaTotal += ["T"+gama1+"_"+"F"+gama2]
else:
    gama1 = clausula

contador = 0
parenteses1 = 0
parenteses2 = 0

print(ListaTotal)

'''
#Aqui será realizado a divisão dos parentes, separando por clausulas
def EncontrarClausulas ()
    #para clausulas duplas com parênteses que não englobam todas as clausulas
    if(gama1 != ''):
        while contador 0 < gama1


ijiimjmjiiuuijj


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
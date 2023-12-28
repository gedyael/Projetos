from adiçao import*
from cores import*
from divisão import*
from multiplicaçao import *
from subtração import* 
from entrada import *
from opçãosair import *


def menu():
    opcao_de_entrada()
    while True:
        entrada_menu = str(input('Selecione a Opçao Desejada: '))
        if entrada_menu == '1':
            Adição()
            Opçao_Sair()
        elif entrada_menu == '2':
            multiplicação()
            Opçao_Sair()
        elif entrada_menu == '3':
            subtração()
            Opçao_Sair()
        elif entrada_menu == '4':
            divisao()   
            Opçao_Sair()
        else:
            print(f'{red}Opçao invalida....{close}')

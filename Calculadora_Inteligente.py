blue= '\033[36m'
red = '\033[31m'
close = '\033[m'

def soma2():
    N1 = int(input('digite o primeiro numero: '))
    N2 = int(input('digite segundo numero: '))
    somar = N1 + N2
    print(somar)
    Opçao_Sair()

def multiplicação():
    N1 = int(input('Digite o Primeiro Numero: '))
    N2 = int(input('Digite o Segundo Numero: '))
    soma_multiplicaçao = N1 * N2
    print(soma_multiplicaçao)
    Opçao_Sair()
def subtração():
    N1 = int(input('Digite o Primeiro Numero: '))
    N2 = int(input('Digite o Segundo Numero: '))
    Resultado_Subtraçao = N1 - N2
    print(Resultado_Subtraçao)
    Opçao_Sair()
def divisao():
    N1 = int(input('Digite o Primeiro Numero: '))
    N2 = int(input('Digite o Segundo Numero: '))
    Resultado_Divisao = N1 / N2
    print(round(Resultado_Divisao))
    Opçao_Sair()

def menu():
    while True:
        opcao_de_entrada()
        entrada_menu = str(input('Selecione a Opçao Desejada: '))
        if entrada_menu == '1':
            soma2()
        elif entrada_menu == '2':
            multiplicação()
        elif entrada_menu == '3':
            subtração()
        elif entrada_menu == '4':
            divisao()   
        else:
            print(f'{red}Opçao invalida....{close}')

def opcao_de_entrada():
    print(f'''{blue}
        1- ADIÇAO
        2- MULTIPLICAÇAO
        3- SUBTRAÇAO
        4- DIVISÃO{close}''')    

def Opçao_Sair():
    escolha = str(input('Deseja Fazer outra Operação? ').upper())
    if escolha == 'SIM':
        menu()
    elif escolha == 'NAO':
        print(f'{red}FECHANDO PROGRAMA....{close}')
        exit()
    else:
        print(f'{red}Opçao invalida!{close}')
        Opçao_Sair()
menu()



       
        

                   
                    
from cores import*
from menu import*
from entrada import*
def Opçao_Sair():
    escolha = str(input(f'{blue}Deseja Fazer outra Operação?{close}').upper())
    if escolha == 'SIM':
        opcao_de_entrada()
        
    elif escolha == 'NAO':
        print(f'{red}FECHANDO PROGRAMA....{close}')
        exit()
    else:
        print(f'{red}Opçao invalida!{close}')
        Opçao_Sair()
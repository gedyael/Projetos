lista = []

blue= '\033[36m'
red = '\033[31m'
greew = '\033[32m'
yellow = '\033[33m'
close = '\033[m'

def Pergunta_1():

    perg_1 = str(input(f'{greew}Deseja acrescentar algo mais ?{close} ').upper())
    if perg_1 == 'SIM':
        lista.append(entrada_2)
    else:
        print(f'{blue}Sua Lista Tem:{close} {yellow}{lista}{close}')

        
print('') 

while True:
    entrada_1 = str(input(f'{greew}me informe um produto:{close} ').upper())
    lista.append(entrada_1)
    print(f'''{blue}sua Lista contém{close} {yellow} {lista} {close}
{blue}Digite Sair a Qualquer Momento{close} ''')
    if entrada_1 == 'SAIR':
        lista.remove('SAIR')
        Pergunta_1()
        break
print('')

print(f'{yellow}{lista}{close}') 

def menu():
    print(f'''
    1- apagar 
    2- apagar todos''')

print('')  

while True:
    menu()
    entrada_2 = str(input(f' {greew}Escolha uma das opção:{close} ').upper())
    if entrada_2 == '1':
        try:
            remover = str(input(f'{greew}Qual Produto Desejar Remover?{close} ').upper())
            lista.remove(remover)
            print(f'{yellow}{remover}{close} {red}apagado com sucesso{close}')
            print(f'{blue}Sua lista contém{close}{yellow}{lista}{close}')
        except:
            print(f'O intem: {remover} Nao Contém Na {lista} ')
    elif entrada_2 == '2':
        lista.clear()
        print(f'''{red}voçe apagou Todos o intém da Sua lista{close} {yellow}{lista}{close}''')
        break
     
   

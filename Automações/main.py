#passo a passo do projeto
# 1: entrar no sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login
# importar o pyautogui que nos permite automatizar qualquer coisa
# usando a teclado mouse e tela do computador
import pyautogui

# definir pausa pra entrar no link
pyautogui.PAUSE = 0.5

# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar 1 tecla do teclado

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("Google")
pyautogui.press("enter")

# escrever o link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

#entrar no link
pyautogui.press("enter")



# 2: fazer login
# 3: importar a base de dados
# 4: cadastrar 1 produto
# 5: repetir o processo de cadastro ate acabar
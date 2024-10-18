# Passo 1: Entrar no sistema da impresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# importar a biblioteca 
import pyautogui
import time

# Tempo para os codigos não se sobre escreverem 
pyautogui.PAUSE = 0.7
# Indo para o Google Chorme
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
# Inserindo e entrando pelo link do Sistema 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Tempo para recarregar caso demore a entrar na pagina 
time.sleep(1)

# Passo 2: Fazer o login no sistema
# Clicar para inserir gmail na entrada de texto 
pyautogui.click(x=751 ,y=533 )
# Escrever o gmail
pyautogui.write("naky88@gmail.com")
# Ir para  proxima entrada de texto ( SENHA )
pyautogui.press("tab") 
# EScrever a senha 
pyautogui.write("naky88@")
# Clicar para prosseguir 
pyautogui.click(x=956 ,y=726 )


time.sleep(1)
# Passo 3: Importar a base de dados
import pandas 

tabela = pandas.read_csv("produtos.csv")


 
 
  
# Passo 4: Cadastrar os produtos

linha = 0 
for linha in tabela.index:

    # Código do Produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.click(x=879, y=376)
    pyautogui.write(str(codigo))

    # Marca do Produto
    marca = tabela.loc[linha, "marca"]
    pyautogui.press("tab")
    pyautogui.write(str(marca))

    # Tipo do Produto
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.press("tab")
    pyautogui.write(str(tipo))

    # Categoria do Produto
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.press("tab")
    pyautogui.write(str(categoria))

    # Preço Unitário do Produto
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.press("tab")
    pyautogui.write(str(preco))

    # Custo do Produto
    custo = tabela.loc[linha, "custo"]
    pyautogui.press("tab")
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # Observações
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
      pyautogui.write(str(obs))
    pyautogui.press("tab")
    
   
    pyautogui.press("enter")
    pyautogui.scroll(1000)
   
    pyautogui.click(x=879, y=376)

   
   
   
# Passo 5: Repetir o processo até acabar os produtos
  
 
  

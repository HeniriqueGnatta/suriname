'''
Arquivo de Modulos
2024.08.13
Henrique Gnatta
'''

# --> bibliotecas
from random import choice# inportando  uma biblioteca ramdo

from time import sleep# --> constante, variaveis e listas
TAM = 50# tamanho da tela
# --> Funções
CAR = choice(['>','-','!','<'])# caracter ultilizado para dispay da tela
MAR = 4 #tamanho da Margem
def clrScreen():# função para limpar a tela
  print('\n'*TAM)# mostra na tela \n == linha em branco que pulou TAM 

def displayline():# função para mostrar   caracteres
  print(CAR*TAM)#para colocar os caracteres vezes o tamanho de vezes que vão ser multiplicados



def displaymsg(msg):# função de mostrar a mensagem a esquerda
  print(f'{CAR} {msg:<{TAM-MAR}} {CAR}')#usando mascara e deslocar amenagem para a esquerda
  
  
  
def displaymsgcenter(msg):#função colocar a mensagem para cima 
  print(f'{CAR} {msg:^{TAM-MAR}} {CAR}')#para centralizar a mensagem 

def displayheader(msgs):#função para colocar linha de baixo do display
  displayline()
  for  item in msgs:
    displaymsgcenter(item)
  displayline()
def displayheaderT(msgs):#função para colocar linha de baixo do display
  displayline()
  for  item in msgs:
    displaymsgcenter(item)
    sleep(1)
  displayline()


def chato(msg):#chato getuseropition e --> chato
   option = input(f'{CAR} {msg}: ').strip()#strip ignora os espaços do usuario
   return option

def validateuseropiton(opiton,listopitions):
  if opiton in listopitions:
    return True
  else:
    msgserro = ['opção invalida!','escolha novamente...']
    displayheader(msgserro)
    return False

# --> Main







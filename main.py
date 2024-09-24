"""
projeto jogo pedra papel tesoura
2024.08.13
Henrique Gnatta
"""

# --> biblioteca
from  modules import clrScreen, displayline, displaymsg,displaymsgcenter,displayheader,chato,validateuseropiton,displayheaderT#inportando de um arquivo ou biblioteca que nesse caso é o modules
from ppt import starppt#inportando do arquivo ppt 
from parimpar import startparimpar
# inport a funções  do arquivo modules.py 
# --> constantes, variaveis e listas 

# --> funções

# --> Main 
msgs = ['seja bem-vindo aos jogos','pedra-papel-tesolra','par ou impar']
displayheader(msgs)
msgs = ['digite 0 --> sair','digite 1 --> pedra-papel-tesoura','digite 2 --> par ou impar']
displayheaderT(msgs)
opuser = chato('sua escolha')
while not validateuseropiton(opuser,['0','1','2']):
  opuser = chato('sua escolha')
if(opuser == '1'):
  startppt()
elif(opuser == '2'):
  startparimpar()
else:
  displaymsg('Até a proxima...')
#iniciar os codigos de starppt
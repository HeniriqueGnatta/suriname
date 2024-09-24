'''
jogo do par ou impar
2024.08.20
Henrique Gnatta
'''

#biblioteca
from modules import clrScreen,displayheader,chato,validateuseropiton,displayline,displaymsg,displaymsgcenter,displayheaderT

from random import randint
from time import sleep 
#costantes, variaveiss e litas 

playerscore = 0# usando para que cada vez que a partida iniciar 0 o placar do player
computerscore = 0# usando para que cada vez que a partida iniciar 0 o placar do computador
msgsinicio = ['Seja bem vindo ao','Par ou Impar','desenvolvido por: Henrique Gnatta ']#mensage, de boas vinda ao iniciar o jogo
msgs = []
playagain  = ''
playerjog = ''
def determinevencedor(playerchoice,playernumber, computernumber):
  result = ''
  choice = ['Par','Impar']
  sumnumbers = playernumber + computernumber
  playerchoicestr = choice[int(playerchoice)]
  computerchoicestr = choice [int(computerchoice)]
 
  if (sumnumbers % 2== 0 and playerchoice == '0') or (sumnumbers % 2 != 0 and playerchoice == 1):
    result = 'ganhou' 
  else:
    play = f'{computerchoicestr} vence {playerchoicestr}'
    result = 'voce perdeu'
  msgs = [f'numero do player: {playernumber}',f'numero do PC:{computernumber}',f'soma {sumnubers}',result]
  displayheaderT(msgs)
  return result


#funções 
def startparimpar():
  while(True):
    clrScreen()
    displayheader(msgsinicio)
    playparimpar()
     #função pra começar o jogo 
    playagain = chato('Deseja jogar novamente [s/n]')
    while not validateuseropiton(playagain,['s','n','S','N']):
      playagain = chato ('deseja jogar novamente[s/n]')
    if playagain.lower() != 's':
      break



def displaymenu():
  msgs =['escolha:','[0] --> Par','[1] --> Impar',]
  displayline()
  for msg in msgs:
    displaymsg(msg)
  displayline()


def displayscore(typecore ,playerscore, computerscore):
  msgs = []
  msgs.append(typescore)
  msgs.append(f'player:{playerscore} ---PC:{computerscore}')
  displayheaderT(msgs)


def playparimpar():
  global playerscore,computerscore
  playerscore = 0
  computerscore = 0
  while playerscore < 2 and computerscore < 2:
    displaymenu()
    playerchoice = chato("sua escolha")
    while not validateuseropiton(playerjog, ['0','1',]):
      displaymenu()
      playerchoice = chato ('sua escolha')
    playernumber = int(chato('escolha um nnumero de 1 até 9'))
    while not validateuseropiton(str(playernumber),[str(i) for i in range(1,9)]):
      playernumber = int(chato('escolha um numero de 1 até 9'))
      cimputernumber = randint(1,9)
    result = determinevencedor(playerchoice, playernumber, computernumber)
    if 'ganhou'in result:
      playscore += 1
    elif 'Perdeu' in result:
      computadorscore += 1
      if playerscore < 2 and computerscore < 2:
        diplayscore('Placar', playerscore, computerscore)
      sleep(1)#biblioteca para espera tempo
      displayscore('placar final', playerscore, computerscore)
    if playerscore > computerscore:
      displayheader(['parabens','you win'])
    else:
       displayheader(['parabens','you lose'])
      #main 
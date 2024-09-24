'''
jogo do peda papel tesoura
2024.08.13
Henrique Gnatta
'''

#biblioteca
from modules import clrScreen,displayheader,chato,validateuseropiton,displayline,displaymsg,displaymsgcenter,displayheaderT

from random import randint
from time import sleep 
#costantes, variaveiss e litas 

playerscore = 0
computerscore = 0
msgsinicio = ['Seja bem vindo ao','jogo do PEDRA PAPEL TESOURA','desenvolvido por: Henrique Gnatta ']
msgs = []
playagain  = ''

def determinevencedor(playerchoice, computerchoice):
  play = ''
  result = ''
  choice = ['Pedra','Papel','Tesolra']
  playerchoicestr = choice[int(playerchoice)]
  computerchoicestr = choice [int (computerchoice)]
  if playerchoice == computerchoice:
    result = 'empate!'
  elif (playerchoice =='0' and computerchoice == '2') or (playerchoice =='1'and computerchoice == '0') or (playerchoice == '2'and computerchoice == '1'):
    play = f'{playerchoicestr} vence {computerchoicestr}'
    result = 'ganhou'
  else:
    play = f'{computerchoicestr} vence {playerchoicestr}'
    result = 'voce perdeu'
  msgs = [' jogada do player; ' + playerchoicestr,'jogando do pc '+ computerchoicestr, play ]
  displayheaderT(msgs)
  return result


#funções 
def starppt():
  while(True):
    clrScreen()
    displayheader(msgsinicio)
    playppt()
     #função pra começar o jogo 
    playagain = chato('Deseja jogar novamente [s/n]')
    while not validateuseropiton(playagain,['s','n','S','N']):
      playagain = chato ('deseja jogar novamente[s/n]')
    if playagain.lower() != 's':
      break
def displaymenu():
  msgs =['escolha:','[0] --> Pedra','[1] --> papel','[2] --> Tesoura']
  displayline()
  for msg in msgs:
    displaymsg(msg)
  displayline()
  
def displayscore(typescore ,playerscore, computerscore):
  msgs = []
  msgs.append(typescore)
  msgs.append(f'player:{playerscore} ---PC:{computerscore}')
  displayheaderT(msgs)


def playppt():
  playerscore = 0
  computerscore = 0
  while playerscore < 2 and computerscore < 2:
    displaymenu()
    playerchoice = chato("sua ecolha")
    while not validateuseropiton(playerchoice, ['0','1','2']):
      displaymenu()
      playerchoice = chato ('sua escolha')
    computerchoice = str(randint(0,2))
    result = determinevencedor(playerchoice, computerchoice)
    if 'ganhou'in result:
      playerscore += 1
    elif 'perdeu' in result:
      computerscore += 1
    if playerscore < 2 and computerscore < 2:
      displayscore('Placar', playerscore, computerscore)
  sleep(1)#biblioteca para espera tempo
  displayscore('placar final', playerscore, computerscore)
  if playerscore > computerscore:
    displayheader(['parabens','you win'])
  else:
     displayheader(['parabens','you lose'])
      #main 
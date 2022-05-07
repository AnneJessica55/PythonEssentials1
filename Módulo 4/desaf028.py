#Escreva um programa que faça o computador pensar em um número intiro entre 0 e 5.
#Depois peça para o usuário tentar descobrirr o número escolhido pelo computados.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
num = randint(0,5)
num1 = int(input('Tente descobrir o número inteiro secreto!\nOlá, me chama Gaspard. Você consegue descobrir o número que estou pensando?\nDeixe sua sugestão abaixo de um número inteiro de 0 até 5:\n'))
print('Processando.....')
sleep(2)
if (num1==num):
    print('Parabéns! Estamos mesmo em sintonia de pensamento. O número que eu pensei foi exatamente {}.'.format(num))
else:
    print('Que pena, você errou. O número que pensei foi {}, e não {}'.format(num,num1))
print('Obrigado por jogar comigo, até a próxima!')

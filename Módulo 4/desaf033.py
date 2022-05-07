#faça um programa ler 3 númes e dizer qual foi digitado primeiro, o maior e o menor
from time import sleep
n1 = int(input("""Olá, humano!
Vamos jogar um jogo?
Você digita 3 valores, e eu vou adivinhar qual foi digitado primeiro, o maior valor digitado e o menor valor digitado. Pode ser?
Então vamos começar
Digite um número inteiro abaixo:\n"""))
n2 = int(input('Digite outro número inteiro abaixo:\n'))
n3 = int(input('Digite o último número inteiro abaixo:\n'))
menor = n1
maior = n1
print('Só um momento, que estou pensando....')
sleep(3)
if (n2>n1 and n2>n3):
    maior = n2
if (n3>n2 and n3>n1):
    maior = n3
if (n2<n1 and n2<n3):
    menor = n2
if( n3<n1 and n3<n2):
    menor = n3
print("""O primeiro valor digitado foi {}.
O maior valor digitado foi {}
O menor valor digitado foi {}.
Acertei? Claro que acertei! HA! HA! HA!
Apreta o play pra gente jogar de novo!!""".format(n1,maior,menor))
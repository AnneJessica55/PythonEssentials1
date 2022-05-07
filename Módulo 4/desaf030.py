#Crie um programa que leia um número inteiro e mostre se ele é ímpar ou par
num = int(input("""Olá! Vamos descobrir se esse número que você está pensando é par ou ímpar?
Então, vamos nessa! Digite abaixo o número inteiro diferente de 0 que você está pensando:\n"""))
if (num%2==0):
    print('O número {} que você digitou é um número par!\n'.format(num))
else:
    print('O número {} que você digitou é um número ímpar!\n'.format(num))
print('Aperte o play para escolher outro número!!')
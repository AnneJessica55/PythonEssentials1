#Faça um programa que peça ao usuário digitar um ano e depois diga se esse ano é ou não bissexto
ano = int(input("""Olá! Vamos saber se o ano em questão é Bissexto?
Digite abaixo a ano que você deseja analisar:\n"""))
if(ano%4==0):
    print('O ano {} é bissexto, logo ele terá 366 dias! Um dia a mais pra você se divertir!'.format(ano))
else:
    print('O ano {} não é bissexto, logo ele só terá 365 dias! Faça valer a pena!'.format(ano))
print('\nAperte o play de novo para escolher outro ano.')
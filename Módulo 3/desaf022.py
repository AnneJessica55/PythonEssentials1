#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maíusculas;
#O nome com todas as letras minúsculas;
#Quantas letras ao sem considerar espaços;
#Quantas letras tem o primeiro nome.
nome = str(input('Digite o seu primeiro nome:\n')).strip()
sobrenome = str(input('Digite o seu Sobrenome:\n')).strip()
print('Analisando seu nome.\nSeu nome em letra maiúscula é:\n{} {}'.format(nome.upper(),sobrenome.upper()))
print('Seu nome em letra ninúscula é:\n{} {}'.format(nome.lower(),sobrenome.lower()))
print('Seu nome contém {} letras, e seu sobrenome contém {} letras.'. format(len(nome)-nome.count(' '), len(sobrenome)-sobrenome.count(' ')))
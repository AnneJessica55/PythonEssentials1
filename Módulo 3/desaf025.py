#Faça um programa que leia o nome do usuário, e diga se tem 'Silva' no nome dele
nome = str(input("""Será que tem Silva no seu nome?
Digite abaixo o seu nome completo sem abreviações:\n"""))
print('SILVA' in nome.upper())
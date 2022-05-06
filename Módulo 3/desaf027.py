#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input("""Escreva uma frase do seu interesse:\n""")).strip().upper()
print("""Sua frase  contém {} letras 'A'.
A primeira letra 'A' está na {}° casa.
A ultima letra 'A' está na {}° casa.""".format(frase.count('A'),frase.find('A')+1, frase.rfind('A')+1))
#Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ela;
n1= input('Digite algo: ');
print('O conteudo digitado é do tipo {}. Ele pode ser um número? {}. Ele pode ser uma palavra/frase? {}'.format(type(n1),n1.isnumeric(),n1.isalpha()))
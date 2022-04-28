#Um professor quer sortear um dos 4 alunos para perturbar durante todo o ano letivo.
#Faça um programa que ajude este amistoso professor a escrever os nomes e sortear um deles..
from random import choice
al1 = input('Digite o primeiro nome:\n');
al2 = input('Digite o segundo nome:\n');
al3 = input('Digite o terceiro nome:\n');
al4 = input('Digite o quarto nome:\n');
infelizes = [al1,al2,al3,al4];
infeliz = choice(infelizes);
print('O felizardo/felizarda é o/a {}.\nExcelente escolha! Esse/essa aluno/aluna não presta mesmo.'.format(infeliz));

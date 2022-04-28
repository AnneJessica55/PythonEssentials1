#Faça um programa onde um professor amável digita o nome de 4 alunos insuportáveis e o programa gera a ordem que esse professor deve irritar esses demônios.
from random import shuffle
al1 = input('Digite o primeiro nome:\n');
al2 = input('Digite o segundo nome:\n');
al3 = input('Digite o terceiro nome:\n');
al4 = input('Digite o quarto nome:\n');
infelizes = [al1,al2,al3,al4];
shuffle(infelizes)
print('A ordem de perturbação será:\n {}.\nBoa perturbação, querido professor.'.format(infelizes));
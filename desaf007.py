#Crie um Algorítmo que leia as notas de um aluno e calcule a sua média.
nome = input('Digite o nome do aluno:\n');
n1 = float(input('Digite a primeira nota:\n'));
n2 = float(input('Digite a segunda nota:\n'));
n3 = float(input('Digite a terceira nota:\n'));
n4 = float(input('Digite a quarta nota:\n'));
print('A média do/da {} é igual a {}.'.format(nome,(n1+n2+n3+n4)/4))
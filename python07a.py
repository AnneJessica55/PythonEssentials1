#Operadores Matemáticos:
# * (multiplicação), +(adição), -(subtração), /(divisão), **(potenciação), //(inteiro da divisão), %(resto da divisão);
#Ordem 1° () []{}, 2° **, 3° * / // %, 4° + -;
#Outros tipode de operadores:
#: (repetições em vezes), <(alinhado a esquerda), >(alinhado a direita), ^(centralizado)
nome = input('Por favor, digite o seu nome: ');
print('{:-^20}, olá. É um prazer te conhecer'.format(nome));
num1 = int(input('Digite um número inteiro: '));
num2 = int(input('Digite outro número inteiro: '))
print('{} + {} = {}'.format(num1,num2,num1 + num2));
print('{} - {} = {}'.format(num1,num2,num1 - num2));
print('{} / {} = {:3f}'.format(num1,num2,num1/num2));
print('{} ^ {} = {}'.format(num1,num2,num1**num2));
print('Divisão inteira de {} por {} é {}'.format(num1,num2,num1//num2));
print('O resto da divisão de {} por {} é igual a {}'.format(num1,num2,num1%num2));
#\n (quebra linha), end=' ' (colocar na mesma linha);
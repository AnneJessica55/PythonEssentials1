import math;

nome = str(input('Digite o seu nome:\n'));
idade = int(input('Digite sua idade em anos:\n'));
peso = float(input('Digite o seu peso em quilogramas:\n'));
altura = float(input('Digite a sua altura em metros: \n'));
imc = (peso/(altura**2));
texto =('Olá, {}. Você tem {} anos, pesa {}Kg e mede {}m de altura, seu IMC é de {:.2f}.').format(nome, idade, peso, altura, imc);
print(texto);
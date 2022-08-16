nome = str(input('Digite o seu nome:\n'));
peso = float(input('Digite o seu peso em quilogramas:\n'));
altura = float(input('Digite a sua altura em metros: \n'));
imc = (peso/(altura**2));

if imc < 18.5:
    print('Olá, {}. Seu IMC é de {:.2f}. Você está abaixo do peso ideal. Coma mais.'.format(nome, imc));
elif imc < 25:
    print('Olá, {}. Seu IMC é de {:.2f}. Você está no seu peso ideal.'.format(nome, imc));
elif imc < 30:
    print('Olá, {}. Seu IMC é de {:.2f}. Você está sobrepeso. Coma menos'.format(nome, imc));
elif imc < 40:
    print('Olá, {}. Seu IMC é de {:.2f}. Você está com obesidade do tipo I. Faça mais exercícios.'.format(nome, imc));
else:
    print('Olá, {}. Seu IMC é de {:.2f}. Você está abaixo com obesidade do tipo II. Vá já pra academia'.format(nome, imc));
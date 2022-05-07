#Faça um programa que leia o salário digitado pelo o usuário e calcule seu aumento
#Caso ele ganhe mais de R$1250, o aumento será de 10%
#Caso ele ganhe menos de R$1250, o aumento será de 15%
nome= str(input('Digite seu nome abaixo:\n')).strip().title()
sal = float(input('Olá, {}!\nDigite abaixo o seu salário em R$:\n'.format(nome)))
if (sal>1250):
    print('Você recebeu um aumento de 10%.\nSeu salário de  R${:.2f} terá um acréscimo de R${:.2f}, passando a ser R${:.2f}\nParabéns, {}, você fez por merecer.'.format(sal, sal*0.1,sal*1.1,nome))
else:
    print('Você recebeu um aumento de 15%.\nSeu salário de  R${:.2f} terá um acréscimo de R${:.2f}, passando a ser R${:.2f}\nParabéns, {}, você fez por merecer.'.format(sal, sal * 0.15, sal * 1.15, nome))
print('--------FIM--------')
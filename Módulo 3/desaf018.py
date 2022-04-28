#Crie um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente do angulo.
from math import radians, degrees, cos, sin
print('Calculando o seno e cosseno de um ângulo.\n')
ang = float(input('Digite o valor do ângulo em ° (graus).\n'));
print('O valor de seno e cosseno do ângulo informado é:\ncos( {} ) = {}\nsen( {} ) = {}'.format(ang, cos(radians(ang)), ang, sin(radians(ang))));


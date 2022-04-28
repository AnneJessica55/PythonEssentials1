#Crie um programa que leia um número real qualquer pelo teclado e mostre a sua porção inteira.
import math
num = float(input("Digite um número Real:\n"))
print("O valor inteiro arredondado de {} é igual a {}.".format(num, math.ceil(num)));
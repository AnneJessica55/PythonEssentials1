#Faça um programa onde o usuário digita o comprimento em cm de 3 retas
#O programa diz se essas retas formam um triângulo
import math
r1 = float(input("""Será que da triangulo?
Digite um comprimento em cm para reta 1, reta 2  e reta 3 para saber se esses comprimentos podem descrever um triângulo
Reta 1:\n"""))
r2 = float(input('Reta 2:\n'))
r3 = float(input('Reta 3:\n'))
if(r1>(math.sqrt((r2-r3)**2)) and r1<(r2+r3) ):
    if( r2 > (math.sqrt((r1 - r3) ** 2)) and r2 < (r1 + r3)):
        if( r3 > (math.sqrt((r2 - r1) ** 2)) and r3 < (r2 + r1)):
            if (r1%3==0 or r1%4==0 or r1%5==0):
                if (r2%3==0 or r2%4==0 or r2%5==0):
                    if (r3 % 3 == 0 or r3 % 4 == 0 or r3 % 5 == 0):
                        print('As retas podem formar um triângulo retângulo.')
                    else:
                        print('As retas podem formar um triângulo comum.')
                else:
                    print('As retas podem formar um triângulo comum.')
            else:
                print('As retas podem formar um triângulo comum.')
else:
    print('As retas nã podem formar um triângulo')
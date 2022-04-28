#Faça um programa que leia o cateto oposto e adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa, bem como os ângulo;
import math

catop = float(input('Informe o comprimento em cm do cateto oposto do triângulo.\n'));
catad = float(input('Informe o comprimento em cm do cateto adjacente do triângulo.\n'));
hip = math.sqrt(catop**2+catad**2);
angop = math.asin(catop/hip);
angad = math.acos(catad/hip);
print('O comprimento da hipotenusa é igual a {}cm, e os ângulo são {} e {} radianos.'.format(hip,angop,angad));


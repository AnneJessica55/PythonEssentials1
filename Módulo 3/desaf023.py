#Digitar um número até 9999 e dizer quem é unidade, dezena, centena e unidade de milhar
num = str(input('Analisando números\nDigite um número de 4 dígitos:\n'))
print("""O número {} possui:
{} unidades;
{} dezenas;
{} centenas
{} unidades de milhar.""". format(num,num[3],num[2],num[1],num[0]))
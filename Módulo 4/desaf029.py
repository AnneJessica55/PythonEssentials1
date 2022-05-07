#Escreva um programa que mostre que peça para a pessoa escrever sua velocidade em km/h
#Caso ela esteja a mais de 80km/h informe que ela foi multada
# calcule a multa como R$ 7  para cada km/h excedido
vel = float(input("""Controle de velocidade:
Digite abaixo a que velocidade, em km/h, você está dirigindo:\n"""))
if (vel>80):
    print("""Você excedeu o limite de velocidade permitido.\nUma multa no valor R${:.2f} será aplicada ao seu veículo""".format((vel-80)*7))
print("""Tenha uma boa viagem.
Volte sempre.""")
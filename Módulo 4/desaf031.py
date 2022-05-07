#Faça um programa que pergunte a distância da viagem em km
#Calcule o valor da passagem em R$0,50 para cada km, se a distância for menor ou igual a 200km
##Calcule o valor da passagem em R$0,45 para cada km, se a distância for maior que 200km
nome = str(input('Por favor, informe o seu nome:\n')).strip().title()
gen = str(input('Informe "Feminino" caso você seja mulher e "Masculino" caso você seja um homem (Favor ignorar as "")\n')).upper().strip()
if(gen=='FEMININO'):
    dist=float(input("""Olá, querida passageira {}. É um prazer viajar contigo.\nInforme, por gentileza a distância em km do seu ponto de partida até o seu destino:\n""".format(nome)))
if(gen=='MASCULINO'):
    dist = float(input(
        """Olá, querido passageiro {}. É um prazer viajar contigo.\nInforme, por gentileza a distância em km do seu ponto de partida até o seu destino:\n""".format(
            nome)))
if (gen != 'FEMININO' and gen!='MASCULINO'):
    dist = float(input(
        """Olá, queridE passageirE {}. É um prazer viajar contigo.\nInforme, por gentileza a distância em km do seu ponto de partida até o seu destino:\n""".format(
            nome)))
if (dist<=200):
        print("O valor da sua passagem é de R${:.2f}. Finalize a compra para adquirir o ticket, e boa viagem, {}!!".format(dist*0.50,nome))
else:
        print("O valor da sua passagem é de R${:.2f}. Finalize a compra para adquirir o ticket, e boa viagem, {}!!".format(
            dist * 0.45,nome))

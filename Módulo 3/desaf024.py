#Faça um programa onde o usuário digita o nome da cidade, e ele diz se essa cidade começa com santo
cidade = str(input("""Sua cidade tem nome de Santo ou Santa?
Digite abaixo o nome da sua cidade\n""")).strip()
print(cidade[:5].upper()=='SANTO' or cidade[:5].upper()=='SANTA' or cidade[:3].upper()=='SÃO')
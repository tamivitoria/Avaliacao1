cont = 0
pergunta1 = input ("Telefonou para a vítima? (sim/nao): ")
if pergunta1 == "sim":
    cont = cont + 1

pergunta2 = input ("Esteve no local do crime? (sim/nao): ")
if pergunta2 == "sim":
    cont = cont + 1

pergunta3 = input ("Mora perto da vítima? (sim/nao): ")
if pergunta3 == "sim":
    cont = cont + 1

pergunta4 = input ("Devia para a vítima? (sim/nao): ")
if pergunta4 == "sim":
    cont = cont + 1

pergunta5 = input ("Já trabalhou com a vítima? (sim/nao): ")
if pergunta5 == "sim":
    cont = cont + 1

if cont == 2:
    print ("Suspeita")
elif cont >= 3 and cont <= 4:
    print ("Cúmplice")
elif cont == 5:
    print ("Assassino")
else:
    print ("Inocente")  

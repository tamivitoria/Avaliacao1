h = float(input("Informe a sua altura: "))
sexo = input("Informe seu sexo (M/F): ")

if sexo == "M":
    peso_ideal = (72.7*h)-58
    print ("Seu peso ideal é", peso_ideal)
else:
    peso_ideal = (62.1*h)-44.7
    print ("Seu peso ideal é", peso_ideal)

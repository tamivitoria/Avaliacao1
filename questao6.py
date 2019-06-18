turno = input("Informe o turno em que você estuda (M-matutino ou V-vespertino ou N-noturno): ")

if turno == "M-matutino":
    print ("Bom Dia!")
elif turno == "V-vespertino":
    print ("Boa Tarde!")
elif  turno == "N-noturno":
    print ("Boa Noite!")
else:
    print ("Valor Inválido!")
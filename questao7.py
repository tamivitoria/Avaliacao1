salario = float(input("Informe o seu salário atual: "))

if salario <= 280.00:
    aumento = (20/100) * salario
    novoSalario = salario + aumento
    print ("Salário antes do reajuste: R$" , salario)
    print ("Percentual do aumento: 20%")
    print ("Valor do aumento: R$" , aumento)
    print ("Novo salário: R$" , novoSalario)
    
elif salario > 280.00 and salario <= 700.00:
    aumento = (15/100) * salario
    novoSalario = salario + aumento
    print ("Salário antes do reajuste: R$" , salario)
    print ("Percentual do aumento: 15%")
    print ("Valor do aumento: R$" , aumento)
    print ("Novo salário: R$" , novoSalario)

elif salario > 700.00 and salario <= 1500.00:
    aumento = (10/100) * salario
    novoSalario = salario + aumento
    print ("Salário antes do reajuste: R$" , salario)
    print ("Percentual do aumento: 10%")
    print ("Valor do aumento: R$" , aumento)
    print ("Novo salário: R$" , novoSalario)

else:
    aumento = (5/100) * salario
    novoSalario = salario + aumento
    print ("Salário antes do reajuste: R$" , salario)
    print ("Percentual do aumento: 5%")
    print ("Valor do aumento: R$" , aumento)
    print ("Novo salário: R$" , novoSalario)

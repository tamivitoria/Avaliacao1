ganho_hora = float(input("Quanto ganha por hora: "))
hr_trab = int(input("Numero de horas trabalhadas no mes: "))


salario_bruto = ganho_hora * hr_trab
imp_renda = salario_bruto * (11/100)
inss = salario_bruto * (8/100)
sindicato = salario_bruto * (5/100)
salario_liquido = salario_bruto - imp_renda - inss - sindicato

print ("+ Salário Bruto: R$", salario_bruto)
print ("- IR (11%): R$", imp_renda)
print ("- INSS (8%): R$", inss)
print ("- Sindicato (5%): R$", sindicato)
print ("Salário Liquido: R$", salario_liquido)
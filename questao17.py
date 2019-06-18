def quant (num):
    quant_digitos = str(num)
    return (len(quant_digitos))


num = int(input("Digite o número: "))
print (quant(num) , "digitos")
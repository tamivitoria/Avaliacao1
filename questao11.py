num = int(input("Informe um número inteiro entre 1 a 10: "))
cont = 1

if num >= 1 and num <=10:
    while cont <= 10:
        tabuada = num * cont
        print ("%i X %i = %i" % (num, cont, tabuada))
        cont = cont + 1

else:
    print ("Erro!!!")
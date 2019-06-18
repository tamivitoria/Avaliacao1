kg_morango = int(input("Quantos quilos de morango deseja comprar: "))
kg_maca = int(input("Quantos quilos de maça deseja comprar: "))
kg_total = kg_morango + kg_maca
 
if kg_total <= 5:
    preco_morango = kg_morango * 2.50
    preco_maca = kg_maca * 1.80
    preco_total = preco_maca + preco_morango
    
else:
    preco_morango = kg_morango * 2.20
    preco_maca = kg_maca * 1.50
    preco_total = preco_maca + preco_morango
    
    if kg_total > 8 or preco_total > 25.00:
        preco_total = (preco_total - (preco_total * 0.1))


print ("O valor a ser pago é: R$" , preco_total)

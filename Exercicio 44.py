preço = float(input('Valor da compra R$: '))
opção = int(input('''FORMAS DE PAGAMENTO
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual a opção? '''))
if opção == 1:
    novo = preço - (preço * 10 / 100)
elif opção == 2:
    novo = preço - (preço * 5 / 100)
elif opção == 3:
    novo = preço
    parcela = novo / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    novo = preço + (preço * 20 / 100)
    total = int(input('Quantas parcelas: '))
    parcela = novo / total
    print('Sua compra será de parcelada em {}x de R#{:.2f} COM JUROS'.format(total, parcela))
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, novo))
    

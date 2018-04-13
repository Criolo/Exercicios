soma = 0
cont = 0
for x in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(x)))
    if num % 2 == 0:
        soma += x
        cont += 1
print('\nA soma dos {} numeros PARES digitados é {}'.format(cont, soma))
        

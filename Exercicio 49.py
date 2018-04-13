numero = int(input('Numero que deseja multiplicar: '))
final = int(input('Até quanto: '))
cont = 1
for c in range(1, final + 1):
    print('{} x {} = {}'.format(numero, c, numero * cont))
    cont += 1    

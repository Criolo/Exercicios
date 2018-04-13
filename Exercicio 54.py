from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pessoas in range(1, 8):
    nasc = int(input('Ano que a {}º pessoa nasceu: '.format(pessoas)))
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('O numero de pessoas maiores de idade é {}'.format(maior))
print('O numero de pessoas menores de idade é {}'.format(menor))

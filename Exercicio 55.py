lista = []
for gorduras in range(1, 3):
    peso = float(input('Peso em kg da {}ª pessoa: '.format(gorduras)))
    lista.append(peso)
lista.sort()
print('O maior peso é {:.1}kg'.format(lista[0]))
print('O menor peso é {:.1f}kg'.format(lista[-1]))

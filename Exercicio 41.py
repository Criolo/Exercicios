from datetime import date

data = date.today().year
print('CLASSIFICAÇÃO DOS NADADORES')
idade = data - int(input('Ano de nascimento: '))

if idade <= 9:
    print('O atleta tem {} anos.'.format(idade))
    print('CLASSIFICAÇÃO: MIRIM')
elif idade <= 14:
    print('O atleta tem {} anos.'.format(idade))
    print('CLASSIFICAÇÃO: INFANTIL')
elif idade <= 19:
    print('O atleta tem {} anos.'.format(idade))
    print('CLASSIFICAÇÃO: JUNIOR')
elif idade <= 25:
    print('O atleta tem {} anos.'.format(idade))
    print('CLASSIFICAÇÃO: SENIOR')
else:
    print('O atleta tem {} anos.'.format(idade))
    print('CLASSIFICAÇÃO: MASTER')
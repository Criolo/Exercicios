peso = float(input('Peso (kg):  '))
alt = float(input('Altura (m): '))
IMC = peso / (alt ** 2)
if IMC < 18.5:
    print('Seu IMC é de {:2.1F} \nABAIXO DO PESO'.format(IMC))
elif 18.5 => IMC < 25:
    print('Seu IMC é de {:2.1F} \nPESO IDEAL'.format(IMC))
elif 25 <= IMC < 30:
    print('Seu IMC é de {:2.1F} \nSOBREPESO'.format(IMC))
elif 30 <= IMC < 40:
    print('Seu IMC é de {:2.1F} \nOBESIDADE'.format(IMC))
elif IMC >= 40:
    print('Seu IMC é de {:2.1F} \nOBESIDADE MÓRBIDA'.format(IMC))

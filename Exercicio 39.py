from datetime import date

nasc = int(input('Digite o ano em que nasceu: '))
atual = date.today().year
idade = atual - nasc
print('Você nasceu em {} e tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = 18 - idade
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento foi há {}'.format(ano))

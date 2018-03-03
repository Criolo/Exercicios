from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Sua opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
escoha = int(input('Qual sua jogada? '))
print('O computador jogou {}'.format(itens[computador]))

if computador == 0:
    if escoha == 0:
        print('O jogador jogou Pedra')
        print('EMPATE')
    elif escoha == 1:
        print('O jogador jogou Papel')
        print('JOGADOR VENCE')
    elif escoha == 2:
        print('O jogador jogou Tesoura')
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA!')
if computador == 1:
    if escoha == 0:
        print('O jogador jogou Pedra')
        print('JOGADOR VENCE')
    elif escoha == 1:
        print('O jogador jogou Papel')
        print('EMPATE')
    elif escoha == 2:
        print('O jogador jogou Tesoura')
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA!')
if computador == 2:
    if escoha == 0:
        print('Jogador jogou Pedra')
        print('JOGADOR VENCE')
    elif escoha == 1:
        print('Jogador jogou Papel')
        print('COMPUTADOR VENCE')
    elif escoha == 2:
        print('Jogador jogou Tesoura')
        print('EMPATE')
    else:
        print('ESCOLHA INVALIDA!')

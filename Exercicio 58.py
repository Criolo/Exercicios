from random import randrange
numero = randrange(1, 11)
chances = 0
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
print(numero)
palpite = int(input('Qual seu palpite? '))
while chances < 4:
    if palpite == numero:
        break
    if palpite > numero:
        print('Menos... Tente mais uma vez.')
        palpite = int(input('Qual seu palpite? '))
        chances += 1
    elif palpite < numero:
        print('Mais... Tente mais uma vez.')
        palpite = int(input('Qual seu palpite? '))
        chances += 1
if palpite == numero:
    print('Parabéns, você acertou!')
else:
    print('Você perdeu!')
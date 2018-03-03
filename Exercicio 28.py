from random import *
numero_secreto = randrange(0, 6)
chute = int(input("Digite um numero entre 0 e 5: "))
if chute == numero_secreto:
    print("Venceu")
else:
    print("Perdeu")
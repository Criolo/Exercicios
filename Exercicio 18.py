from math import sin, cos, tan, radians
angulo = float(input("Digite o angulo: "))
seno = sin(radians(angulo))
print("O angulo de {} tem o seno de {:.2f}".format(angulo, seno))
cose = cos(radians(angulo))
print("O angulo de {} tem o cosseno de {:.2f}".format(angulo, cose))
tange = tan(radians((angulo)))
print("O angulo de {} tem a tangente de {:.2f}".format(angulo, tange))

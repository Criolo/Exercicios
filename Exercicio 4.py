print("Tipos de um valor".center(50, " "))
print()
N = input("Digite algo:")
print("O tipo primitivo desse valor é:", type(N))
print("Tem somente espaços ? {}".format(N.isspace()))
print("É um numero ? {}".format(N.isnumeric()))
print("Está em maiuscula ? {}".format(N.isupper()))
print("Está em minuscula ? {}".format(N.islower()))
print("Está capitalizada ? {}".format(N.istitle()))
print("É alfanúmerico ? {}".format(N.isalnum()))
print("É alfabetico ? {]".format(N.isalpha()))

def bissexto(ano):
    return  ano % 4 == 0 and ( ano % 400 == 0 or  ano % 100 != 0)
while True:
    print()
    print("Ano bissexto")
    print()
    ano = int(input("ano: "))
    print("O ano {} é bissexto".format(ano) if (bissexto(ano) == True) else "O ano {} não é bissexto".format(ano))

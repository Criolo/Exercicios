casa = float(input("Qual o valor da casa ? \nR$"))
sal = float(input("Qual o salário ? \nR$"))
ano = int(input("Quantos anos: "))
pres = casa / (ano * 12)
sale = sal*30/100
minimo = sal*30/100
print("Para pagar uma casa de {:.2f} em {} anos".format(casa, ano), end='')
print(" a prestação será de {:.2f}".format(pres))
if pres <= minimo:
    print("Emprestimo aprovado")
else:
    print("Emprestimo não aprovado")


salario = float(input("Qual salario do funcionario ? R$ "))
if salario <= 1250.00:
    novo = salario + (salario * 15 / 100)
    print("seu salario de R${} agora é R${}".format(salario, novo))

else:
    novo = salario + (salario * 10 / 100)
    print("seu salario de R${} agora é R${}".format(salario, novo))

carro = float(input("Velocidade do carro(Km/h): "))
multa = (carro - 80)* 7
if carro > 80:
    print("Sua multa é de R${:.2f}".format(multa))
print("Dirija com segurança!")

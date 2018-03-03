print("Converter real em dolares ")
print()
N = float(input("Digite seu saldo \nR$: "))
Dollar = N / 3.27
print("Com R${:.2f} Você pode comprar US${:.2f}".format(N, Dollar))

from time import sleep
print("DESCONTO".center(50, " "))
print()
preco = float(input("Qual o preço do produto ? \nR$: "))
des = int(input("Qual o valor do desconto: "))
novo = preco - (preco * des / 100)
print("O produto que custa R${:.2f}, com desconto de {}% ficará custando R${:.2f}".format(preco, des, novo))
sleep(10)

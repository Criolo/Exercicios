from time import sleep
print("CONVETER METROS EM CENTÍMETROS E METROS EM MILÍMETROS".center(50, " "))
print()
M = int(input("Digite o valor em metros: "))
MC = M * 100
MM = M * 1000
print("O valor em centimetros: {}cm \nO valor em milímetros: {}mm".format(MC, MM))
sleep(10)

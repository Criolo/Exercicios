from math import hypot

print("HIPOTENSUA".center(50, " "))
print()
CM = float(input("Digite o Cateto oposto: "))
CME = float(input("Digite o Cateto adjacente: "))

print("Hipotenussa: {:.2f}".format(hypot(CM, CME)))
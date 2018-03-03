nome = input("Digite seu nome completo: ").strip()
nome = nome.title().split()
print("Nome: {}\nUltimo: {}".format(nome[0], nome[-1]))
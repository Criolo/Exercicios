n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0

while opção != 5:
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior valor
[ 4 ] novos números
[ 5 ] sair do programa''')
    opção = int(input('Qual é a sua opção? '))
    if opção == 1:
        novo = n1 + n2
        print('A soma dos números é {}'.format(novo))
        print()
    elif opção == 2:
        novo = n1 * n2
        print('O produto dos números é {}'.format(novo))
        print()
    elif opção == 3:
        novo = [n1, n2] 
        print(print('O maior valor digitado foi {}'.format(max(novo))))
        print()
    elif opção == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        continue
    else:
        print('Opção invalída, tente novamente.')
        print()

print('Você saiu do programa.')



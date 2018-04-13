num = int(input('Digite um numero: '))
tot = 0
for buceta in range(1, num + 1):
    if num % buceta == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(buceta), end='')
print('\n\033[m0 O numero tal foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO')

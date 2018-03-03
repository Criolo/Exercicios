num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] Converter para BÍNARIO')
print('[ 2 ] Converter para OCTAL')
print('[ 3 ] Converter para HEXADECIMAL')
escp = int(input())
if escp == 1:
    print('{} convertido para BÍNARIO é igual a {}'.format(num, bin(num)[2:]))
elif escp == 2:
    print('{} convertido para BÍNARIO é igual a {}'.format(num, oct(num)[2:]))
else:
    print('{} convertido para BÍNARIO é igual a {}'.format(num, hex(num)[2:]))
        



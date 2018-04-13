print('TERMOS DE UMA PA')
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro + (11 - 1) * razão  
for buceta in range(primeiro, termo, razão):
    print('{}'.format(buceta), end=' → ')
print('UBBA lUBBA DUB DUB')

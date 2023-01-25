'''va0 = int(input('Digite um número'))
va1 = int(input('Digite um número'))
va2 = int(input('Digite um número'))
va3 = int(input('Digite um número'))'''
valores = ((int(input('Digite um número'))),
           (int(input('Digite mais um número'))),
           (int(input('Digite outro número'))),
           (int(input('Digite o último número'))))
if valores == 3:
    print(f'O valor 3 aparece {valores.index(3)+1}')
else:
    print('NÃO TEM 3!!!')


print('OS VALORES PARES FORAM: ')
for num in valores:
    if num % 2 ==0:
        print(f'{num}')
print(f'O valor 9 aparece {valores.count(9)} vezes')
print(f'Você digitou: {valores}')
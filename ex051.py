#progressão aritmetica
num = int(input('Digite um número'))
razao = int(input('Digite o valor da razão: '))
for c in range(num, num + (10  - 1) * razao, razao):
    print(c)
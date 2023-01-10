'''Leitura de número para descobrir qual é maior ou se ambos são iguais'''
num1 = int(input('Digite um número de 1 a 100000'))
num2 = int(input('Digite um número de 1 a 100000'))
if num1 > num2:
    print('O primeiro valor é maior')
elif num2 > num1:
    print('O segundo valor é maior')
elif num1 == num2:
    print('Os números são iguais')
else:
    print('ERROR!!')
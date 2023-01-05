#faça um progrmaa que leia um número, e mostre seu anterior e seu sucessor
num = int(input('Digite um número inteiro: '))
print('\033[1;40mO antecessor de {} é \n{} e o sucessor \né {} '.format(num, num-1, num+1))
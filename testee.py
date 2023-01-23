num = 0
num2 = 1
sequencia = int(input('digite quantos numero quer na sequencia de fibonacci'))
resultado = 1
c = 2
print(num)
print(num2)
while c < sequencia:
    fibonacci = num + num2
    print(fibonacci)
    num = num2
    num2 = fibonacci
    c += 1

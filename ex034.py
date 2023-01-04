salario = float(input('Digite o seu salario: '))
if salario <= 1000:
    print('Seu salario é de R${:.2f} e com o aumento de 15% irá ficar R${:.2f}'.format(salario, 15/100 * salario + salario))
else:
    print('Seu salario é de R${:.2f} e com o aumento de 10% irá ficar R${:.2f}'.format(salario, 10/100 * salario + salario))
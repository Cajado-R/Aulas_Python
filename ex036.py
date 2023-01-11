'''Programa para ler o valor de uma casa, o salario de um comprador, e ver se ele consegue pagar
a parcela mensal do emprestimo (que será utilizado para  a compra da casa) que não deve exceder 30% de seu salario'''
valcasa = float(input('Qual o valor da casa?'))
salario = float(input('Digite o seus rendimentos mensais (Salário) em R$'))
anopag = int(input('Digite a quantidade e tempo que deseja pagar ex: 1 - 160'))
sal30 = salario * 30/100
emprestimo = valcasa / anopag
if sal30 >= emprestimo:
    print('\033[1;32mSeu emprestimo no valor de R${:.2f} foi aprovado, parabéns!'.format(valcasa))
    print('Você solicitou {} parcelas de R${:.2f}'.format(anopag, emprestimo))
elif emprestimo > sal30:
    print('\033[1;31mEmprestimo negado tente novamente em 30 dias')
    print('Você solicitou um emprestimo que não pode lhe ser dado no momento, pois excede 30% de seu salario de R${}'.format(salario))
else:
    print('ERROR!')


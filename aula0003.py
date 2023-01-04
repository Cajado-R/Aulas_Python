frase = '   Cláudio Rodrigues Cajado'
#encontrar o número de letras
print(frase.count('o'))
#encontrar sequencias.
print(frase.find('dio'))
#número de caracteres
print(len(frase))
#exiba os caracteres nesse espaço
print(frase[5:15])
#troque isso por isso
print(frase.replace('Cláudio', 'Gostoso'))
#exiba a frase full maiusculo
print(frase.upper())
#tudo em minusculo
print(frase.lower())
#o primeiro caractere torna-se maiusculo
print(frase.capitalize())
#analisa quantas palavras tem na string e torna todas as primeiras letras das palavras em maiusculo
print(frase.title())
#remove espaços inuteis
print(frase.strip())
#remove espaços a direita e o l faz o contrario
print(frase.rstrip())
#cria divisão em frases (recomeça a contagem de letras indexadas, viram novas listas)
print(frase.split())
#faz o oposto do split pra nomes separados em lista
print('-'.join(frase))
frasee = ['claudio', 'joao', 'pedro']
print('-'.join(frasee))

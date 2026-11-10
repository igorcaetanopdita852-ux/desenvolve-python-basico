nq = int(input('Quantas pessoas serão entrevistadas: '))
cont = 0
soma = 0

while cont < nq:
    idade = int(input('Qual a sua idade? '))
    soma += idade 
    cont += 1
print(f'A media das idade é: {soma / nq:,.2f} ')
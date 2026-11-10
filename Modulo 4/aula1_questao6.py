ne = int(input('Quantos experimentos foram realizados: '))
cont = 0
soma_sapo = 0
soma_rato = 0
soma_coelho = 0


while cont < ne:
    quantia = int(input('Quantas cobaias foram usadas? '))
    tipo = input('Qual o tipo da cobaia? (s de sapo, c de coelho, r de rato) ')

    if tipo == "s":
        soma_sapo += quantia
    elif tipo == 'c':
        soma_coelho += quantia
    elif tipo == 'r':
        soma_rato += quantia
    else:
        print('Entrada invalida')
    cont += 1


print('Total de cobaias: ', soma_rato + soma_sapo + soma_coelho)

print('Total de sapos: ',soma_sapo)
print('Total de ratos: ', soma_rato)
print('Total de coelhos: ',soma_coelho)

print(f'Percentual de sapos: {soma_sapo / (soma_rato + soma_sapo + soma_coelho) * 100:,.2f}%')
print(f'Percentual de ratos:  {soma_rato / (soma_rato + soma_sapo + soma_coelho) * 100:,.2f}%')
print(f'percentual de coelhos: {soma_coelho / (soma_rato + soma_sapo + soma_coelho) * 100:,.2f}%')

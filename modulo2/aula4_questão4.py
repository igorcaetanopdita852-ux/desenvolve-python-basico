valor_i = int(input('Qual o valor a trocar? '))
notas = 100, 50, 20, 10, 5, 2, 1

for nota in notas: 
    quantidade = valor_i // nota
    print(f'{quantidade} nota(s) de R${nota}')
    valor_i %= nota
nome_p1 = str(input('Qual o nome do produto 1? '))
preç_p1 = float(input('Qual o preço de uma unidade do produto 1? '))
q1 = int(input('Qual a qunatidade do produto 1? '))

      
nome_p2 = str(input('Qual o nome do produto 2? '))
preç_p2 = int(input('Qual o preço de uma unidade do produto 2? '))
q2 = int(input('Qual a qunatidade do produto 2? '))

nome_p3 = str(input('Qual o nome do produto 3? '))
preç_p3 = int(input('Qual o preço de uma unidade do produto 3? '))
q3 = int(input('Qual a qunatidade do produto 3? '))



valor_p1 = preç_p1 * q1
valor_p2 = preç_p2 * q2
valor_p3 = preç_p3 * q3

valor_f = valor_p1 + valor_p2 + valor_p3

print(f'Total: R$ {valor_f:,.2f}')

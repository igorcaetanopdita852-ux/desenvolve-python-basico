idade = int(input('Qual a sua idade? '))
jogou_jogos = input('Já jogou pelo menos 3 jogos? ') == "True" or "Sim" or "true" or "sim"
vitorias = int(input("Quantos jogos você ganhou? ")) > 1

print(16 <= idade <= 18 and jogou_jogos and vitorias)
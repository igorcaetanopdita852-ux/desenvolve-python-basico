genero = input('Qual o seu genero?(M ou F): ')
idade = int(input('Digite sua idade '))
tempo_trabalho = int(input('Qual o seu tempo de trabalho? '))

situação_a = (genero == "M" and idade >= 60) or (genero == "F" and idade >= 65)

situação_b = tempo_trabalho >= 30

situação_c = idade >= 60 and tempo_trabalho >= 25

aposentar = situação_a or situação_b or situação_c

print(aposentar)
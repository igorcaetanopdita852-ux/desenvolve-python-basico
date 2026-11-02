distancia =int(input('Qual a distancia até o destino (km)?: '))
peso =float(input('Qual o peso do produto?: '))

if distancia <= 100:
    valor = peso
elif distancia <= 300:
    valor = peso * 1.50 
else:
    valor = peso * 2.0

if peso > 10:
    valor += 10 

print(f"Valor do frete: R${valor:.2f}")
comp = int(input('Digite o Comprimento:'))   #pega o valor no comprimente
larg = int(input('Digite a Largura:'))       #pega o valor do comprimento
preç_por_m = int(input('Qual é o Preço por Metro? Digite somente o numero: '))
# ^^ Pega o valor de um metro kkk
area_m2 = comp * larg    #calcula a area
preço_final = preç_por_m * area_m2    #calcula o preço final
print(f"O terreno tem {area_m2:,.2f}m2 e custa R${preço_final:,.2f}")
# ^^ Printa a area e o preço final, ambos em suas medidas/valores
classe = input('Escolha sua classe(mago, guerreiro, arqueiro): ')
if classe == "mago": 
    força_m = int(input('Digite sua força (de 0 a 10):')) <= 10
    magia_m = int(input('Digite sua magia (de 15 a 20) : ')) >= 15 <= 20
    print(f'personagem balanceado em relação a classe: {força_m and magia_m}')
elif classe == "guerreiro":
    magia_g = int(input('Digite sua magia (de 0 a 10):')) <= 10
    força_g = int(input('Digite sua força (de 15 a 20) : ')) >= 15 <= 20
    print(f'personagem balanceado em relação a classe: {força_g and magia_g}')
elif classe == 'arqueiro':
    força_a = int(input('Digite sua força (de 5 a 15) :')) >= 5 <= 15
    magia_a = int(input('Digite sua magia (de 5 a 15) :')) >= 5 <= 15
    print(f'personagem balanceado em relação a classe: {força_a and magia_a}')
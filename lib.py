import random

opções = ['pedra', 'papel', 'tesoura']
escolha_pc = random.choice(opções)
def jogar():
    while True:
        escolha_usuario = input("Escolha Pedra, Papel ou Tesoura: ").lower()
        if escolha_usuario in opções:
            break
        print("Escolha inválida. Tente novamente.")
    if escolha_usuario == escolha_pc:
        resultado = "Empate!"
    elif (escolha_usuario == 'pedra' and escolha_pc == 'tesoura') or \
        (escolha_usuario == 'papel' and escolha_pc == 'pedra') or \
        (escolha_usuario == 'tesoura' and escolha_pc == 'papel'):
        resultado = "Você ganhou!"
    else:
        resultado = "Você perdeu!"

    print(f"Você escolheu: {escolha_usuario}")
    print(f"O computador escolheu: {escolha_pc}")
    print(f"Resultado: {resultado}")

while True:
    jogar()
    jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
    if jogar_novamente != 's':
        print("Obrigado por jogar!")
        break
numero = int(input("Digite um número (0 para sair): "))
quantidade = 0
soma = 0
while numero != 0:
    soma += numero
    quantidade += 1
    numero = int(input("Digite um número (0 para sair): "))
media = soma / quantidade 
print(f"A soma é {soma} e a média é {media}")

num = int(input("Digite um número para ver a tabuada: "))
def tabuada(num):
    tabuada = []
    print(f"Tabuada do {num}:")
    for i in range(1, 21):
        resultado = num * i
        tabuada.append(resultado)
    return tabuada


print(tabuada(num))

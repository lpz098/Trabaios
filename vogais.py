vogais = ['a', 'e', 'i', 'o', 'u']
def contar(pal):
    count = 0
    for letra in vogais:
        count += pal.count(letra)
    return count
print(contar("banana"))
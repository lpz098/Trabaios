Rezero = {
    "Genero": "Isekai",
    "episodios": 25,
    "temporada": 4,
    "nota": 8.5
}  

def anime_info(anime):
    for i in anime:
        print(f"{i}: {anime[i]}")
        while True:
            user_input = input("Deseja continuar? (s/n): ")
            if user_input.lower() == 's':
                break
            elif user_input.lower() == 'n':
                print("Saindo do programa.")
                return
            else:
                print("Entrada inválida. Por favor, digite 's' para sim ou 'n' para não.")
    
anime_info(Rezero)
# Lista inicial com os dados dos times de futebol
lstTimes = [
    ['Atlético Mineiro', 20, 8, 7, 53, 26], ['Bahia', 12, 10, 11, 39, 37],
    ['Botafogo', 14, 12, 8, 46, 29], ['Ceará', 10, 11, 14, 34, 43],
    ['Corinthians', 18, 9, 10, 50, 31], ['Cruzeiro', 9, 14, 10, 33, 33],
    ['Flamengo', 23, 7, 7, 62, 27], ['Fluminense', 15, 11, 9, 44, 32],
    ['Fortaleza', 11, 13, 11, 36, 35], ['Grêmio', 13, 9, 15, 38, 43],
    ['Internacional', 16, 8, 13, 45, 39], ['Juventude', 8, 13, 15, 30, 44],
    ['Mirassol', 10, 10, 17, 32, 46], ['Palmeiras', 22, 9, 6, 58, 25],
    ['Red Bull Bragantino', 14, 8, 16, 40, 45], ['Santos', 13, 11, 14, 39, 41],
    ['São Paulo', 17, 7, 14, 48, 38], ['Sport', 11, 12, 15, 35, 42],
    ['Vasco da Gama', 9, 15, 14, 33, 40], ['Vitória', 7, 13, 18, 28, 47]
]

# Usando List Comprehension para gerar a nova lista com os dados calculados
# [expressão for item in iterável]
lstTimes_atualizada = [
    [
        time[0],  # Nome do time
        time[1],  # Vitórias
        time[2],  # Empates
        time[3],  # Derrotas
        (time[1] * 3 + time[2]),  # Pontos (calculado)
        time[4],  # Gols marcados
        time[5],  # Gols sofridos
        (time[4] - time[5])  # Saldo de gols (calculado)
    ]
    for time in lstTimes  # Para cada time na lista original
]

# Imprimir o resultado para verificação
print("Lista de times gerada com List Comprehension:")
for time in lstTimes_atualizada:
    print(time)
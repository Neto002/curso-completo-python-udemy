perguntas: list = [
    {"pergunta": "Quanto é 2 + 2?", "opcoes": ["1", "3", "4", "5"], "resposta": "4"},
    {
        "pergunta": "Quanto é 5 x 5?",
        "opcoes": ["25", "55", "10", "51"],
        "resposta": "25",
    },
    {"pergunta": "Quanto é 10 / 2?", "opcoes": ["4", "5", "2", "1"], "resposta": "5"},
]

quantidade_acertos = 0

for item in perguntas:
    print(f"Pergunta: {item['pergunta']}\n")

    opcoes = item["opcoes"]
    for i, opcao in enumerate(opcoes):
        print(f"{i}) {opcao}")

    resposta: str = input("\nEscolha uma opção: ").strip()

    acertou = False
    resposta_int = None
    quantidade_opcoes = len(opcoes)

    while not resposta.isdigit():
        print("Por favor, digite uma opção válida")
        resposta: str = input("\nEscolha uma opção: ").strip()

    resposta_int = int(resposta)

    if resposta_int is not None:
        opcao_valida = resposta_int >= 0 and resposta_int < quantidade_opcoes
        if opcao_valida:
            resposta_correta = opcoes[resposta_int] == item["resposta"]
            if resposta_correta:
                acertou = True

    if acertou:
        print("Acertou")
        quantidade_acertos += 1
    else:
        print("Errou")

    print()

print(f"Você acertou {quantidade_acertos} de {len(perguntas)} perguntas.")

import json


def listar(tarefas: list) -> None:
    print()
    if not tarefas:
        print("Nenhuma tarefa para listar")
        return

    print("Tarefas: ")
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas: list, tarefas_refazer: list) -> None:
    print()
    if not tarefas:
        print("Nenhuma tarefa para desfazer")
        return

    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)

    listar(tarefas)


def refazer(tarefas: list, tarefas_refazer: list) -> None:
    print()
    if not tarefas_refazer:
        print("Nenhuma tarefa para refazer")
        return

    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)

    listar(tarefas)


def adicionar_tarefa(tarefa: str, tarefas: list) -> None:
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print("Nenhuma tarefa para adicionar")
        return

    tarefas.append(tarefa)

    listar(tarefas)


def ler(tarefas: list, caminho_arquivo: str) -> list:
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo inexistente')
        salvar(tarefas, caminho_arquivo)
    return dados


def salvar(tarefas: list, caminho_arquivo: str) -> None:
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)

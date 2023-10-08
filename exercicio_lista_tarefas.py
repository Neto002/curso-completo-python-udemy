import os


def listar(tarefas: list) -> None:
    print()
    if not tarefas:
        print("Nenhuma tarefa para listar")
        return

    print("Tarefas: ")
    for tarefa in tarefas:
        print(f'\t{tarefa}')


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


tarefas = []
tarefas_refazer = []

while True:
    print("Comandos: listar, desfazer, refazer, clear e sair")
    tarefa = input("Digite uma tarefa ou comando: ").strip().lower()

    if tarefa == "listar":
        listar(tarefas)
    elif tarefa == "desfazer":
        desfazer(tarefas, tarefas_refazer)
    elif tarefa == "refazer":
        refazer(tarefas, tarefas_refazer)
    elif (tarefa == 'clear'):
        os.system('cls')
    elif (tarefa == 'sair'):
        print("Saindo")
        break
    else:
        adicionar_tarefa(tarefa, tarefas)

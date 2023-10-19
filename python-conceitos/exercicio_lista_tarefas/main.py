import os

from funcoes.funcoes_tarefas import (adicionar_tarefa, desfazer, ler, listar,
                                     refazer, salvar)

if __name__ == '__main__':
    CAMINHO_ARQUIVO = './exercicio_lista_tarefas/base.json'
    tarefas = ler([], CAMINHO_ARQUIVO)
    tarefas_refazer = []

    while True:
        print("Comandos: listar, desfazer, refazer, clear e sair")
        tarefa = input("Digite uma tarefa ou comando: ").strip().lower()

        comandos = {
            'listar': lambda: listar(tarefas),
            'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
            'refazer': lambda: refazer(tarefas, tarefas_refazer),
            'clear': lambda: os.system('cls'),
            'sair': lambda: exit('Saindo')
        }

        comando = comandos.get(tarefa)

        if comando is None:
            adicionar_tarefa(tarefa, tarefas)
        else:
            comando()

        salvar(tarefas, CAMINHO_ARQUIVO)

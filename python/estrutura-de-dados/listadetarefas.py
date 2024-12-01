tarefas = []
estado_tarefa = []

def exibirTarefas():
    for index in range(len(tarefas)):
        print(tarefas[index],' | ', estado_tarefa[index])


def addTarefa(tarefa):
    tarefas.append(tarefa)
    estado_tarefa.append("Não-concluída")

def pesquisaTarefas(pesquisa):
    if not tarefas:
        print('Erro: não há nenhuma tarefa na lista.')
        return None
    else:
        if pesquisa in tarefas:
            index_pesquisa = tarefas.index(pesquisa)
            print(f'Tarefa encontrada: {tarefas[index_pesquisa]} - Estado: {estado_tarefa[index_pesquisa]}')
            return index_pesquisa
        else:
            print('Erro: tarefa não encontrada.')
            return None

def remTarefas(tarefa):
    del tarefas[pesquisaTarefas(tarefa)]
    exibirTarefas()

def concluirTarefa(tarefa):
    estado_tarefa[pesquisaTarefas(tarefa)] = "Concluída"
    exibirTarefas()



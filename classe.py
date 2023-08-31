class Tarefas:
    def __init__(self):
        self.tarefa =[]

    def adicionar_tarefa(self, descricao):
        self.descricao = descricao
        self.tarefa.append(descricao)

    def listar_tarefa(self):
        for tarefas in self.tarefa():
            print("1 - ir ao mercado\n2 - Passear com o Cachorro\n3 - Estudar para a prova")

    def excluir_tarefa(self):
        pass

    def getTarefas(self):
        return self.tarefa
#
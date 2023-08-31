from classe import*
import time
import os

def espera():
    time.sleep(1)

tarefa = Tarefas()
def main():
    sair = False
    while sair == False:
        print("Aplicativo TO-DO")
        escolha = int(input("Escolha uma opção:\n[1] Adicionar Tarefas\n[2] Listar Tarefas\n[3] Excluir Tarefa\n[4] Sair\n> "))
        match escolha:
            case 1:
                os.system("cls")
                print("Você escolheu adicionar tarefa.")
                input("Adicione sua tarefa: ")
                tarefa.adicionar_tarefa
                print("Tarefa adicionada com sucesso!")
                os.system("pause")
                
            case 2:
                os.system("cls")
                print("Você escolheu listar suas tarefas!")
                tarefa.listar_tarefa()
                os.system("pause")

            case 3:
                print("Você escolheu excluir tarefa")
                print("Qual você deseja excluir?")
                print(f"1 - Ir ao mercado\n2 - Passear com o cachorro\n3 - Estudar para a prova")
                

                pass
            case 4:
                os.system("cls")
                print("Você escolheu a opção sair.")
                print("Obrigado por usar nosso aplicativo!")
                espera()
                print("Saindo...")
                espera()
                sair = True
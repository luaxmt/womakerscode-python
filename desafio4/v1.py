tarefas = []

def visualizar_tarefas():
  if tarefas:
    print('\nSuas tarefas são: ')
    for numero, tarefa in enumerate(tarefas, 1):
      print(f'{numero}. {tarefa}')
  else:
    print('\nVocê não tem nenhuma tarefa.')

def adicionar_tarefa(tarefa):
  tarefas.append(tarefa)
  print('\nTarefa', tarefa, 'adicionada com sucesso.')

def remover_tarefa(numero):
    if 0 <= numero < len(tarefas):
        tarefa_removida = tarefas.pop(numero)
        print('\nTarefa', tarefa_removida, 'removida com sucesso!')
    else:
        print("\nNúmero de tarefa inválido.")

def mostrar_menu():
  while True:
    print('\nLista de tarefas')
    print('1. Visualizar lista de tarefas')
    print('2. Adicionar tarefa')
    print('3. Remover tarefa')
    print('4. Sair do menu')

    escolha = input('Digite o número da opção desejada: ')

    if escolha == "1":
      visualizar_tarefas()

    elif escolha == "2":
      tarefa = input('Digite a nova tarefa: ')
      adicionar_tarefa(tarefa)

    elif escolha == "3":
      visualizar_tarefas()
      numero = int(input('Digite o número da terafa a ser removida: ')) -1
      remover_tarefa(numero)

    elif escolha == "4":
      print('\nVocê saiu da sua lista de tarefas.')
      break

    else:
      print('Opção inválida.')

mostrar_menu()
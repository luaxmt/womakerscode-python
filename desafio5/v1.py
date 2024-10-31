# Funções para os cálculos
def calcular_soma(numero1, numero2):
  soma = numero1 + numero2
  print('\n', numero1, ' + ', numero2, ' = ', soma)

def calcular_subtracao(numero1, numero2):
  subtracao = numero1 - numero2
  print('\n', numero1, ' - ', numero2, ' = ', subtracao)

def calcular_multiplicacao(numero1, numero2):
  multiplicacao = numero1 * numero2
  print('\n', numero1, ' * ', numero2, ' = ', multiplicacao)

def calcular_divisao(numero1, numero2):
  if numero2 == 0:
    print('Erro: não é possível dividir por zero!')
    return
  divisao = numero1 / numero2
  print('\n', numero1, ' / ', numero2, ' = ', divisao)

# Função para validar respostas s/n
def validar_sim_nao(resposta, pergunta):
  while resposta.lower() not in ['s', 'n']:
    resposta = input('\nPor favor, responda apenas "s" para sim e "n" para não: ')
  return resposta.lower() == 's'

#Função que expõe o menu de opções
def mostrar_menu(numero1, numero2):
  while True:
    print('\nOs números escolhidos foram', numero1,'e', numero2)
    print('\nQue operação você deseja realizar?')
    print('1. Adição')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')

    escolha = input('\nDigite o número referente à operação: ')

    if escolha == "1":
      calcular_soma(numero1, numero2)

    elif escolha == "2":
      calcular_subtracao(numero1, numero2)

    elif escolha == "3":
      calcular_multiplicacao(numero1, numero2)

    elif escolha == "4":
      calcular_divisao(numero1, numero2)

    else:
      print('\nOperação inválida. Por favor, escolha um número entre 1 e 4.')
      continue

    continuar = input('\nDeseja realizar outra operação com estes números? (s/n): ')
    if not validar_sim_nao(continuar, '\nDeseja realizar outra operação com estes números? (s/n): '):
        return False

# Função para evitar que o usuário digite letras em vez de números para os cálculos
def obter_numero(mensagem):
    while True:
      try:
        return float(input(mensagem))
      except ValueError:
        print('\nPor favor, digite apenas números!')

# Função principal (calculadora)
def calculadora():
  while True:
    print('\nBem-vindo à Calculadora Não Muito Eficiente. Escolha dois números: ')

    numero1 = obter_numero('Insira primeiro número: ')
    numero2 = obter_numero('Insira segundo número: ')

    mostrar_menu(numero1, numero2)

    reiniciar = input('\nDeseja fazer novos cálculos com números diferentes? (s/n): ')
    if not validar_sim_nao(reiniciar, '\nDeseja fazer novos cálculos com números diferentes? (s/n): '):
        print('\nObrigada por utilizar a Calculadora Não Muito Eficiente!')
        break

calculadora()
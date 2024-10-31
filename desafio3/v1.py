import random

def adivinhar_numero():
  numero_aleatorio = random.randint(1, 100)
  palpite = 0

  while palpite != numero_aleatorio:
    palpite = int(input('O número secreto fica entre 1 e 100. Faça seu palpite: '))

    if palpite > numero_aleatorio:
      print('O número secreto é menor que', palpite)
    elif palpite < numero_aleatorio:
      print('O número secreto é maior que', palpite)
    else:
      print('Parabéns, você acertou!')

adivinhar_numero()
# VERSÃO 1

nota1 = float(input('Insira o valor da nota 1: '))
nota2 = float(input('Insira o valor da nota 2: '))
nota3 = float(input('Insira o valor da nota 3: '))

media = (nota1 + nota2 + nota3) / 3
print(f'Sua média é: {media:.1f}')

if media >=6:
  print('Parabéns, você foi aprovado!')
else:
  print('Infelizmente, você foi reprovado :(')
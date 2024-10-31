# VERSÃO FINAL: impede que o input seja menor que 0 ou maior que 10; adiciona parágrafo no resultado.

def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

nota1 = float(input('Insira o valor da nota 1: '))
while nota1 < 0 or nota1 > 10:
  nota1 = float(input('O valor da nota deve estar entre 0 e 10. Insira o valor da nota 1: '))
nota2 = float(input('Insira o valor da nota 2: '))
while nota2 < 0 or nota2 > 10:
  nota2 = float(input('O valor da nota deve estar entre 0 e 10. Insira o valor da nota 2: '))
nota3 = float(input('Insira o valor da nota 3: '))
while nota3 < 0 or nota3 > 10:
  nota3 = float(input('O valor da nota deve estar entre 0 e 10. Insira o valor da nota 3: '))

media = calcular_media(nota1, nota2, nota3)
print(f'\nSua média é: {media:.1f}')

if media >=6:
  print('\nParabéns, você foi aprovado!')
else:
  print('\nInfelizmente, você foi reprovado :(')
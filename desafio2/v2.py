# VERSÃO 2: cria a função contar_vogais.

def contar_vogais(frase):
  vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  contador_vogais = 0

  for letra in frase:
    if letra in vogais:
      contador_vogais += 1
  return contador_vogais

frase = input('Escreva uma palavra ou frase: ')
print('Sua frase contém ', contar_vogais(frase), ' vogais.')
# VERSÃO 1

frase = input('Escreva uma palavra ou frase: ')
vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
contador_vogais = 0

for letra in frase:
  if letra in vogais:
    contador_vogais += 1

print('Sua frase contém ', contador_vogais, ' vogais.')
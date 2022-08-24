print('Olá Mundo!')
frase = 'Olá Mundo!'
print(frase)
print('Nosso primeiro código foi o : {}'.format(frase)) # o format substitui o {} na string pela variável deixada depois
print('Nosso primeiro código foi o : {0}'.format(frase, 'teste'))
print('Nosso primeiro código foi o : {1}'.format(frase, 'teste'))
nome = 'Kleython José'
funcao = 'Professor'
idade = 28
print('O {} {} tem {} anos de idade.'.format(funcao, nome, idade))
frase = 'O {0} {1} tem {2} anos de idade.'.format(funcao, nome, idade)
print(frase.upper()) #deixa tudo com capslock
print(frase.lower()) #deixa tudo sem caps lock
print(frase.swapcase()) #troca os caps lock
print(frase.title()) #transforma em um título (primeira letra de cada palavra é maiúscula)
print(frase.count("o")) #contar quantos o tem na frase
nomesplit = nome.split() #separa a string em uma lista de strings com cada palavra
print(nomesplit[0:5]) #printa os elementos da array que foi formada pelo split do primeiro ao quarto
print(frase.replace('Kleython', 'Rogério')) #troca um padrão de texto por outro
print(frase.isalpha) #checa se a string é composta somente de letras
print(frase.isalnum) #checa se a string é composta de letras e números
print(frase.islower) #checa se a string é 100% sem caps lock
print(frase.isupper) #checa se a string é 100% caps lock
print(frase.rjust(20)) #coloca 20 espaços antes da frase
print(frase.strip) #remove os espaços desnecessários

# Listas

São mutáveis e indexadas.
lista = []

nomes = ['Danilo', 'João', 'Diego']

A primeira posição das listas é a 0. Então:
print(nomes[0])
printaria Danilo

Caso o número seja negativo, a lista é contada de traz pra frente:
print(nomes[-1])
printaria Diego

Para adicionar um valor ao final da lista, usamos o append:
nomes.append('Ithalo')
print(nomes)
printaria ['Danilo', 'João', 'Diego', 'Ithalo']

Para adicionar um valor ao começo dda lista, usamos o extend:
nomes.extend('Ithalo')
print(nomes)
printaria ['Ithalo', 'Danilo', 'João', 'Diego']

Para contar quantas vezes o mesmo elemento aparece na lista, usamos o count:
x = nomes.count('Danilo')
print(x)
printaria 1

Para remover um item da lista, usamos o pop. Podemos colocar a posição do item a ser removido dentro do pop, ou, se vazio, por padrão é -1 (último):

nomes.pop()
print(nomes)
printaria ['Danilo', 'João']

Para testar o tipo de uma variável, usamos type:
print(type(nomes))
printaria <class 'list'>

Para inserir um valor na lista sem ser pro final, mas numa posição específica, usamos insert:
nomes.insert('Arthur', 2)
print(nomes)
printaria ['Danilo', 'João' , 'Arthur', 'Diego']

# Tuplas

São IMUTÁVEIS e indexadas.
tupla = ()

numeros = ('096', '321', '542')

por ser imutável, não dá pra adicionar, remover ou alterar dados.

# Dicionários

Se comportam igual às listas, mas com chave e valor.

dicionario = {}

dados = {'nome': 'kleython', 'idade': 28}
print(dados['nome'])
printaria kleython

adicionar ao dicionário:
dados['Cidade'] = 'Ribeirão'

exemplo de dados:
dicionario = [{'nome': 'kleython', 'idade': 28}, {'nome': 'rogerio', 'idade': 29}]
print(dicionario[0]['nome'])
printaria kleython

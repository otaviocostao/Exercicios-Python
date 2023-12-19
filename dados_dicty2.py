# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

p1 = {
    'nome': 'Otavio',
    'sobrenome': 'Costa',
}

# GET
print('\nMétodo GET\n')
print(p1['nome'])
print(p1.get('nome', 'não existe')) #Caso não haja a Key 'nome', exibe 'Não existe'

# POP
print('\nMétodo POP\n')
#nome = p1.pop('nome') # Apaga a Key 'nome'
#print(p1)
ultima_chave = p1.popitem() # Apaga a ultima Key do Dict
print(ultima_chave)
print(p1)

# UPDATE
print('\nMétodo UPDATE\n')
p1.update(nome='Novo valor', idade=19) #Atualiza alguma Key ou cria uma nova
print(p1)

lista = ['nome', 'João'], ['idade', 25]
p1.update(lista) #Pode realizar o Update a partir de um iterável
print(p1)
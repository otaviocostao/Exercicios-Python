# Usamos as chaves "{}" ou a classe dict para criar dicionários
# Imutáveis: str, int, float, bool, tuple
# Mutáveis: dict, list

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

import copy

pessoa = {
    'nome': 'Otavio',
    'sobrenome': 'Costa',
    'idade': 18,
    'altura': 1.8,
    'enderecos': [
        {'rua': 'Rua José Pinheiro', 'numero': 73, 'bairro': 'Centro'},
        {'rua': 'Outra rua', 'numero': 123, 'bairro': 'Outro bairro'}
        ]
}

print(pessoa['nome'])
print(pessoa['sobrenome'])
print(pessoa)

# METODO COPY

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [1,2,3]
}
#d2 = d1.copy()
d2 = copy.deepcopy(d1)

d2['c1'] = 1000
d2['l1'][1] = 999
print(d1)
print(d2)
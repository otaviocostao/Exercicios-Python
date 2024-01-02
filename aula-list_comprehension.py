# List comprehension em Python
# Forma mais rapida de criar listas a partir de iteráveis.

#lista = [numero for numero in range(10)]
#print(lista)
#print()

#lista = [numero*2 for numero in range(10)]
#print(lista)
#print()

# Mapeamento de dados em List Comprehension
produtos= [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30},
]

novos_produtos= [
    {**produto, 'nome': produto['nome'], 'preco':produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

print(*novos_produtos, sep='\n')
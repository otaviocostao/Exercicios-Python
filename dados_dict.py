# Usamos as chaves "{}" ou a classe dict para criar dicionários
# Imutáveis: str, int, float, bool, tuple
# Mutáveis: dict, list

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
"""
Higher Order Functions
Funções de primeira classe
Funções que retornam outras funções
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}'

def executa(funcao, *args):
    return funcao(*args)

print(
    executa(saudacao, 'Olá, bom dia', 'Otávio')
)

print(
    executa(saudacao, 'Olá, boa noite', 'João')
)
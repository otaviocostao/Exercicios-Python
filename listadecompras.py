#ENUNCIADO: Faça uma lista de compras. O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.

import os

lista_de_compras= []

while True:
    opcaoinicial = input("Selecione uma opção:\n[I]nserir [A]pagar [L]istar:\n").lower()

    if opcaoinicial == 'i':
        os.system('cls')
        produto = input('Qual produto deseja adicionar a lista? ')
        lista_de_compras.append(produto)
        print(lista_de_compras)

    if opcaoinicial == 'a':
        os.system('cls')
        pos_apagar = int(input('Digite o índice que deseja apagar: '))
        lista_de_compras.pop(pos_apagar)
        print(lista_de_compras)

    if opcaoinicial == 'l':
        os.system('cls')
        for indice, produto in enumerate(lista_de_compras):
            print(indice, produto)

        if lista_de_compras == 0:
            print('A lista está vazia e não pode ser listada.')

    else:
        print('Escolha alguma das opções anteriores.')
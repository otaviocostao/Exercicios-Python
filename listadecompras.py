#ENUNCIADO: Faça uma lista de compras. O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
lista_de_compras= []
lista_enumerada = list(enumerate(lista_de_compras))

while True:
    opcaoinicial = input("Selecione uma opção:\n[I]nserir [A]pagar [L]istar:\n").lower()

    if opcaoinicial == 'i':
        produto = input('Qual produto deseja adicionar a lista? ')
        lista_de_compras.append(produto)
        print(lista_de_compras)

    if opcaoinicial == 'a':
        pos_apagar = int(input('Digite o índice que deseja apagar: '))
        lista_de_compras.pop(pos_apagar)
        print(lista_de_compras)

    if opcaoinicial == 'l':
        for indice, produto in lista_enumerada:
            print(lista_enumerada)
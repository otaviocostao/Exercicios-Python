# Exercício: Sistema de perguntas e respostas

perguntas = [
    {
        'pergunta': 'Quanto é 2+2: ',
        'alternativas': ['2', '4', '5', '8'],
        'resposta': '4',
    },
    {
        'pergunta': 'Quanto é 5*5: ',
        'alternativas': ['25', '15', '10', '35'],
        'resposta': '25',
    },
    {
        'pergunta': 'Quanto é 10/2: ',
        'alternativas': ['4', '6', '5', '2'],
        'resposta': '5',
    }
]

qtd_acertos= 0

for indice in perguntas:
    print('Pergunta:', indice['pergunta'])
    print()

    lista_alternativas = list(indice['alternativas'])
    opcoes = indice['alternativas']

    for i, alternativa in enumerate(lista_alternativas):
        print(f'{i})', alternativa)

    escolha = input('\nEscolha uma das alternativas: ')
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        int_escolha = int(escolha)

    acertou = False

    if int_escolha is not None:
        if int_escolha >= 0 and int_escolha < qtd_opcoes:
            if lista_alternativas[int_escolha] == indice['resposta']:
                acertou = True
    
    if acertou:
        print('\nCorreto! 👍\n')
        qtd_acertos += 1
    else:
        print('\nIncorreto! 👎\n')

print(f'Você acertou {qtd_acertos} de {len(perguntas)} perguntas!')
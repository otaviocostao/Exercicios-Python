# Exercícios com funções
# Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro.

def duplicar(numero):
    return numero * 2

def triplicar(numero):
    return numero * 3

def quadruplicar(numero):
    return numero * 4

print('EXERCÍCIO 1:')
numero_input = int(input('Digite um numero: '))

print(duplicar(numero_input))
print(triplicar(numero_input))
print(quadruplicar(numero_input))

# Crie uma função que multiplica um numero por um multiplicador

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

print('EXERCÍCIO 2:')
numero_input2 = int(input('Digite um número para ser multiplicado: '))    
multiplicador_input = int(input(f'Digite o multiplicador do número {numero_input2}: '))

multiplicador = criar_multiplicador(multiplicador_input)

print(multiplicador(numero_input2))
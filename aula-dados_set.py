# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
s1 = set()  # vazio
s1 = {'Luiz', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

print('\nDIFERENÇA ENTRE SET E LIST\n')

l1= [1, 2, 3, 3, 3, 3, 4, 5, 5]
print(f'Lista 1 = "{l1}"')

s2 = set(l1)
print(f'Lista 1 convertida para Set= "{s2}"')

l2 = list(s2)
print(f'Set convertido para lista novamente, agora a lista não possui valores duplicados: "{l2}"\n\n')

# Métodos úteis:
# add, update, clear, discard

print('MÉTODOS ÚTEIS\n')

s3 = set()
s3.add('Otavio')
s3.add(1)
print(f'Após usar o metodo add: {s3}')

s3.update(('João', 5, 4, 3, 2, 1))
print(f'Após usar o método Update: {s3}')

s3.discard('João')
print(f'Após usar o método Discard e remover "João": {s3}')

s3.clear()
print(f'Após usar o método Clear: {s3}')

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

print('\nOPERADORES ÚTEIS:\n')

s4= {1,2,3}
s5= {2,3,4}
s6= s4 | s5
print(f'União dos dois Sets: {s6}\n')

s6 = s4 & s5
print(f'Intercecção dos dois Sets: {s6}\n')

s6 = s4 - s5
print(f'Diferença dos dois Sets: {s6}\n')

s6 = s4 ^ s5
print(f'Diferença simétrica dos dois Sets: {s6}')
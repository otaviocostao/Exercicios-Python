"""
split: Divide uma string
join: une uma string
"""

frase = 'Olha só, que coisa interessante'
lista_frases_cruas= frase.split(',') #Divide as frases pela vírgula

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

print(lista_frases_cruas) #Com o espaço
print(lista_frases) #Sem o espaço
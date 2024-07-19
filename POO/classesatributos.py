# Metodos e instancias de classes

class Carro:
    def __init__(self, nome):
        self.nome = nome
    
    def acelerar(self):
        for i in range (10, 100):
            print(f'O carro {self.nome} esta a {i}km/h')


fusca = Carro('Fusca')
print(fusca.nome)

class Animal:
    def __init__(self, nome):
        self.nome = nome

leao = Animal('Leão')

print(leao.nome)
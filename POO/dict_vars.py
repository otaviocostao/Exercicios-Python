class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

p1 = Pessoa('Otavio', 20)

print(p1.get_ano_nascimento())
print(p1.__dict__)

p1.__dict__['outra'] = 'coisa'
p1.__dict__['nome'] = 'jose'

del p1.__dict__['nome']
print(p1.__dict__)
print(vars(p1))
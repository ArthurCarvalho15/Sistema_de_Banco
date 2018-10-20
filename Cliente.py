# Classe Cliente
class Cliente():
    # Método construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
     # Métodos  get
    def get_nome(self):
        return self.nome
    def get_idade(self):
        return self.idade
    # Método str
    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}'




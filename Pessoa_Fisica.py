# Classe Conta_Fisica
from Cliente import Cliente
class Pessoa_Fisica(Cliente):
    # Método Contrutivo
    def __init__(self, nome, idade, cpf):
        super().__init__(nome, idade)
        self.cpf = cpf

    # Método get
    def get_cpf(self):
        return self.cpf

    # Sobrescrevendo o Método str
    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, CPF: {self.cpf}'

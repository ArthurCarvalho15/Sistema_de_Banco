# Classe Pessoa_Juridica
from Cliente import Cliente

class Pessoa_Juridica(Cliente):
    # Mètodo contrutor
    def __init__(self, nome, idade, cnpj):
        super().__init__(nome, idade)
        self.cnpj = cnpj

    # Método get
    def get_cnpj(self):
        return self.cnpj

    # Sobrescrevendo o Método str
    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, CNPJ: {self.cnpj}'

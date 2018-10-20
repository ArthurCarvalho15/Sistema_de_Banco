# Classe Debito
# Importando a classe Cartao
from Cartao import Cartao

class Debito(Cartao):
    # Método construtivo
    def __init__(self, numero, validade, security_code):
        super().__init__(numero, validade, security_code)
# Classe Conta
class Conta:
    # Método costrutor
    def __init__(self, account_number, agencia):
        self.account_number = account_number
        self.agencia = agencia
    # Método get
    def get_account_number(self):
        return self.account_number
    def get_agencia(self):
        return self.agencia

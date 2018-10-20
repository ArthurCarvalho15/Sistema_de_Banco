# Arquivo Principal
# Importar as classes
from Pessoa_Fisica import Pessoa_Fisica
from Pessoa_Juridica import Pessoa_Juridica
from Conta import Conta
from Credito import Credito
from Debito import Debito

# Criando os objetos
fisica = Pessoa_Fisica('João', 18, '123456')
juridica = Pessoa_Juridica('José', 25, '987654')
conta1 = Conta('111111', 'BRB')
conta2 = Conta('222222', 'Bradesco')
credito = Credito('9874563210', '04/21', '999')
debito = Debito('0123654789', '05/23', '111')
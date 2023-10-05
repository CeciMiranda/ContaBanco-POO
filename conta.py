from datetime import date
  
class Cliente:
  def __init__(self, nome, sobrenome, cpf):
    self.nome = nome
    self.sobrenome = sobrenome
    self.cpf = cpf

  
class Conta:
  def	__init__(self, numero, titular, sobrenome, cpf,	saldo, limite, data_abertura=date.today()):
    self.numero = numero
    self.titular = titular
    self.sobrenome = sobrenome
    self.cpf = cpf
    self.saldo = saldo
    self.limite = limite
    self.data_abertura = data_abertura
  
  def dtAbertura (self):
    print(f'Conta: {self.numero} \nData de abertura: {self.data_abertura}')
     
  def deposito (self, valor):
    self.saldo += valor
    return True

  def saque (self, valor):
    if self.saldo < valor:
      return False
    else:
      self.saldo -= valor
      return True  
      
  def extrato(self):
    print(f"Número: {self.numero}\nTitular: {self.titular} \nSaldo R${self.saldo},00")
    return True

  def transferencia (self, destino, valor):
    retirou = self.saque(valor)
    if (retirou == False):
      return False
    else:
      destino.deposito(valor)
      return True
  

    
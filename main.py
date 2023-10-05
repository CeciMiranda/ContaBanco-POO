from conta import Conta
from conta import Cliente


cliente1 = Cliente('Ana Clara', 'Bonifacio', '456-7')
cliente2 = Cliente('João Lucas', 'Crescencio', '678-9')
cliente3 = Cliente('Rickson', 'Rocha', '345-6')

conta1 = Conta('123-4', cliente1.nome, cliente1.sobrenome, cliente1.cpf,	120,	1000)
conta2 = Conta('432-1', cliente2.nome, cliente2.sobrenome, cliente2.cpf, 150, 1000)
conta3 = Conta('098-7', cliente3.nome, cliente3.sobrenome, cliente3.cpf, 100, 1000)

print(conta1.dtAbertura())
print(conta1.saque(50))
print(conta1.transferencia(conta2, 20))
print(conta1.extrato())
print(conta2.extrato())





  
# qual o objetivo do sistema:
# simulação de um banco

# o que banco tem?
# cadastro
# saldo
# saque
# deposito
# extrato 

saldo =  5000.20  # real / float
senha = 1234

print('Banco Z... ')
print('Seja bem vindo(a)')
senha  =  int(input('Digite sua senha: '))
op = input('''
            Escolha a operaçao:
            
            1 - Saque
            2 - Deposito
            3 - Extrato
            
            ''')
resultado = op == '1' and float(input('Você escolheu saque R$: ')) - saldo or op == '2' and float(input('Você escolheu Deposito')) + saldo or ('Extrato: ', saldo)
print(resultado)




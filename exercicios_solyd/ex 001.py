'''EXERCICIO: cRIE UM SOFTWARE DE GERENCIAMENTO BANCARIO.
ESTE SOFTWARE PODERA SER CAPAZ DE CRIAR CLIENTES E CONTAS
CADA CLIENTE POSSUI NOME CPF IDADE.
CADA CONTA POSSUI UM CLIENTE, E POSSUI UM SALDO, LIMITE, SACAR , DEOISUTAR, E CONSULTAR SALTO'''

from time import sleep

class clientes:

    cliente = list()
    conta = list()

    def __init__(self):
        pass
    def criar_cliente(self):
        titulo('CADASTRO DE USUARIO')
        nome = input('Nome: ')
        cpf = input('cpf: ')
        idade = int(input('Idade: '))
        pessoa = [nome, cpf, idade, 0]
        print(nome,cpf,idade,pessoa)
        cliente.append(pessoa)
        print(clientes)
        sleep(1)


class contas(clientes):

    def consultar_saldo(self):
        titulo('Qual cliente deseja consultar:')
        sleep(1)
        print(self.clientes)
        for i, v in enumerate(self.clientes):
            print(f'{i} - {v[0]}')
            sleep(0.5)
        resp = int(input('Nº cliente: '))


def titulo(frase):
    print('=' * (len(frase) + 6))
    print(f'   {frase}')
    print('=' * (len(frase) + 6))

def menu():
    print('=' * 20)
    print('   BANCO SILVERIO')
    print('=' * 20)
    print(f'''[ 1 ] Criar cliente
[ 2 ] Consultar saldo.
[ 3 ] Depositar.
[ 4 ] Sacar.''')
    print('=' * 20)

while True:
    menu()
    opc = int(input('Digite sua opcao: '))
    cliente = clientes()
    conta = contas()
    if opc == 1:
        cliente.criar_cliente()
    if opc == 2:
        conta.consultar_saldo()
def menu():
    print('''           MENU
===============================
[ 1 ] Cadastrar nova pessoa.
[ 2 ] Listar pessoas.
[ 3 ] Remover pessoa cadastrada
[ 4 ] Adicionar codigo.
===============================''')

logpessoas = 'logpessoas.txt'

def arquivo_existe(arquivo_txt):
    try:
        a = open(arquivo_txt, 'rt')
        a.close()
    except:
        return False
    else:
        return True


def arquivo_cadastrar(arquivo_txt):
    if not arquivo_existe(arquivo_txt):
        with open(arquivo_txt, 'wt+'):
            pass
    print('=' * 20)
    nome = input('Digite o nome: ').title().strip()
    data = int(input('data de nascimento: '))
    cpf = input('CPF: ').strip()
    cidaden = input('Cidade natal: ').strip()
    tel = int(input('Numero de telefone: '))
    with open(arquivo_txt, 'wt') as arq:
        arq.write(f'{nome};{data};{cpf};{cidaden};{tel}\n')
    print('=' * 20)

def arquivo_listar(arquivo_txt):
    if not arquivo_existe(arquivo_txt):
        with open (arquivo_txt, 'wt+'):
            pass
    with open (arquivo_txt, 'rt') as arq:
        if arq.read() == '':
            print('=' * 35)
            print('    NENHUMA PESSOA CADASTRADA')
            print('=' * 35)
        else:
            arquivo = arq.read().split(';')
            for linha in arquivo:
                print(linha)


while True:
    menu()
    opcao = int(input('Digite a opcão: '))
    if opcao == 1:
        arquivo_cadastrar(logpessoas)
    if opcao == 2:
        arquivo_listar(logpessoas)

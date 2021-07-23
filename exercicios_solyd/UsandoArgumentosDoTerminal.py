import sys

argumentos = sys.argv
print(argumentos)

def soma(n1,n2):
    return n1 + n2


def subtracao(n1,n2):
    return n1 - n2

if argumentos[1] == 'soma':
    print(f'A soma dos resultados da {soma(argumentos[2],argumentos[3])}')
elif argumentos[1] == 'subtracao':
    print(f'A soma dos resultados da {subtracao(argumentos[2],argumentos[3])}')
else:
    print('Voce precisa passar argumentos')
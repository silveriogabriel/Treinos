'''EXERCICIO: cRIE UM SOFTWARE DE GERENCIAMENTO BANCARIO
ESSE software podera ser capas de criar clientes e contas
cada cliente possui nome, cpf, idade
cada conta possui um cliente salto limite sacar depositar e consultar salto'''

import PySimpleGUI as ps


class TelaLoginPython:
    def __init__(self):
        # layout
        self.layout = [
            [ps.Text('LOGIN')],
            [ps.Text('Usuario:'), ps.Input(size=(15, 0), key='usuario')],
            [ps.Text('Senha:  '), ps.Input(size=(15, 0), key='senha')],
            [ps.Button('ENTER'), ps.Button('REGISTRAR', size=(15, 0))],
        ]
        # tela
        self.janela = ps.Window('BANCO SILVERIO').layout(self.layout)

    def iniciar(self):
        # extrair dados
        senha = 'abobrinha'
        usuario = 'pantera'
        while True:
            self.button, self.values = self.janela.read()
            if self.button == ps.WINDOW_CLOSED:
                break
            if self.values['usuario'] == usuario and self.values['senha'] == senha or self.button == 'REGISTRAR':
                self.janela = ps.WINDOW_CLOSED
            else:
                print('Usuario/Senha inexistente!!')


class TelaRegistrarPython:
    def __init__(self):
        # layout
        self.layout = [
            [ps.Text('CADASTRE-SE')],
            [ps.Text('Usuario:'), ps.Input(size=(15, 0), key='usuario')],
            [ps.Text('Senha:  '), ps.Input(size=(15, 0), key='senha')],
            [ps.Button('ENTER'), ps.Button('REGISTRAR', size=(15, 0))],
        ]
        # janela
        self.janela = ps.Window('REGISTRAR', layout=self.layout)

    def iniciar(self):
        while True:
            self.button, self.values = self.janela.read()


tela = TelaLoginPython()
tela2 = TelaRegistrarPython()
tela.iniciar()
tela2.iniciar()
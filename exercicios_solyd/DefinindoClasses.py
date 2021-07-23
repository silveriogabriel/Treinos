class Veiculo:

    def __init__(self, cor='defalt', rodas='defalt', marca='defalt', litros=0):
        self.cor = cor
        self.rodas = rodas
        self.marca = marca
        self.tanque = litros

    def abastecer(self, litros):
        self.tanque = self.tanque + litros

carro_azul = Veiculo('azul', 4, 'volkswagem', 40)
print(f'{carro_azul.tanque}')
carro_azul.abastecer(10)
print(f'{carro_azul.tanque}')
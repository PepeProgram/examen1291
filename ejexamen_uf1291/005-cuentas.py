#  Copyright (c) 2023. José Manuel Abelleira López.
#

class Cuenta:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def ingresar(self, importe):
        self.saldo += importe
        return self.saldo

    def retirar(self, importe):
        if self.saldo < importe:
            print('No hay saldo suficiente')
        else:
            self.saldo -= importe
        return self.saldo

    def estado(self):
        print(f'El saldo actual es {self.saldo}')


c0321 = Cuenta('Pepe')
print('Ingreso 3000')
c0321.ingresar(3000)
c0321.estado()
print('Retiro 1500')
c0321.retirar(1500)
c0321.estado()
print('Retiro 2000')
c0321.retirar(2000)
c0321.estado()

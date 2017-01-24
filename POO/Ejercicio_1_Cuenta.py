'''
Created on 10 ene. 2017

@author: MariaJesus
'''
class Cuenta (object):
    saldo=0.0
    def __init__(self,saldo):
        self.saldo=saldo
    def ingresar (self,cantidad):
        self.saldo=self.saldo+cantidad
        print(self.saldo)
    def  retirar (self,cantidad):
        if cantidad<self.saldo:
            self.saldo=self.saldo-cantidad
            print(self.saldo)
        else:
            print("Error: Usted no dispone de la cantidad que solicita")
cuenta1=Cuenta(0.0)
cantidades=[125.00, 530.00, 50.00, 333.00]
for i in range (1):
    cuenta1.ingresar(cantidades[0])
for i in range (1):
    cuenta1.ingresar(cantidades[1])
for i in range (1):
    cuenta1.ingresar(cantidades[2])
for i in range (1):
    cuenta1.retirar(cantidades[3])
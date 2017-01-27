'''
Created on 10 ene. 2017

@author: MariaJesus
'''
from POO.Ejercicio_2_Persona import Persona
class Cuenta (object):
    def __init__(self,saldo,pin):
        self.__saldo=saldo
        self.pin=pin
    def ingresar (self,cantidad):
        self.__saldo=self.__saldo+cantidad
        # print(self.__saldo)
    def  retirar (self,cantidad):
        if cantidad<self.__saldo:
            self.__saldo=self.__saldo-cantidad
            # print(self.__saldo)
        else:
            print("Error: Usted no dispone de la cantidad que solicita")
    def Leer_Saldo (self, Pin):
        if self.pin==Pin:
            print(self.__saldo)
        else:
            print("Error: El número PIN es incorrecto")
    def Desocultar_Saldo (self):
        return self.__saldo
#--------------------------------------------------------------------
class Cuenta_ahorro(Cuenta):
    def __avisar(self,cantidad):
        if cantidad>super(Cuenta_ahorro,self).Desocultar_Saldo():
            print("Numeros rojos")
    def avisar_a(self,cantidad):
        self.avisar_a(cantidad)
#--------------------------------------------------------------------
class Cliente(Persona,Cuenta_ahorro):
    def __init__(self,Nombre,DNI,direccion,tlf,email,saldo,pin):
        Persona.__init__(self, Nombre, DNI, direccion, tlf, email)
        Cuenta_ahorro.__init__(self, saldo, pin)
        self.credit=1000       
    def mostar_datos (self):
        print(self.Nombre, self.DNI, self.direccion, self.tlf, self.Desocultar_Saldo(), self.credit)
        if self.email!="":
            print(self.email)
#--------------------------------------------------------------------
if __name__== '__main__':
#Programa principal
    cuenta1=Cuenta(0.0, 1313)
    cantidades=[125.00, 124.00,]
    for i in range (1):
        cuenta1.ingresar(cantidades[0])
    for i in range (1):
        cuenta1.retirar(cantidades[1])
pin=int(input("Escriba su pin por favor:"))
cuenta1.Leer_Saldo(pin)
persona1=Cliente("Antonio","24597852W","C/Socrates","958414141","antonioelshulo@gmail.com",5.0,pin)
#Segundo programa principal
persona1.mostar_datos()
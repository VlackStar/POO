'''
Created on 10 ene. 2017

@author: MariaJesus
'''
class Persona (object):
    def __init__(self, Nombre, DNI, direccion, tlf, email):
        self.Nombre=Nombre
        self.DNI=DNI
        self.direccion=direccion
        self.tlf=tlf
        self.email=email
    def mostar (self,Nombre,DNI,direccion,tlf,email):
        print(self.Nombre, self.DNI, self.direccion, self.tlf)
        if self.email!="":
            print(self.email)
if __name__== '__main__':
    clase_tic=[]
    for n in range (10):
        nombre=input("Nombre: ")
        DNI=input("DNI: ")
        direccion=input("Dirección: ")
        tlf=input("Tlf: ")
        email=input("E-mail:")
        clase_tic.append(Persona (nombre,DNI,direccion,tlf,email))
    for i in range (10):
        clase_tic[i].mostrar()
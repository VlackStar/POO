'''
Created on 31 ene. 2017

@author: MariaJesus
'''
class Fraccion (object):
    def __init__(self,numerador,denominador = 1):
        self.numerador=numerador
        self.denominador=denominador
#----------------------------------------------------------#
    def euclides (self,A,B):
        if A==0:
            return B
        elif B==0:
            return A
        return self.euclides (B,A%B)     
#----------------------------------------------------------#
    def __add__(self,other):
        denominador= self.denominador * other.denominador
        numerador1=self.numerador * other.denominador
        numerador2=other.numerador * self.numerador
        numerador= numerador1+numerador2
        return numerador/self.euclides(numerador, denominador), denominador/self.euclides(numerador, denominador)
#----------------------------------------------------------#
    def __sub__(self,other):
        denominador= self.denominador * other.denominador
        numerador1=self.numerador * other.denominador
        numerador2=other.numerador * self.numerador
        numerador= numerador1-numerador2
        return numerador/self.euclides(numerador, denominador), denominador/self.euclides(numerador, denominador)
#----------------------------------------------------------#
    def __mul__(self,other):
        numerador= self.numerador * other.numerador
        denominador= self.denominador * other.denominador
        return numerador/self.euclides(numerador, denominador), denominador/self.euclides(numerador, denominador)
#----------------------------------------------------------#
    def __truediv__(self,other):
        numerador=self.numerador*other.denominador
        denominador=self.numerador*other.denominador
        return numerador/self.euclides(numerador, denominador), denominador/self.euclides(numerador, denominador)
#----------------------------------------------------------#
Fraccion1 = Fraccion(1,2)
Fraccion2 = Fraccion(3,4)
print(Fraccion1+Fraccion2)
print(Fraccion1-Fraccion2)
print(Fraccion1*Fraccion2)
print(Fraccion1/Fraccion2)
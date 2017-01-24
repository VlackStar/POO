'''
Created on 10 ene. 2017

@author: MariaJesus
'''
import math
class Punto:
    x0=0
    y0=0
    x=""
    y=""
    def __init__ (self,x,y):
        self.y=y
        self.x=x    
    def distancia (self):
        return math.sqrt(self.x**2+self.y**2)
    def muestra_punto (self):
        print(self.x)
        print(self.y)
punto1=Punto (0,0)
punto2=Punto (12,12)
punto1.muestra_punto()
if punto1.distancia>punto2.distancia():
    punto2.muestra_punto()
else:
    punto1.muestra_punto()
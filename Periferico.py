'''
Created on 27-10-2012

'''
class Periferico:
    
    def __init__(self,nombre):
        self.bloqueado=False
        self.nombre=nombre
        
    def bloquear(self):
        self.bloqueado=True
        
    def desbloquear(self):
        self.bloqueado=False
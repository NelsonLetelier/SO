
sistema=None
class lector:    
    @staticmethod
    def leer(sistema,queue1, queue3):
        f = open("example.txt")
        sistema.makeProcess(f.readlines(),queue1,queue3)
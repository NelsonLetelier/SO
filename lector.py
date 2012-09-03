import SO

sistema=None
class lector:    
    @staticmethod
    def leer(args):
        global sistema
        sistema=args
        f = open("/Users/nletelier/code/SO/example.txt")
        sistema.makeProcess(f.readlines())
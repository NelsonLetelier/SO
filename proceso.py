class proceso:
    
    def __init__(self, nombre, fecha, tipoProceso, prioridadBase, opciones):
        self.name = nombre
        self.fecha = int(fecha)
        self.tipoProceso = int(tipoProceso)
        self.prioridadBase = int(prioridadBase)
        self.prioridad = int(prioridadBase)
        self.opciones = opciones
        self.tiempoEjecutado = 0
        self.tiempoEjecucion = 5
        
        
    def getTiempoEjecutado(self):
        return self.tiempoEjecutado


    def setTiempoEjecutado(self, value):
        self.tiempoEjecutado = value


    def getName(self):
        return self.name

    def getFecha(self):
        return self.fecha

    def getPrioridad(self):
        return self.prioridad
t=0
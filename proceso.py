class proceso:
    
    def __init__(self, nombre, fecha, tipoProceso, prioridadBase, opciones):
        self.name = nombre
        self.fecha = int(fecha)
        self.tipoProceso = int(tipoProceso)
        self.prioridadBase = int(prioridadBase)
        self.prioridad = int(prioridadBase)
        self.opciones = opciones
        self.tiempoEjecutado = 0
        self.perifericosUsa=list()
        self.perifericosBloquea=list()
        if self.tipoProceso == 1 or self.tipoProceso == 2:
            self.perifericosUsa=["Pantalla","Audifono","Microfono","EnviarInfo","RecibirInfo"]
            self.perifericosBloquea=["Audifono","Microfono"]
            self.tiempoEjecucion= float(opciones[1])
        elif self.tipoProceso == 3 or self.tipoProceso == 4:
            self.tiempoEjecucion = 0.02*len(opciones[1])
            self.perifericosUsa=["Audifono","EnviarInfo","RecibirInfo"]
        elif self.tipoProceso == 5:
            self.tiempoEjecucion = 1
            self.perifericosUsa=["Pantalla"]
        elif self.tipoProceso == 7:
            self.tiempoEjecucion = 2
            self.perifericosUsa=["GPS","EnviarInfo"]
        else:
            self.tiempoEjecucion = float(opciones[0])
            if self.tipoProceso==6:
                self.perifericosUsa=["Pantalla","Audifono","Microfono","GPS","EnviarInfo","RecibirInfo"]
            elif self.tipoProceso==8:
                self.perifericosUsa=["Pantalla","GPS"]
            elif self.tipoProceso==9:
                self.perifericosUsa=["Pantalla","Audifono","GPS","EnviarInfo","RecibirInfo"]
            elif self.tipoProceso==10:
                self.perifericosUsa=["Pantalla","Audifono"]         
        
        
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
            
        

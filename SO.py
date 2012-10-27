import proceso
import multiprocessing
import lector
import time
import datetime
import Periferico

class SO:
    def __init__(self):
        self.procesos = list()
        self.procesosEnWaiting = list()
        self.lock=multiprocessing.Lock()
        self.procesosActuales=list()
        self.proceso = None
        self.t=0
        self.perifericos=[Periferico.Periferico("Pantalla"),Periferico.Periferico("Audifono"),Periferico.Periferico("Microfono")
                         ,Periferico.Periferico("GPS"),Periferico.Periferico("EnviarInfo"),Periferico.Periferico("RecibirInfo")]

    def makeProcess(self,lines,queue1,queue3):
        t1=0
        for line in lines:
            props = line.split(';')
            opciones = list()
            for i in range(4, len(props)):
                opciones.append(props[i])
            while not queue1.empty():
                t1=queue1.get()
            process = proceso.proceso(props[0], int(props[1])+t1, props[2], props[3], opciones)
            self.procesos.append(process)
        queue3.put(sorted(self.procesos, key=lambda proceso: proceso.fecha))

    def llamar(self, queue2):
        numero = int(raw_input("Ingrese el numero al cual desea llamar\n"))
        print "Llamando... \n", str(numero)
        horaInicio = datetime.datetime.now()
        l=list()
        l.append(numero)
        l.append(15)
        p = proceso.proceso("Hacer_Llamada", 0, 1, 0,l)
        while not queue2.empty():
            self.procesosEnWaiting = queue2.get()
        self.procesosEnWaiting.append(p)
        queue2.put(sorted(self.procesosEnWaiting, key= lambda proceso: proceso.prioridad))
        cancelar = 1
        cancelar = int(raw_input("(0) Cortar"))
        horaTermino = datetime.datetime.now()
        tiempo = horaTermino - horaInicio
        print "Llamada finalizada\n"
        print "Tiempo de llamada: \n", str(tiempo)
        f=open("Historial.txt", "a")
        linea = str(numero) + ";" + str(horaInicio) + ";" + str(tiempo) + "\n"
        f.write(linea)
        f.close()
    

    def enviar_mensaje(self, queue2):
        while not queue2.empty():
            self.procesosEnWaiting=queue2.get()
        numero = int(raw_input("Ingrese el numero al cual desea mandarle un mensaje\n"))
        mensaje = raw_input("Escriba el mensaje\n")
        time = datetime.datetime.now()
        l = list()
        l.append(numero)
        l.append(mensaje)
        p = proceso.proceso("enviar_mensaje", 0, 3, 2, l)
        self.procesosEnWaiting.append(p)
        self.procesosEnWaiting = sorted(self.procesosEnWaiting, key=lambda proceso: proceso.prioridad)#ordeno la lista seun prioridad
        queue2.put(self.procesosEnWaiting)
        f=open("Mensajes.txt", "a")
        linea = "Mensaje_Enviado" + ":" + str(numero) + ";" + str(time)+ ";" + mensaje + "\n"
        f.write(linea)
        f.close()


    def revisar_agenda(self):
        ##muestro los contactos y pregunto a cual quiere llamar o enviar mensaje
        print "Contactos\n"
        f= open("Contactos.txt")
        while True:
            linea = f.readline()
            if not linea: break
            print linea

    def ver_historial(self):
        print "Historial\n"
        f=open("Historial.txt")
        while True:
            linea = f.readline()
            if not linea: break
            print linea

    def ver_mensajes(self):
        print "Mensajes\n"
        f=open("Mensajes.txt")
        while True:
            linea = f.readline()
            if not linea: break
            print linea

    def agregar_contacto(self):
        nombre = raw_input("Ingrese el nombre del contacto\n")
        numero = raw_input("Ingrese el numero del contacto\n")
        f=open("Contactos.txt", "a")
        linea = nombre + ";" + numero + "\n"
        f.write(linea)
        


    def ver_procesos(self,queue2,queue4):
        ##muestro los procesos ejecutandose
        while not queue4.empty():
            self.procesosActuales=queue4.get()
        if len(self.procesosActuales)==0:
            print "no hay procesos ejecutandose"
        else:
            for proceso in self.procesosActuales:
                print proceso.name+"\t"+"running"
        while not queue2.empty():
            self.procesosEnWaiting=queue2.get()
        for proceso in self.procesosEnWaiting:
            print proceso.name

    def ejecutar_proceso(self, nombre, queue1, queue2, queue3):
        if nombre == "Llamar":
            self.llamar(queue2)
        elif nombre == "Mandar mensaje": 
            self.enviar_mensaje(queue2)
        elif nombre == "Ver contactos":
            self.revisar_agenda()
        elif nombre == "Revisar historial":
            self.ver_historial()
        elif nombre == "Ver procesos":
            self.ver_procesos(queue2)
        elif nombre == "Cargar archivo":
            self.cargar_archivo(queue1, queue3)
        elif nombre == "Salir":
            self.terminar()
        else: 
            print "\nNombre de proceso invalido, escriba el proceso que desea ejecutar tal como se ve en el menu."
            nombre = nombreProcesoEjecutar = raw_input("Ingrese el nombre del proceso que desea ejecutar\n")
            self.ejecutar_proceso(nombreProcesoEjecutar, queue1, queue2, queue3)

    def cargar_archivo(self,queue1, queue3):
        lector.lector.leer(self,queue1,queue3)  

    def simular(self, queue1, queue2, queue3, queue4):
        while True:
            while not queue2.empty():
                self.procesosEnWaiting=queue2.get()
            while not queue3.empty():
                self.procesos=queue3.get()          
            while not len(self.procesos)==0 or not len(self.procesosActuales)==0 or not len(self.procesosEnWaiting)==0:#Mientras hayan procesos por llegar se sigue simulando
                #Proceso que acaba de llegar:
                if not len(self. procesos)==0:
                    procesoNuevo=self.procesos.pop(0)
                    procesoBloqueado=False
                    for periferico in self.perifericos:
                        if periferico.bloqueado:
                            for usado in procesoNuevo.perifericosUsa:
                                if usado==periferico.nombre:
                                    procesoBloqueado=True
                    if not procesoBloqueado:
                        self.procesosActuales.append(procesoNuevo)
                        for bloqueado in procesoNuevo.perifericosBloquea:
                            for periferico in self.perifericos:
                                if bloqueado==periferico.nombre:
                                    periferico.bloquear()
                                    for proceso in self.procesosActuales:
                                        if not proceso==procesoNuevo:
                                            if not proceso.perifericosUsa.count(periferico.nombre)==0:
                                                self.procesosActuales.remove(proceso)
                                                self.procesosEnWaiting.append(proceso)
                    else:
                        self.procesosEnWaiting.append(procesoNuevo)
                #Round Robin:
                if not len(self.procesosActuales)==0:
                    procesoActual=self.procesosActuales.pop(0)
                    procesoActual.tiempoEjecutado=procesoActual.tiempoEjecutado+0.1
                    if(procesoActual.tiempoEjecutado>=procesoActual.tiempoEjecucion):
                        for periferico in self.perifericos:
                            for bloqueado in procesoActual.perifericosBloquea:
                                if(periferico.nombre==bloqueado):
                                    periferico.desbloquear()
                        if procesoActual.tipoProceso==1:#Guarda la llamada en el historial
                            f=open("Historial.txt", "a")
                            tiempo = datetime.datetime.now()
                            linea = str(procesoActual.opciones[0]) + ";" + str(tiempo) + ";" + str(procesoActual.opciones[1]) + "\n"
                            f.write(linea)
                            f.close()
                        elif procesoActual.tipoProceso==2:#Guarda la llamada recibida en el historial
                            f=open("Historial.txt", "a")
                            tiempo = datetime.datetime.now()
                            linea = str(procesoActual.opciones[0]) + ";" + str(tiempo) + ";" + str(procesoActual.opciones[1]) + "\n"
                            f.write(linea)
                            f.close()
                        elif procesoActual.tipoProceso==3:#Guarda el mensaje enviado en mensajes
                            f=open("Mensajes.txt", "a")
                            tiempo = datetime.datetime.now()
                            linea = "Mensaje_Enviado" + ":" + str(procesoActual.opciones[0]) +";" + str(tiempo)+";"+ procesoActual.opciones[1]
                            f.write(linea)
                            f.close()
                        elif procesoActual.tipoProceso==4:#Guarda el mensaje recibido en mensajes
                            f=open("Mensajes.txt", "a")
                            tiempo = datetime.datetime.now()
                            linea = "Mensaje_Recibido" + ":" + str(procesoActual.opciones[0]) +";" + str(tiempo)+";"+ procesoActual.opciones[1]
                            f.write(linea)
                            f.close()
                        elif procesoActual.tipoProceso==5:#Agrego el contacto
                            f=open("Contactos.txt", "a")
                            linea = procesoActual.opciones[0] + ";" + procesoActual.opciones[1]
                            f.write(linea)
                    else:
                        self.procesosActuales.append(procesoActual)
                #Meter desde waiting:
                for proceso in self.procesosEnWaiting:
                    procesoBloqueado=False
                    for periferico in self.perifericos:
                        if periferico.bloqueado:
                            for usado in proceso.perifericosUsa:
                                if usado==periferico.nombre:
                                    procesoBloqueado=True
                    if not procesoBloqueado:
                        self.procesosActuales.append(proceso)
                        self.procesosEnWaiting.remove(proceso)
                        for bloqueado in proceso.perifericosBloquea:
                            for periferico in self.perifericos:
                                if bloqueado==periferico.nombre:
                                    periferico.bloquear()
                                    for procesoReady in self.procesosActuales:
                                        if not proceso==procesoReady:
                                            if not procesoReady.perifericosUsa.count(periferico.nombre)==0:
                                                self.procesosActuales.remove(procesoReady)
                                                self.procesosEnWaiting.append(procesoReady)
                self.t = self.t + 0.1
                queue1.put(self.t)
                time.sleep(0.1)
                queue2.put(self.procesosEnWaiting)
                queue4.put(self.procesosActuales)    
                            
                                    
                            
            
            

    def start(self,queue1,queue2,queue3,queue4):
        self.proceso=multiprocessing.Process(target=self.simular, args=(queue1,queue2,queue3,queue4))
        self.proceso.start()

    def terminar(self):
        self.proceso.terminate()

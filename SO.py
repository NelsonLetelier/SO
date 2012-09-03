import proceso
import multiprocessing
import lector
import time

class SO:
    def __init__(self):
        self.procesos = list()
        self.procesosEnCola = list()
        self.lock=multiprocessing.Lock()
        self.procesoActual="ninguno"
        self.proceso = None
        self.t=0

    def makeProcess(self,lines):
        for line in lines:
            props = line.split(';')
            opciones = list()
            for i in range(4, len(props)):
                opciones.append(props[i])            
            process = proceso(props[0], int(props[1])+t, props[2], props[3], opciones)
            self.procesos.append(process)
        self.procesos = sorted(self.procesos, key=lambda proceso: proceso.fecha)

    def llamar(self):
        numero = int(raw_input("Ingrese el numero al cual desea llamar\n"))
        print "Llamando... \n", numero
        ##guardar la hora, numero, tiempo de duracion
    

    def enviar_mensaje(self):
        numero = int(raw_input("Ingrese el numero al cual desea mandarle un mensaje\n"))
        mensaje = int(raw_input("Escriba el mensaje\n"))
        ##guardar el numero y el mensaje en el archivo memoria


    def revisar_agenda(self):
        ##muestro los contactos y pregunto a cual quiere llamar o enviar mensaje
        print "Contactos"

    def ver_historial(self):
        print "Historial\n"

    def ver_procesos():
        ##muestro los procesos ejecutandose
        procesos = open("procesos.txt")

    def ejecutar_proceso(nombre):
        ##ejecuta el proceso nombre
        print "Ejecutando proceso ", nombre

    def cargar_archivo(self):
        lector.lector.leer(self)  

    def simular(self):
        while True:
            while not len(self.procesos)==0 or not len(self.procesosEnCola)==0:#Mientras hayan procesos en cola o hayan procesos por llegar se sigue simulando
                if not self.procesoActual == "ninguno":#Si hay un proceso activo, su tiempo ejecutado aumenta con cada ciclo
                    procesoActual.tiempoEjecutado += 1
                    if procesoActual.tiempoEjecutado == procesoActual.tiempoEjecucion:#Si ya se ejecuto todo lo que debia, el proceso actual se sale
                        if len(self.procesosEnCola) == 0:#Si no hay procesos esperando, no se ejecuta ningun proceso
                            self.procesoActual = "ninguno"
                        else:#Si hay procesos esperando, entonces el primero pasa a ser el proceso actual
                            self.procesoActual = self.procesosEnCola[0]
                            self.procesosEnCola.remove(self.procesosEnCola[0])
                            print str(t) + "\t" + self.procesoActual.getName()
                if not len(self.procesos) == 0 and t >= self.procesos[0].fecha:#Si llega un proceso (considerando que hay procesos por llegar)
                    if self.procesoActual == "ninguno":#Si no habia ningun proceso ejecutandose, pasa directamente a procesarse
                            self.procesoActual = self.procesos[0]
                            print str(self.t) + "\t" + self.procesoActual.getName()
                            self.procesos.remove(self.procesos[0])
                    else:
                        if self.procesos[0].prioridad > procesoActual.prioridad: #Si el proceso que entra tiene mayor prioridad que el proceso que se esta ejecutando
                            self.procesosEnCola.append(procesoActual)#Asigno como proceso actual al nuevo proceso
                            procesoActual= self.procesos[0]#Meto a la cola el proceso que se estaba ejecutando
                        else:#Si no, lo meto a la cola
                            self.procesosEnCola.append(self.procesos[0])                                
                        self.procesosEnCola = sorted(self.procesosEnCola, key=lambda proceso: proceso.prioridad)#ordeno la lista seun prioridad
                        self.procesos.remove(self.procesos[0])#Elimino al proceso de la lista procesos
            self.t = self.t + 1 
            time.sleep(1)

    def start(self):
        self.proceso=multiprocessing.Process(target=self.simular)
        self.proceso.start()

    def terminar(self):
        self.proceso.terminate()
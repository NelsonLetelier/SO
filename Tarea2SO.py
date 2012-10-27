import SO
import sys
import time
import multiprocessing       

if __name__ == '__main__':
    queue1=multiprocessing.Queue()
    queue2=multiprocessing.Queue()
    queue3=multiprocessing.Queue()
    queue4=multiprocessing.Queue()
    sistema=SO.SO()
    sistema.start(queue1,queue2,queue3,queue4)
    print "MENU\n"
    opcion= 1
    while opcion !=0:
        opcion = int(raw_input("(1) Llamar\n(2) Mandar mensaje\n(3) Ver contactos\n(4) Revisar historial\n(5) Ver procesos\n(6) Cargar archivo\n(7) Ejecutar proceso\n(8) Ver mensajes\n(9) Agregar contacto\n(0) Salir\n"))
        if opcion == 1:
            sistema.llamar(queue2)
        elif opcion ==2:
            sistema.enviar_mensaje(queue2)
        elif opcion == 3:
            sistema.revisar_agenda()
        elif opcion == 4:
            sistema.ver_historial()
        elif opcion == 5:
            sistema.ver_procesos(queue2,queue4)
        elif opcion == 6:
            sistema.cargar_archivo(queue1,queue3)
            time.sleep(1)
        elif opcion == 7:
            nombreProcesoEjecutar = raw_input("Ingrese el nombre del proceso que desea ejecutar\n")
            sistema.ejecutar_proceso(nombreProcesoEjecutar, queue1, queue2, queue3)
        elif opcion == 8:
            sistema.ver_mensajes()
        elif opcion == 9:
            sistema.agregar_contacto()
        elif opcion == 0:
            sistema.terminar()
            print "Hasta Luego"
        else:
            print "\nOpcion invalida\n"
